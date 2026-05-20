const crypto = require('crypto');
const userRepository = require('../repositories/userRepository');
const courseRepository = require('../repositories/courseRepository');
const enrollmentRepository = require('../repositories/enrollmentRepository');
const paymentRepository = require('../repositories/paymentRepository');
const auditRepository = require('../repositories/auditRepository');
const Payment = require('../models/payment');

function hashPassword(password) {
    const salt = crypto.randomBytes(16).toString('hex');
    const hash = crypto.scryptSync(password, salt, 64).toString('hex');
    return `${salt}:${hash}`;
}

async function checkout({ name, email, password, courseId, cardNumber }) {
    const course = await courseRepository.findActiveById(courseId);
    if (!course) {
        const err = new Error('Curso não encontrado');
        err.status = 404;
        throw err;
    }

    let user = await userRepository.findByEmail(email);
    let userId;

    if (!user) {
        const safePassword = password || crypto.randomBytes(8).toString('hex');
        const hashedPassword = hashPassword(safePassword);
        userId = await userRepository.create(name, email, hashedPassword);
    } else {
        userId = user.id;
    }

    const paymentStatus = Payment.approve(cardNumber);
    if (paymentStatus === 'DENIED') {
        const err = new Error('Pagamento recusado');
        err.status = 400;
        throw err;
    }

    const enrollmentId = await enrollmentRepository.create(userId, courseId);
    await paymentRepository.create(enrollmentId, course.price, paymentStatus);
    await auditRepository.log(`Checkout curso ${courseId} por ${userId}`);

    return { enrollmentId };
}

module.exports = { checkout };
