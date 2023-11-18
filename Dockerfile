FROM python:3.11

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію усередині контейнера
WORKDIR $APP_HOME

COPY poetry.lock $APP_HOME/poetry.lock
COPY pyproject.toml $APP_HOME/pyproject.toml

# Встановимо Poetry
RUN pip install poetry

#Встановлення PyPDF2, docx2txt, python-pptx
RUN pip install PyPDF2
RUN pip install docx2txt
RUN pip install python-pptx

# Встановлення залежностей через Poetry
RUN poetry config virtualenvs.create false && poetry install --only main

# Скопіюємо інші файли до робочої директорії контейнера
COPY . .

# Позначимо порт де працює програма всередині контейнера
EXPOSE 8000

# Запустимо нашу програму всередині контейнера
CMD ["python", "DocChat/manage.py", "runserver", "0.0.0.0:8000"]