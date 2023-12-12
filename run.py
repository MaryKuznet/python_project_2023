#!flask/bin/python
from app import app

# Запускаем приложение
app.run(debug=True, host='0.0.0.0', port=5000)