const express = require('express');
const settings = require('./config/settings');
const { initDb, createSchema, seedDb } = require('./infrastructure/database');
const router = require('./views/routes');
const errorHandler = require('./middlewares/errorHandler');

const app = express();
app.use(express.json());

async function start() {
    initDb(settings.dbPath);
    await createSchema();
    await seedDb();

    app.use(router);
    app.use(errorHandler);

    app.listen(settings.port, () => {
        console.log(`Frankenstein LMS rodando na porta ${settings.port}...`);
    });
}

start().catch(err => {
    console.error('Falha ao iniciar a aplicação:', err);
    process.exit(1);
});
