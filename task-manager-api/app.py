# Wrapper de compatibilidade — mantido para preservar o comando 'python app.py'.
# Entry point real: src/app.py
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from app import app  # noqa: F401 — importa src/app.py

if __name__ == '__main__':
    from config import settings
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
