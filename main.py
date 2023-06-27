from Calculator import Calculator
from Operations import SumOperation
from Operations import *
a =(2,3)
print(type(a))



calculator = Calculator([SumOperation()])

ot = OperationType.PLUS

result = calculator.Operation(operationtype=ot, number1=10, number2=2)

print(result)
# s = SumOperation()
#
# print(f"sum operation test = {s.get_result(tuple([2,3]))}")
# print(f"sum operation type = {s.name}")

