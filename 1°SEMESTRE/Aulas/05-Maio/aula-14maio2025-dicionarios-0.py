# tradutor ={}
# tradutor ["pineapple"]="abacaxi"
# tradutor ["apple"]="maça"
# tradutor ["orange"]="laranja"
# print(type(tradutor))
# print(tradutor)

# tradutor1 ={}
# tradutor1 ={"pineapple":"abacaxi", "apple":"maça","orange":"laranja"}
# print(type(tradutor1))
# print(tradutor1)

# print(tradutor["apple"])
# print(tradutor1["orange"])

# del (tradutor['pineapple'])
# print(tradutor)
# print(tradutor.pop("pineapple","sem correspondencia"))
# tradutor1.clear()
# print(f'dicionario vazio',tradutor1)
# print('apple' in tradutor1)
# print('maça' in tradutor.values())
# tradutor1["orange"]="orangutango"
# print(tradutor1['orange'])


dados={'crossfox':{'km':35000,'ano':2005}, 'ds5':{'km':17000,'ano':2015}, 'fusca': {'km':130000,'ano':1979}, 'jetta': {'km':56000,'ano':2011},'passat': {'km':62000,'ano':1999}}
print(dados)
print(dados['fusca']['ano'])
print(dados.get('gol','veiculo não encontrado'))
print(dados.get('ds5','veiculo não encontrado'))