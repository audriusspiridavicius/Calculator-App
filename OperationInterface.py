from OperationType import OperationType


class OperationInterface:
    def __init__(self):
        self.name: OperationType = OperationType.PLUS

    def get_result(self, numbers):
        pass
