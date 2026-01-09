i=12
sum_e=0
sum_o=0
while(i<=37):
    if(i%2==0):
        sum_e+=i

    else:
        sum_o+=i
    i+=1

print("sum of even natural number is :", sum_e)
print("sum of odd natural number is :", sum_o)