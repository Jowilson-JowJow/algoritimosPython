#Escreva uma função que conte quantas vogais há em uma string.

def vowel_counter1(text):
    return sum(text.count(jow) for jow in 'aeiou')
   
    
typed_text=input('Type word or phrase: ')
print('The amunt of vowel in this word or phrase is ',vowel_counter1(typed_text))