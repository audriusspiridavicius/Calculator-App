from OperationInterface import OperationInterface
from OperationType import OperationType


class Calculator:
    def __init__(self, calculatoroperations):
        self.operations:list[OperationInterface] = calculatoroperations

    def Operation(self, operationtype: OperationType, number1, number2):

        op = [operation for operation in self.operations if operation.name == operationtype]

        if op:
            return op[0].get_result((number1,number2))
        return 0