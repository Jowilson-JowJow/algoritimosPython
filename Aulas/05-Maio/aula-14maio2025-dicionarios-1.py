#esse exercicios esta no teams deve enviar ele para realizar a tarefa
tradutor={}
tradutor={
"pineapple":"abacaxi", "apple":"maçã", "banana":"banana", "grape":"uva", "orange":"laranja",
"lemon":"limão", "lime":"lima", "strawberry":"morango", "blueberry":"mirtilo", "watermelon":"melancia",
"peach":"pêssego", "pear":"pêra", "plum":"ameixa", "cherry":"cereja", "mango":"manga",
"papaya":"mamão", "kiwi":"kiwi", "coconut":"coco", "avocado":"abacate", "melon":"melão",
"carrot":"cenoura", "potato":"batata", "tomato":"tomate", "onion":"cebola", "garlic":"alho",
"lettuce":"alface", "spinach":"espinafre", "broccoli":"brócolis", "cauliflower":"couve-flor", "cabbage":"repolho",
"pepper":"pimentão", "cucumber":"pepino", "zucchini":"abobrinha", "pumpkin":"abóbora", "eggplant":"berinjela",
"rice":"arroz", "beans":"feijão", "bread":"pão", "butter":"manteiga", "cheese":"queijo",
"milk":"leite", "egg":"ovo", "meat":"carne", "chicken":"frango", "fish":"peixe",
"salt":"sal", "sugar":"açúcar", "oil":"óleo", "vinegar":"vinagre", "flour":"farinha",
"coffee":"café", "tea":"chá", "juice":"suco", "water":"água", "soda":"refrigerante",
"cup":"xícara", "glass":"copo", "plate":"prato", "spoon":"colher", "fork":"garfo",
"knife":"faca", "napkin":"guardanapo", "table":"mesa", "chair":"cadeira", "window":"janela",
"door":"porta", "floor":"chão", "ceiling":"teto", "wall":"parede", "roof":"telhado",
"house":"casa", "apartment":"apartamento", "room":"quarto", "kitchen":"cozinha", "bathroom":"banheiro",
"bed":"cama", "pillow":"travesseiro", "blanket":"cobertor", "closet":"guarda-roupa", "mirror":"espelho",
"television":"televisão", "radio":"rádio", "computer":"computador", "phone":"telefone", "lamp":"lâmpada",
"book":"livro", "pen":"caneta", "pencil":"lápis", "notebook":"caderno", "paper":"papel",
"school":"escola", "student":"aluno", "teacher":"professor", "classroom":"sala de aula", "lesson":"lição",
"homework":"tarefa", "test":"prova", "exam":"exame", "grade":"nota", "subject":"matéria",
"math":"matemática", "science":"ciência", "history":"história", "geography":"geografia", "language":"idioma",
"English":"inglês", "Portuguese":"português", "Spanish":"espanhol", "French":"francês", "German":"alemão",
"family":"família", "father":"pai", "mother":"mãe", "brother":"irmão", "sister":"irmã",
"grandfather":"avô", "grandmother":"avó", "uncle":"tio", "aunt":"tia", "cousin":"primo",
"son":"filho", "daughter":"filha", "baby":"bebê", "child":"criança", "friend":"amigo",
"boy":"menino", "girl":"menina", "man":"homem", "woman":"mulher", "person":"pessoa",
"people":"pessoas", "city":"cidade", "street":"rua", "car":"carro", "bus":"ônibus",
"train":"trem", "plane":"avião", "boat":"barco", "bicycle":"bicicleta", "motorcycle":"motocicleta",
"traffic":"trânsito", "light":"luz", "sun":"sol", "moon":"lua", "star":"estrela",
"sky":"céu", "cloud":"nuvem", "rain":"chuva", "snow":"neve", "wind":"vento",
"weather":"tempo", "hot":"quente", "cold":"frio", "warm":"morno", "cool":"fresco",
"happy":"feliz", "sad":"triste", "angry":"zangado", "tired":"cansado", "sick":"doente",
"hungry":"faminto", "thirsty":"sedento", "beautiful":"bonito", "ugly":"feio", "strong":"forte",
"weak":"fraco", "fast":"rápido", "slow":"devagar", "big":"grande", "small":"pequeno",
"new":"novo", "old":"velho", "good":"bom", "bad":"ruim", "easy":"fácil",
"hard":"difícil", "clean":"limpo", "dirty":"sujo", "open":"abrir", "close":"fechar"
}

while True:
    menu=input("Digite: \n1--para traduzir palavra em inglês: \n2--para adicionar palavra em inglês: \ndigite x para sair: ").lower()
    if menu=='1':
        palavra=input('Digite uma palvra em inglês: ').lower()
        if palavra in tradutor:
            print( f'A palavra digitada foi: ', palavra,'traduzindo para português: ',tradutor[palavra])
        else:
            print('Essa plavra não existe no tradutor ainda, deseja acrescenta-la digite 2')
    elif menu=='2':
        palavra_nova_in=input('Digite uma palvra nova em ingles: ').lower()
        palavra_nova_pr=input('Digite a tradução da palavra em portugues: ').lower()
        tradutor[palavra_nova_in]=palavra_nova_pr
        print( f'A palavra inserida foi: ', palavra_nova_in,'traduzindo para português: ',tradutor[palavra_nova_in])
    else: 
        menu=='x'
        break