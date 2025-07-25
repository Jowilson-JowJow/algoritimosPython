def text_slicing():#função que vai pedir uma palavra ou frase e fazer o fatiamento dessa string
    word=input('Type a word (or hrase): ')#solicita que o usuario digite uma palara ou frase
    x=int(input('enter the start of slicing: '))#solicita o inicio do fatiamento
    y=int(input('enter the end of the slice: '))#solicita o final do fatiamento
    slicing_word=word[x:y]#faz o fatiamento da palavra ou frase digitada onde 0 x é o index de inicio e y=n-1 index de final, se digitar y=5 o fatiamento vai até o indice 4
    print(f'the word (or phrase) entered was: {word}\nshowing the slicing of the word (or phrase): {slicing_word} ')
    #a função do fatiamento sempre gera uma nova  string

def word_length():#função que vai contar o comprimento(tamanho) de uma palavra ou frase
    word=input('type a word (or phrase): ')#solicita que se digite uma palavra ou frase
    word_size=len(word)#conta o comprimento(tamanho) da palavra ou frase digitada inclui na contagem espaços
    print(f'the word (or phrase) entered was: {word}\nthe length of the word (or phrase) typed is: {word_size}')

def add_words():#função que vai somar duas palavras ou frase
    word1=input('Type the word (or phrase): ')#solicita digitar uma frase ou palavra
    word2=input('Type the word (or phrase): ')#solicta digitar uma palvra ou frase
    summed_words=word1+' '+word2#soma as duas strings e salva em outra variavel, porem não da espaço entre as palavras. então coloque um espaço na soma
    print(f'the first text typed was: {word1}\nand the second text typed was: {word2}\nputting the texts together we have: {summed_words}')

def repeat_text():#função que solicita um texto e a quanidade de vezes a ser repetido
    word=input('enter the text to repeat: ')#solicita um texto
    num_repeat=int(input('Enter the number that the text will be repeated: '))#solicita quantas vezes o texto será repetido
    print(f'the typed text was: {word}\nthis text will bw repeated {num_repeat} times\nseehow the repeated text looks\n{word*num_repeat}')#a sintaxe para repetir o texto é word*num_repeat

def text_search():#função que vai pedir parte de texto para buscar em uma frase ou palavra previamente digitada
    word=input('type a word (or phrase: )')#solicita uma frase ou palavra
    search_word=input('Enter a word (or phrase) to search for: ')#solicita um texto para se procurar no texto digitado previamente
    print(f'the word (or phrase) entered was: {word}\nthe text to search for is: {search_word}')
    answer=search_word in word#é preciso fazer o print para retorar true ou false
    print (answer)#ira retornar TRUE ou FALSE

def first_capital_close():#função para pegar a primeira letra de uma palavra e por em maiusculo
    word=input('type a word: ')#pede para digitar uma palavra
    capital_word=word.capitalize()#pega a palavra digitada e coloca a primeira letra em  maiuscula funciona para frases tambem
    print(f'the word typed was: {word}\nwith the first letter captalized is: {capital_word}')

def by_word_title():#cada palavra de uma oração inicia com maiuscula
    phrase=input('Enter the title:').lower()
    phrase_title=phrase.title()
    print(phrase_title)

def capitalized_word():#retorna palavra ou frase em maiusculas
    word=input('type a word (or phrase): ').upper()
    print(word)
    
def lowercase_word():#retorna palavra ou frase em minuscula
    word=input('type a word (or phrase): ').lower()
    print(word)

def tiny_word():#O método casefold() é usado para converter uma string em minúsculas, de forma ainda mais agressiva que o método lower(). Isso é útil principalmente em comparações entre textos, pois ele trata diferenças sutis entre caracteres maiúsculos/minúsculos em diferentes idiomas.
    word1=input('type a word: ')
    word2=input('type a new word: ')
    word1_tiny=word1.casefold()
    word2_tiny=word2.casefold()
    print(f'A 1° palavra digitada foi: "{word1}"\ne a 2° palavra digitada foi: "{word2}"\nas duas palavras são iguais?\n{word1_tiny==word2_tiny}')#o (f'texto{}') ou (F'txto{}') funciona normalmente
    
def invet_lower_upper():#inverte caractere de maiusculo para minsculo e vice-versa 
    word=input('type a word (or phrase): ')
    word1=word.swapcase()#sintaxe para inverter maiuscula em minusculo e vice-versa diz ser util para teste, me pergunto qual testes se pode realizar com essa inversão?
    print(f'a palavra (ou frase) digitada foi: "{word}"\napós inverter maiusculas em minusculas e vice-versa, temos:\n"{word1}"')

def remove_space():# serve para remover espaços ou caractere especial porem não remove no meio
    word=input('type a word (or phrase) with spaces: ')
    space_remove_word=word.strip()
    print(f'A palavra (ou frase) digitada , co espaço, foi: "{word}"\napós remover o espaço ficou: "{space_remove_word}"')
    word1=input('type a word (or phrase) with special character "*": ')
    space_remove_word1=word1.strip('*')
    print(f'A palavra (ou frase) digitada , co espaço, foi: "{word1}"\napós remover o espaço ficou: "{space_remove_word1}"')

def remove_suffix():#Remove prefixo/sufixo exato se presente; caso contrário retorna cópia idêntica. Útil p/ parsing seguro sem startswith + slicing manual.
    word=input('type a word (or phrase): ')
    sulffix_remove=input('type a sulffix or prefix to remove: ')
    new_word=word.removesuffix(sulffix_remove)#remove só o sulfixo
    print(f'A palavra ou frase digitada foi: "{word}"\nremovendo o sulfixo "{sulffix_remove}"\na nova palavra é: "{new_word}"')

def remove_prefix():#Remove prefixo/sufixo exato se presente; caso contrário retorna cópia idêntica. Útil p/ parsing seguro sem startswith + slicing manual.
    word=input('type a word (or phrase): ')
    prefix_remove=input('type a sulffix or prefix to remove: ')
    new_word=word.removeprefix(prefix_remove)#remove só o prefixo
    print(f'A palavra ou frase digitada foi: "{word}"\nremovendo o sulfixo "{prefix_remove}"\na nova palavra é: "{new_word}"')

def center_text():#Centraliza o texto dentro de um espaço de largura width, preenchendo os lados com o caractere fillchar.
    word=input('type a word: ')
    character=int(input('type how many characters you want to center: '))
    center_word=word.center(character)
    print(f'"{center_word}"')
    
def center_text_character():#Centraliza o texto dentro de um espaço de largura width, preenchendo os lados com o caractere fillchar.
    word=input('type a word: ')
    space=int(input('type how many characters you want to center: '))
    character=input('type a character to searate and interleave: ')
    center_word=word.center(space,character)
    print(f'"{center_word}"')

def align_left():#função alinha palavra ou frase a direita com ou sem caractere especial
    word=input('type a word (or phrase): ')
    space=int(input('enter thedesired width: '))
    character=input('type the desired character: ')
    if character=='':
        word_left=word.ljust(space)
        print(word_left)
    else:
        word_left=word.ljust(space,character)
        print(word_left)

def align_right():#função alinha a palavra ou texto a esquerda com ou sem caractere especial
    word=input('Type a word (or phrase):')
    space=int(input('enter the desired width: '))
    character=input('type the desired character: ')
    if character=='':
        word_right=word.rjust(space)
        print(word_right)
    else:
        word_right=word.rjust(space,character)
        print(word_right)

def word_zero():#função preecnhe com zeros, respeitando sinais
    word=input('type a word (or phrase): ')
    width=int(input('how many zeros will be filled:  '))#para que o zfill prencha com zeros a esquerda o valor para width tem que ser maior que o input em word
    zero_word=word.zfill(width)
    print(f'o texto digitado foi: "{word}"\ne foi solicitado acrescentar "{width}" zeros a esquerda\no texto ficou assim "{zero_word}"')

def count_word():
    word=input('Type a word (or phrase): ')
    character=input('Enter the character to be counted: ')
    word_size=word.count(character)
    print(word_size)




