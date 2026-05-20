const userRepository = require('../repositories/userRepository');

async function deleteUser(req, res, next) {
    try {
        const { id } = req.params;
        await userRepository.deleteById(id);
        return res.status(200).json({ msg: 'Usuário removido com sucesso' });
    } catch (err) {
        next(err);
    }
}

module.exports = { deleteUser };
