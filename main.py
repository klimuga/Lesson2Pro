StrToSum =''

while StrToSum.isdigit() != True:
    StrToSum = str(input('input number: '))

i=0
SumStr=0
while i in range(0, len(StrToSum)):
    SumStr += int(StrToSum[i])
    i+=1
print('сумма цифр числа', StrToSum, '-', SumStr)

i=0
MultStr=1
while i in range(0, len(StrToSum)):
    MultStr *= int(StrToSum[i])
    i+=1
print('произведение цифр числа', StrToSum, '-', MultStr)

i=0
Is5= False
while i in range(0, len(StrToSum)):
    if(int(StrToSum[i])==5):
        Is5 = True
    i+=1
if(Is5==True):
    print('Цифра 5 есть в числе')
else:
    print('Цифры 5 нет в числе')

i=0
MaxDigit= 0
while i in range(0, len(StrToSum)):
    if(int(StrToSum[i])>MaxDigit):
        MaxDigit = int(StrToSum[i])
    i+=1
print('цифра -',MaxDigit, "максимальная в числе", StrToSum)

i=0
Count5= 0
while i in range(0, len(StrToSum)):
    if(int(StrToSum[i])==5):
        Count5+=1
    i+=1
print('В числе',Count5, "пятерок")
