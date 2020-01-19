FROM python:3.7.3-stretch

ADD ./Pipfile ./Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY ./ ./pdf-parser
WORKDIR /pdf-parser

ENV PYTHONPATH "${PYTONPATH}:pdf-parser/"

CMD ["python", "pdf_parser/panage.py", "runserver", "0.0.0.0:8080"]