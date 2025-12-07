import random 
import os 

PALAVRAS = ['casa', 'amor', 'tempo', 'pessoa', 'dia', 'vida', 'mundo', 'trabalho', 'filho', 'cidade', 'olho', 'mae', 'pai', 'coisa', 'governo', 'empresa', 'falar', 'denominacao', 'poder', 'estar', 'ter', 'ir', 'ver', 'querer', 'saber', 'pensar', 'achar', 'sentir', 'voce', 'nos', 'eles', 'outro', 'grande', 'pequeno', 'bom', 'novo', 'velho', 'certo', 'alto', 'baixo', 'rapido', 'devagar', 'agora', 'sempre', 'nunca', 'muito', 'pouco', 'aqui', 'la', 'perto', 'longe', 'porque', 'como', 'quando', 'onde', 'quem', 'qual', 'historia', 'arte', 'ciencia', 'escola', 'livro', 'numero', 'ponto', 'linha', 'circulo', 'cor', 'branco', 'preto', 'azul', 'verde', 'vermelho', 'amarelo', 'mesa', 'cadeira', 'porta', 'janela', 'rua', 'carro', 'trem', 'aviao', 'barco', 'comida', 'beber', 'dormir', 'acordar', 'comecar', 'terminar', 'ajudar', 'receber', 'dar', 'abrir', 'fechar', 'esperar', 'levar', 'mudar', 'acabar', 'preciso', 'apenas', 'depois','irmao', 'irma', 'primo', 'prima', 'amigo', 'amiga', 'tio', 'tia', 'avo', 'familia', 'crianca', 'jovem', 'adulto', 'homem', 'mulher', 'animal', 'cachorro', 'gato', 'passaro', 'peixe', 'floresta', 'rio', 'mar', 'montanha', 'pedra', 'areia', 'sol', 'lua', 'ceu', 'nuvem', 'chuva', 'vento', 'fogo', 'agua', 'terra', 'ar', 'flor', 'fruta', 'legume', 'pao', 'leite', 'queijo', 'carne', 'doce', 'sal', 'acucar', 'roupa', 'sapato', 'camisa', 'calca', 'vestido', 'relogio', 'anel', 'pulseira', 'ouro', 'prata', 'moeda', 'papel', 'caneta', 'lapis', 'telefone', 'computador', 'televisao', 'radio', 'musica', 'filme', 'jogo', 'esporte', 'saude', 'doenca', 'medico', 'hospital', 'farmacia', 'dinheiro', 'banco', 'mercado', 'loja', 'fabrica', 'escritorio', 'apartamento', 'hotel', 'praia', 'campo', 'estrada', 'ponte', 'viagem', 'passaporte', 'mala', 'chave', 'bandeira', 'regiao', 'estado', 'distrito', 'bairro', 'esquina', 'semaforo', 'placa', 'poste', 'luz', 'sombra', 'espelho', 'parede', 'teto', 'chao', 'escada', 'cozinha', 'quarto', 'sala', 'banheiro', 'jardim', 'telhado', 'cimento', 'ferro', 'madeira', 'plastico', 'vidro', 'tecido', 'metal', 'borracha', 'pneu', 'roda', 'motor', 'combustivel', 'oleo', 'gasolina', 'alcool', 'freio', 'volante', 'velocidade', 'pista', 'neve', 'gelo', 'calor', 'frio', 'calma', 'paz', 'guerra', 'alegria', 'tristeza', 'raiva', 'medo', 'esperanca', 'fe', 'justica', 'lei', 'policia', 'prisao', 'crime', 'inocente', 'culpado', 'testemunha', 'juiz', 'advogado', 'tribunal', 'processo', 'documento', 'registro', 'identidade', 'eleicao', 'politica', 'votacao', 'debate', 'partido', 'presidente', 'ministro', 'deputado', 'senador', 'vereador', 'prefeito', 'governador', 'secretario', 'funcionario', 'servico', 'qualidade', 'cliente', 'fornecedor', 'venda', 'compra', 'estoque', 'lucro', 'prejuizo', 'investimento', 'risco', 'planejamento', 'estrategia', 'objetivo', 'meta', 'resultado', 'sucesso', 'fracasso', 'desafio', 'oportunidade', 'tendencia', 'inovacao', 'tecnologia', 'software', 'hardware', 'rede', 'internet', 'site', 'email', 'senha', 'usuario', 'conta', 'aplicativo', 'noticia', 'jornal', 'revista', 'reporter', 'entrevista', 'camera', 'foto', 'video', 'gravacao', 'podcast', 'transmissao', 'comunicacao', 'dialogo', 'discussao', 'argumento', 'conclusao', 'resumo', 'detalhe', 'exemplo', 'conceito', 'definicao', 'hipotese', 'teoria', 'pesquisa', 'analise', 'sintese', 'metodo', 'padrao', 'variacao', 'estatistica', 'probabilidade', 'matematica', 'geometria', 'fisica', 'quimica', 'biologia', 'geografia', 'sociologia', 'filosofia', 'psicologia', 'economia', 'direito', 'engenharia', 'arquitetura', 'medicina', 'enfermagem', 'nutricao', 'educacao', 'administracao', 'marketing', 'financas', 'contabilidade', 'recurso', 'humano', 'logistica', 'producao', 'manutencao', 'seguranca', 'higiene', 'limpeza', 'ordem', 'bagunca', 'rotina', 'habito', 'costume', 'tradicao', 'cultura', 'idioma', 'lingua', 'alfabeto', 'silaba', 'frase', 'texto', 'paragrafo', 'capitulo', 'biblioteca', 'museu', 'galeria', 'exposicao', 'evento', 'festa', 'reuniao', 'congresso', 'simposio', 'palestra', 'curso', 'treinamento', 'aprendizado', 'ensino', 'professor', 'aluno', 'colegio', 'universidade', 'doutorado', 'mestrado', 'graduacao', 'diploma']

FORCA_DESENHO=[
    """
        ____
        |   |
        |
        |
        |
        |
      __|__
    """,
     """
        ____
        |   |
        |   o
        |
        |
        |
      __|__
    """,
       """
        ____
        |   |
        |   o
        |   |
        |
        |
      __|__
    """,
         """
        ____
        |   |
        |   o
        |  /|
        |
        |
      __|__
    """,
            """
        ____
        |   |
        |   o
        |  /|\\
        |
        |
      __|__
    """,
             """
        ____
        |   |
        |   o
        |  /|\\
        |  /
        |
      __|__
    """,
              """
        ____
        |   |
        |   o
        |  /|\\
        |  / \\
        |
      __|__
    """,
]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def escolher_palavra():
    return random.choice(PALAVRAS).upper()

def mostrar_status(palavra, letra_certas, letras_erradas, tentativas):
    limpar_tela()
    print(FORCA_DESENHO[len(letras_erradas)])
    print()

    palavra_display = ''
    for letra in palavra:
        if letra in letra_certas:
            palavra_display += letra + ' '
        else:
            palavra_display+='_ '
    print('Palavra:', palavra_display,'\n')

    if letras_erradas:
        print('Letras Erradas:', ', '.join(sorted(letras_erradas)))

    print(f'Tentativas Restantes: {tentativas - len(letras_erradas)}')
    print()

def pedir_letra(letras_usadas):
    while True:
        letra = input('Digite uma letra: ').upper().strip()

        if len(letra)!=1:
            print('Digite apenas letra!!!')
            continue
        if not letra.isalpha():
            print('Digite apenas letra!!!')
            continue
        if letra in letras_usadas:
            print("Você ja tentou essa letra!!!")
            continue
        return letra

def jogar():
    print('='*50)
    print(' '*18+ 'Jogo da Forca')
    print('='*50)
    print('\nPressione ENTER para começar...')
    
    palavra = escolher_palavra()
    letras_certas = set()
    letras_erradas = set()
    tentativas_max = 6

    while True:
        mostrar_status(palavra, letras_certas, letras_erradas, tentativas_max)
        if all(letra in letras_certas for letra in palavra):
            print('='*50)
            print(' '*14+ 'Parabéns, você ganhou!')
            print(f"{' '*14}'A palavra é:' {palavra}'")
            print('='*50)
            break

        if(len(letras_erradas)>= tentativas_max):
            print('='*50)
            print(' '*17+ 'wasted - PERDEU')
            print(f"{' '*14}'A palavra é:' {palavra}'")
            print('='*50)
            break


        letra = pedir_letra(letras_certas | letras_erradas)

        if letra in palavra:
            letras_certas.add(letra)
        else:
            letras_erradas.add(letra)

    jogar_novamente = input('\nDeseja Jogar Novamente? (S/N): ').upper().strip()
    if(jogar_novamente=='S'):
        jogar()
    else:
        print('\nAté a proxima, Obrigado por jogar.')
if __name__=='__main__':
    jogar()


#https://www.invertexto.com/forcacodigo
#(para ver p codigo do mauricio)

# #instale o pit install pygame
# PS C:\Users\JowilsonNunes\Documents\GitHub\algoritimosPython> pip install pygame
# Defaulting to user installation because normal site-packages is not writeable
# Collecting pygame
#   Downloading pygame-2.6.1-cp313-cp313-win_amd64.whl.metadata (13 kB)
# Downloading pygame-2.6.1-cp313-cp313-win_amd64.whl (10.6 MB)
#    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 31.9 MB/s eta 0:00:00
# Installing collected packages: pygame
# Successfully installed pygame-2.6.1

# [notice] A new release of pip is available: 24.3.1 -> 25.3
# [notice] To update, run: python.exe -m pip install --upgrade pip
# PS C:\Users\JowilsonNunes\Documents\GitHub\algoritimosPython> 

#use o site abixo para ler a documentação do pygame
#https://www.pygame.org/docs/
