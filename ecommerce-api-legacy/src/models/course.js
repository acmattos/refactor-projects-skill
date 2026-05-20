class Course {
    constructor({ id, title, price, active }) {
        this.id = id;
        this.title = title;
        this.price = price;
        this.active = active;
    }

    isActive() {
        return this.active === 1;
    }
}

module.exports = Course;
