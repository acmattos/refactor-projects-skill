const db = require('../infrastructure/database');

async function log(action) {
    await db.run(
        "INSERT INTO audit_logs (action, created_at) VALUES (?, datetime('now'))",
        [action]
    );
}

module.exports = { log };
