import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Jogo Legal de Forca')

branco = (255,255,255)
azul = (0,100,200)

executando = True

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.quit:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False

    tela.fill(azul)
    pygame.display.flip()

pygame.quit()
sys.exit()
