#Crie uma função que inverta uma string.
def reverse_text(text):
    reverse_text=text[::-1]
    print(reverse_text)

a=input('type a text: ')
print(f'the typed text was {a} and its inverted text is', end=" ")
reverse_text(a)