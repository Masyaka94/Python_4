# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

result=''

help_1 = open("Python4.2.1.txt", "r")
str1 = help_1.read()
help_1.close()

help_2 = open("Python4.2.2.txt", "r")
str2 = help_2.read()
help_2.close()

mnogochlen1 = str1.split('+')
mnogochlen2 = str2.split('+')

koef_mnogochlen1 = []
koef_mnogochlen2 = []
some_result = ''

for i in range(0,len(mnogochlen1)):
    for x in mnogochlen1[i]:
       if x.isdigit():
        some_result+=x
       else:
        break
    if some_result=='':
        koef_mnogochlen1.append(0)    
    else:
        koef_mnogochlen1.append(some_result)
    some_result=''

print(mnogochlen1)
print(koef_mnogochlen1)

for i in range(0,len(mnogochlen2)):
    for x in mnogochlen2[i]:
       if x.isdigit():
        some_result+=x
       else:
        break
    if some_result=='':
        koef_mnogochlen2.append(0)    
    else:
        koef_mnogochlen2.append(some_result)
    some_result=''

print(mnogochlen2)
print(koef_mnogochlen2)
res_koef = []

for i in range(0,len(koef_mnogochlen1)):
    res_koef.append(int(koef_mnogochlen1[i])+int(koef_mnogochlen2[i]))
print(res_koef)

for i in range(0,len(res_koef)-1):
    if i != len(res_koef)-1:
        result+=(f'{str(res_koef[i])}x^{len(res_koef)-i-1}+')
    elif i == len(res_koef)-1:
        result+= (f'{str(res_koef[i])}x+')
result+=(f'{res_koef[-1]}=0')
print(result)

file = open("Python4.2_res.txt", "w")
file.write(result)
file.close()