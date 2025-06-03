# #Um dicionário é uma estrutura de dados que armazena pares chaves-valor. É muito útil qaundo queremos associar uma informação (valor) a uma etiqueta única (chave).

# aluno={'nome':"joão", 'idade': 20,'curso':'ADS'}
# print(f'O nome do aluno é {aluno['nome']}')
# print(f'A idade do aluno é {aluno['idade']}')
# print(f'O curso do aluno é {aluno[f'curso']}')

# # a sintaxe para criar um dicionario é (d={'chave':'valor'})

#====================================================

# #pode se criar dicionarios de 3 formas, veja abaixo:
# d1={"a":1,'b':2}
# d2=dict(c=3,d=4)
# d3=dict([('e',5),('f',6)])
# print(d1,d2,d3)

#====================================================

#para acesar elementos de um dicionario, basta usar a sintaxe:
# dados={'nome': 'ana', 'idade':25}
# print(dados['idade'])
# print(dados.get('nome'))
# print(dados.get('peso',0)) #retorna 0 se a chave nã existir

#====================================================

# # adicionando e removendo valores
# dados1={}#cria dicionario vazio
# print(dados1)
# dados1['nome']='ana'
# print(dados1)
# dados1['idade']=22
# print(dados1)
# dados1['idade']=23 #modifica o valor de 22 para 23
# print(dados1)

#====================================================

# # para remover itens do dicionario
# dados={'nome':'ana','idade':22}
# print(dados)
# del dados['idade'] #remove pela chave
# print(dados)
# nome=dados.pop('nome')
# print(dados, nome)# Remove e retorna o valor (teste a diferença com print(dados))

#====================================================

# #verifiand a existencia de chaves

# info={'curso':'python'}
# print('curso' in info) #retorna True
# print('nome' in info) #retorna False

#====================================================

# #inteirando sobre dicionários
# carro={'marca':'ford','modelo':'ka','ano':2020}
# for chave in carro:
#     print(chave, carro[chave],end=" ")

# for chave, valor in carro.items(): #dar preferncia para essa forma
#     print(chave, valor)

#====================================================

# #dict.keys()	Retorna todas as chaves
# #dict.values()	Retorna todos os valores
# #dict.items()	Retorna pares (chave, valor)
# #dict.update()	Atualiza o dicionário com outro
# #dict.clear()	Remove todos os itens
# #dict.copy()	Retorna uma cópia rasa (shallow copy)
# pessoa = {"nome": "João", "idade": 30}
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# pessoa.update({"idade": 31, "cidade": "SP"})
# print(pessoa)

# nova = pessoa.copy()
# nova["nome"] = "Pedro"
# print(pessoa, nova)

#====================================================

# # dicionarios aninhados (nested dicts)
# usuarios = {
#     "user1": {"nome": "Ana", "idade": 28},
#     "user2": {"nome": "Paulo", "idade": 32}
# }

# print(usuarios["user1"]["nome"])  # Ana

#====================================================

# # compreensão de dicionarios (dic comprehension)
# quadrados = {x: x**2 for x in range(5)}
# print(quadrados)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#====================================================

# #conversã de outros tipos para dicionarios
# lista = [("a", 1), ("b", 2)]
# d = dict(lista)
# print(d)

# # De dois listas
# chaves = ["nome", "idade"]
# valores = ["Carlos", 20]
# d2 = dict(zip(chaves, valores))
# print(d2)

#====================================================

# #Uso de defaultdict (do módulo collections)
# from collections import defaultdict

# d = defaultdict(int)
# d["chave1"] += 1  # Inicializa automaticamente com 0
# print(d)

#====================================================

#Uso de Counter (frequência de elementos)
from collections import Counter

frase = "banana"
contagem = Counter(frase)
print(contagem)  # {'a': 3, 'b': 1, 'n': 2}

#====================================================

#Ordenação de Dicionários
d = {"c": 3, "a": 1, "b": 2}
ordenado = dict(sorted(d.items()))
print(ordenado)

#====================================================

#Dicionário como Estrutura de Dados (Casos práticos)
texto = "python é fácil e python é poderoso"
palavras = texto.split()
frequencia = {}

for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print(frequencia)

#====================================================

# Boas Práticas com Dicionários
# Use chaves imutáveis (strings, números, tuplas).

# Prefira get() para evitar KeyError.

# Quando possível, use defaultdict para contagens.

# Use items() para percorrer pares chave-valor eficientemente.


