FROM python:3.10-slim

ARG api_port
ENV UVICORN_PORT ${api_port}

ARG root_path
ENV UVICORN_ROOT_PATH ${root_path}

WORKDIR /project

COPY . /project/

RUN pip install -r requirements.txt

CMD ["uvicorn", "src.app:app", "--proxy-headers", "--host", "0.0.0.0"] 