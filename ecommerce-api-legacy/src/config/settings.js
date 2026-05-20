const settings = {
    port: parseInt(process.env.PORT) || 3000,
    adminToken: process.env.ADMIN_TOKEN || '',
    paymentGatewayKey: process.env.PAYMENT_GATEWAY_KEY || '',
    smtpUser: process.env.SMTP_USER || '',
    dbPath: process.env.DB_PATH || ':memory:'
};

module.exports = settings;
