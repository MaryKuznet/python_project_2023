# Веб-приложение по классификации нарисованных пользователем изображений

Создаётся сайт с возмлжностью нарисовать в окне рисунок и отправить на клссификацию модели MobileNet, после чего будет возможность сохранить результат, также есть страничка с сохраненными изображениями.

Идея была использовать модель обученную на датасете QuikDraw!, взяв модель из https://www.kaggle.com/code/gaborfodor/greyscale-mobilenet-lb-0-892/output

## 1-й вариант запуска локально

1. Клонирование репозитория 

```git clone https://github.com/MaryKuznet/python_project_2023.git```

2. Переход в директорию python_project_2023

```cd python_project_2023```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```

6. Запуск скрипта для создании базы данных

```python3 helpers.py --help```

7. Запуск самого приложения
   
```python3 run.py```

И перейдите по появившейся ссылке

## 2-й вариант запуска через docker

Я нашла проблему и сделала так, чтобы с docker работало.

1. Клонирование репозитория 

```git clone https://github.com/MaryKuznet/python_project_2023.git```

2. Переход в директорию python_project_2023

```cd python_project_2023```

3. Собираем контейнер

```docker build -f Dockerfile -t my_app .```

4. Запускаем образ в фоновом режиме

```docker run -d -p 5000:5000 my_app```

5. Перейдите по ссылке http://127.0.0.1:5000
