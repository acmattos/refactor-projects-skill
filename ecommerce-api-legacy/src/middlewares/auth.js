const settings = require('../config/settings');

function auth(req, res, next) {
    const token = req.headers['x-admin-token'];
    if (!settings.adminToken || token !== settings.adminToken) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    next();
}

module.exports = auth;
