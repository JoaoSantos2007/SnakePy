import pygame #importa a biblioteca Pygame
import random #importa a biblioteca Random

pygame.init()

cor_fundo = (150,255,159)#Define a cor do fundo

cor_cobra = (255,0,0)#Define a cor da cobra

cor_comida = (128,60,60)#Define a cor da comida

cor_pontos =(0,0,0)#Define a cor dos pontos

dimensoes = (600, 600)

#Valores Iniciais

tempo = 7.5

x = 300
y = 300

d = 20

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 -d)/20)*20
y_comida = round(random.randrange(0, 600 -d)/20)*20

fonte = pygame.font.SysFont("hack", 35) 

lista_cobra = [[x,y]]

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption("Snake")

tela.fill(cor_fundo)

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
    tela.fill(cor_fundo)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, cor_cobra, [unidade[0],unidade[1],d,d])

def mover_cobra(dx, dy, lista_cobra):
    delta_x = 0
    delta_y = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    # x = x + delta_x
    # y = y + delta_y


    return dx, dy, lista_cobra

def verifica_comida(dx,dy,x_comida,y_comida,lista_cobra,tempo):

    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        tempo = tempo + 0.5
        x_comida = round(random.randrange(0, 600 -d)/20)*20
        y_comida = round(random.randrange(0, 600 -d)/20)*20

    pygame.draw.rect(tela, cor_comida, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra, tempo

def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        raise Exception

def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()

    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception

def atualizar_pontos(lista_cobra):
    pontos = str(len(lista_cobra))
    score = fonte.render("Scores: " + pontos, True, cor_pontos)
    tela.blit(score, [0, 0])

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra, tempo = verifica_comida(dx,dy,x_comida,y_comida,lista_cobra,tempo)
    print(lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)
    clock.tick(tempo)
