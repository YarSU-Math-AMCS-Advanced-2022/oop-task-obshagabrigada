from worker import Worker, WorkerStatus
from order import Order,Status

class Cooker(Worker):

    def give_order(self, order: Order):
        self.workerStatus = WorkerStatus.INPROGRESSWORK
        self.currentWork = order

    def order_assembly(self):
        print(f'Работает над заказом ID: {self.currentWork.orderId}')
        self.package()
        

    def package(self):
        self.currentWork.status = Status.INSTOCK
        self.currentWork = None
        print("Приготовил заказ")
        self.workerStatus = WorkerStatus.FREE
        
