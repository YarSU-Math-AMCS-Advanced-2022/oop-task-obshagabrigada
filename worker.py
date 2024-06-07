from order import Order
from enum import Enum

class WorkerStatus(Enum):
    NOTWORKING = 0
    INPROGRESSWORK = 1
    FREE = 2

class Worker:
    currentWork: Order
    workerStatus: WorkerStatus
    timeStartWork: str
    timeEndWork: str
    workDuration: int

    # принять заказ, если возможно

    def __init__(self,workDuration:int):
        self.currentWork = None
        self.workerStatus = WorkerStatus.NOTWORKING
        self.workDuration = min(6,workDuration)

    def get_shift(self, timeStartWork: int = 0):
        self.workerStatus = WorkerStatus.FREE
        self.timeStartWork = timeStartWork
        self.timeEndWork = (timeStartWork + self.workDuration) % 24

    def end_shift(self):
        self.workerStatus = WorkerStatus.NOTWORKING
        print(f"получил зарплату {300 * (self.timeEndWork - self.timeStartWork)} ")
    # получить смену, когда работает
