# -*- coding: utf-8 -*-                                 
import sys, os

# указываем директорию с проектом 
sys.path.append('/root/flask_app/') 

# указываем директорию с библиотеками, куда поставили Flask
sys.path.append('/root/flask_app/venv/lib/python3.9/site-packages/flask/') 

from HelloFlask import app as application
# Когда Flask стартует, он ищет application. 
# Если не указать 'as application', сайт не заработает

from werkzeug.debug import DebuggedApplication
# Опционально: подключение модуля отладки 

application.wsgi_app = DebuggedApplication(application.wsgi_app, True)
# Опционально: включение модуля отадки

application.debug = False
# Опционально: True/False устанавливается по необходимости в отладке 