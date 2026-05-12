#calculate compound interest.
principal =10000
rate =5
time =2
amount  =  principal * (1 + rate/100) ** time
ci =  amount - principal
print(ci)