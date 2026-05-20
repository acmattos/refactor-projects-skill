class Payment {
    constructor({ id, enrollmentId, amount, status }) {
        this.id = id;
        this.enrollmentId = enrollmentId;
        this.amount = amount;
        this.status = status;
    }

    isApproved() {
        return this.status === 'PAID';
    }

    static approve(cardNumber) {
        return cardNumber.startsWith('4') ? 'PAID' : 'DENIED';
    }
}

module.exports = Payment;
