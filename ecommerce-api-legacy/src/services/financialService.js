const financialRepository = require('../repositories/financialRepository');

async function getFinancialReport() {
    const rows = await financialRepository.getCourseFinancialSummary();

    const courseMap = new Map();

    for (const row of rows) {
        if (!courseMap.has(row.course_title)) {
            courseMap.set(row.course_title, { course: row.course_title, revenue: 0, students: [] });
        }
        const courseData = courseMap.get(row.course_title);

        if (row.student_name) {
            if (row.status === 'PAID') {
                courseData.revenue += row.amount;
            }
            courseData.students.push({
                student: row.student_name,
                paid: row.amount || 0
            });
        }
    }

    return Array.from(courseMap.values());
}

module.exports = { getFinancialReport };
