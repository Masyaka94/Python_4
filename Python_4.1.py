# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#Пример: если k = 2, 
# то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


k = int(input('Введите натуральную степень: '))
koef = []
ixi = []
result = []
str_result=''
while k > -1:
    if k > 1:
        koef.append(random.randint(0,11))
        ixi.append(f'x^{k}')
    elif k == 1:
        koef.append(random.randint(0,11))
        ixi.append(f'x')
    elif k == 0:
        koef.append(random.randint(0,11))
        ixi.append('')
    k-=1
for i in range(0,len(koef)):
    if koef[i] == 1 and i<len(koef)-1:
        result.append(ixi[i])
    elif koef[i] == 0:
        continue
    result.append(str(koef[i])+(ixi[i]))
    if ixi[i] == '':
        continue
for i in range(0,len(result)):
    if i < len(result)-1:
        str_result+=str(result[i])+'+'
    elif i == len(result)-1:
        str_result+=str(result[i])+'=0'
file = open("test_Python4.1.txt", "w")
file.write(str_result)
file.close()