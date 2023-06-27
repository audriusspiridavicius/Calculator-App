from OperationInterface import OperationInterface
from OperationType import OperationType


class SumOperation(OperationInterface):

    def __init__(self):
        super().__init__()
        self.name = OperationType.PLUS

    def get_result(self, numbers):
        return sum(numbers)


class MinusOperation(OperationInterface):

    def __init__(self,):
        super().__init__()
        self.name = OperationType.MINUS

    def get_result(self, numbers):
        return numbers[0] - numbers[1]


class DivideOperation(OperationInterface):

    def __init__(self):
        super().__init__()
        self.name = OperationType.DIVIDE

    def get_result(self, numbers):
        return numbers[0] / numbers[1]


class MultiplyOperation(OperationInterface):
    def __init__(self):
        super().__init__()
        self.name = OperationType.MULTIPLY

    def get_result(self, numbers):
        return numbers[0] * numbers[1]