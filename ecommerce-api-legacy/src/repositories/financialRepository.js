const db = require('../infrastructure/database');

async function getCourseFinancialSummary() {
    return db.all(`
        SELECT
            c.title AS course_title,
            u.name  AS student_name,
            p.amount,
            p.status
        FROM courses c
        LEFT JOIN enrollments e ON e.course_id = c.id
        LEFT JOIN users u ON u.id = e.user_id
        LEFT JOIN payments p ON p.enrollment_id = e.id
    `);
}

module.exports = { getCourseFinancialSummary };
