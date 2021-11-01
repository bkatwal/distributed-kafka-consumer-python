## Dockerfile should be used only if the application need to be deployed outside of ray head node

FROM python:3.8.5-slim

### common steps start

# username
ARG APP_USER=app

# Create user to run the application
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

# create application working directory
WORKDIR /var/www-api
RUN chown -R app:app . /usr/local;
RUN mkdir -p .tmp .log;
RUN chown -R app:app .tmp
RUN chown -R app:app .log
### common steps end

# switch to app user
USER ${APP_USER}:${APP_USER}

# bundle app source
COPY --chown=app requirements.txt .
COPY --chown=app ./src ./src
COPY --chown=app ./config ./config
COPY --chown=app setup.cfg .
COPY --chown=app setup.py .
COPY --chown=app README.md .
ARG BUILD_TIME=abc

# install dependency requirements
RUN pip install -r requirements.txt

RUN pip install -e .

# set application environment
ENV APP_ENV="production"

# expose applicable server port
EXPOSE 8002

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8002", "src.event_consumer_app:app"]
