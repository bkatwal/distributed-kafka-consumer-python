import secrets
import time

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.requests import Request
from starlette.responses import JSONResponse

from src import USERNAME, PASSWORD
from src.exceptions.usi_exceptions import BadInput, GenericException
from src.kafka_core.consumer_manager import ConsumerWorkerManager
from src.utility import logging_util

logger = logging_util.get_logger(__name__)

app = FastAPI(title="Universal Search Event Consumer")
security = HTTPBasic()
cwm = ConsumerWorkerManager()


def authorize(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.on_event("startup")
def on_startup():
    cwm.start_all_workers()


@app.on_event("shutdown")
def on_shutdown():
    cwm.start_all_workers()


@app.post('/event-consumer/knockknock', include_in_schema=False)
def health():
    return {'message': 'Who\'s there?'}


@app.post('/event-consumer/start-consumers', dependencies=[Depends(authorize)])
def start_consumers():
    cwm.start_all_workers()
    return "Successfully started all workers!"


@app.get('/event-consumers', dependencies=[Depends(authorize)])
def start_consumers():
    return cwm.get_all_running_consumer()


@app.post('/event-consumer/read-from-timestamp', dependencies=[Depends(authorize)])
def read_from_timestamp(consumer_name: str, start_timestamp: int,
                        end_timestamp: int = int(time.time() * 1000),
                        stop_running_consumer: bool = True):
    cwm.start_worker_with_timestamp(start_timestamp=start_timestamp, end_timestamp=end_timestamp,
                                    stop_regular=stop_running_consumer, name=consumer_name)
    return "Successfully started!"


@app.post('/event-consumer/start-consumer/{consumer_name}', dependencies=[Depends(authorize)])
def start_consumer(consumer_name):
    cwm.start_worker(consumer_name)
    return "Successfully started worker!"


@app.post('/event-consumer/stop-consumers', dependencies=[Depends(authorize)])
def stop_consumers():
    cwm.stop_all_workers()
    return "Successfully Stopped all workers!"


@app.post('/event-consumer/stop-consumer/{consumer_name}', dependencies=[Depends(authorize)])
def stop_consumer(consumer_name):
    cwm.stop_worker(consumer_name)
    return "Successfully Stopped!"


@app.exception_handler(Exception)
def generic_exception_handler(request: Request, exc: Exception):
    logger.error(exc)
    return JSONResponse(
        status_code=500,
        content={"message": "Oops! I messed up!"},
    )


@app.exception_handler(GenericException)
def request_validation_exception_handler(request: Request, exc: GenericException):
    logger.error(exc)
    return JSONResponse(
        status_code=500,
        content={"message": exc.message},
    )


@app.exception_handler(BadInput)
def request_validation_exception_handler(request: Request, exc: BadInput):
    logger.error(exc)
    return JSONResponse(
        status_code=422,
        content={"message": exc.message},
    )
