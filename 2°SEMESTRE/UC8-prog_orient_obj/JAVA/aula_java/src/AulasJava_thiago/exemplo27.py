#criar dicionario
brinquedo ={
    'marca':'estrela',
    'modelo':'boneca',
    'preco':150
}
print(brinquedo['preco'])
# quando eu criar uma função que não sei a quantidade de parametros que ira receber usar *args
def my_func(param1, *args):
    print(param1)
    for item in args:
        print(item)
    print(len(args))

my_func(12,14,15,18,30,66)

