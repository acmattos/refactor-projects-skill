# Compatibility wrapper — real entry point: src/app.py
# Run with: python app.py  OR  python src/app.py
import sys
import os
import importlib.util

_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_root, "src"))
os.environ.setdefault("DATABASE_URL", os.path.join(_root, "loja.db"))

_spec = importlib.util.spec_from_file_location("_src_app", os.path.join(_root, "src", "app.py"))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
app = _mod.app

if __name__ == "__main__":
    _mod.main()
