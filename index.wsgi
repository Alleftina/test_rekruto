public_html/index.wsgi:
activate_this = '/root/flask_app/venv/bin/python3.9'
exec(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, '/root/flask_app/')
sys.path.insert(1, '/root/flask_app/venv/lib/python3.9/site-packages/')
from flask_test.app import app as application