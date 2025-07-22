# #crie a tabuada do 1 até a do 10
# for x in range(0,11):
#     for y in range(0,11):
#         z=x*y
#         print(x,'x',y,'=',z)
#     print('-'*10)


x=int(input('Digite o numero que se quer a tabuada: '))
for i in range(11):
    print(f'{x}*{i}={x*i}')
