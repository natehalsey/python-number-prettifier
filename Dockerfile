FROM python:3.10-slim as base

WORKDIR /var/task/
ENV PYTHONPATH "${PYTHONPATH}:/var/task"

RUN python -m pip install --upgrade pip

COPY src ./
COPY requirements.txt ./
COPY setup.py ./

RUN pip install pip-tools
RUN pip-sync requirements.txt

RUN python setup.py install

FROM base as app

ENTRYPOINT [ "python", "main.py" ]

FROM base as test

ENTRYPOINT [ "pytest", "." ]