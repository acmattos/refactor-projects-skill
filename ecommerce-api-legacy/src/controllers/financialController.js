const financialService = require('../services/financialService');

async function getFinancialReport(req, res, next) {
    try {
        const report = await financialService.getFinancialReport();
        return res.status(200).json(report);
    } catch (err) {
        next(err);
    }
}

module.exports = { getFinancialReport };
