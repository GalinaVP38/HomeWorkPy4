# Вычислить число Пи c заданной точностью d Пример: при d = 0.001, π = 3.141;
# при d = 0.1, π = 3.1; при d = 0.00001, π = 3.14154; d от 0.1 до 0.0000000001
from math import pi
myPi = 0
myPi_d = 0
mathPi = 0
N = 50000
i = 1
while i<N:
    myPi = myPi +(4/i)-(4/(i+2))    # через ряд Лейбница
    i=i+4
print(myPi)
mathPi = pi
# myPi_d = format(myPi, '0.1f')
# myPi_d = format(myPi, '0.2f')
# myPi_d = format(myPi, '0.3f')
myPi_d = format(myPi, '0.10f')
print(myPi_d)
print(mathPi)
