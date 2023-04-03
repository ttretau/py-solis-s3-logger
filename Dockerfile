FROM public.ecr.aws/bitnami/python:3.10

ENV APP_MODULE=py_solis_s3_logger.cli:py_solis_s3_logger

COPY pyproject.toml README.md /app/
WORKDIR /app
RUN pip install hatch

COPY py_solis_s3_logger /app/py_solis_s3_logger

RUN hatch env prune && hatch env create production

CMD hatch run production:publisher