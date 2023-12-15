import pygame  # importa a biblioteca Pygame
import random  # importa a biblioteca Random
import os
from audioplayer import AudioPlayer

inicio = False
absolutePath = os.path.dirname(__file__)
assetsPath = absolutePath + "/assets"

# Começar partida
def iniciar(inicio, tela, fonte, texto):
    texto = fonte.render("Pressione T para iniciar: ", True, cor_pontos)
    tela.blit(imagem, [0, 263])
    tela.blit(texto, [150, 150])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                inicio = True
        if event.type == pygame.QUIT:
            raise Exception
    return inicio


while True:
    status = True
    pygame.init()
    player = AudioPlayer(assetsPath + "/music.mp3")
    comer = AudioPlayer(assetsPath + "/eat.mp3")
    erro = AudioPlayer(assetsPath + "/error.mp3")

    player.play()

    # Definir cores
    cor_inicio = (64, 193, 255)
    cor_fundo = (150, 255, 159)
    cor_cobra = (255, 0, 0)
    cor_comida = (138, 0, 0)
    cor_pontos = (0, 0, 0)
    cor_inicio = (64, 193, 255)
    cor_fim = (255, 255, 110)

    dimensoes = (600, 600)
    fim = ""

    # Valores Iniciais
    pontuação = ""
    texto = ""
    tempo = 11

    direcao_x = "Liberado"
    direcao_y = "Liberado"

    x = 300
    y = 300

    d = 20

    dx = 0
    dy = 0

    x_comida = round(random.randrange(0, 600 - d)/20)*20
    y_comida = round(random.randrange(0, 600 - d)/20)*20

    fonte = pygame.font.SysFont("hack", 35)
    fonte2 = pygame.font.SysFont("hack", 100)

    lista_cobra = [[x, y]]

    tela = pygame.display.set_mode((dimensoes))
    pygame.display.set_caption("Snake")
    tela.fill(cor_inicio)

    imagem = pygame.image.load(assetsPath + "/snake.png")
    estatico = imagem.get_rect()

    clock = pygame.time.Clock()
    if inicio == False:
        while inicio == False:
            pygame.display.update()
            inicio = iniciar(inicio, tela, fonte, texto)

    def desenha_cobra(lista_cobra):
        tela.fill(cor_fundo)
        for unidade in lista_cobra:
            pygame.draw.rect(tela, cor_cobra, [unidade[0], unidade[1], d, d])

    tela.fill(cor_fundo)

    def mover_cobra(dx, dy, lista_cobra, direcao_x, direcao_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise Exception
            if event.type == pygame.KEYDOWN:
                if direcao_x == "Liberado":
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        dx = -d
                        dy = 0
                        direcao_x = "Ocupado"
                        direcao_y = "Liberado"
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        dx = d
                        dy = 0
                        direcao_x = "Ocupado"
                        direcao_y = "Liberado"
                if direcao_y == "Liberado":
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        dx = 0
                        dy = -d
                        direcao_y = "Ocupado"
                        direcao_x = "Liberado"
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        dx = 0
                        dy = d
                        direcao_y = "Ocupado"
                        direcao_x = "Liberado"
                if event.key == pygame.K_ESCAPE:
                    raise Exception

        x_novo = lista_cobra[-1][0] + dx
        y_novo = lista_cobra[-1][1] + dy

        lista_cobra.append([x_novo, y_novo])

        del lista_cobra[0]

        return dx, dy, lista_cobra, direcao_x, direcao_y

    def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra, tempo):
        head = lista_cobra[-1]

        x_novo = head[0] + dx
        y_novo = head[1] + dy

        if head[0] == x_comida and head[1] == y_comida:
            comer.play()
            lista_cobra.append([x_novo, y_novo])
            tempo = tempo + 0.5
            x_comida = round(random.randrange(0, 600 - d)/20)*20
            y_comida = round(random.randrange(0, 600 - d)/20)*20

        pygame.draw.rect(tela, cor_comida, [x_comida, y_comida, d, d])

        return x_comida, y_comida, lista_cobra, tempo

    def verifica_parede(lista_cobra, status):
        head = lista_cobra[-1]
        x = head[0]
        y = head[1]

        if x not in range(600) or y not in range(600):
            status = False
        return status

    def verifica_mordeu_cobra(lista_cobra, status):
        head = lista_cobra[-1]
        corpo = lista_cobra.copy()

        del corpo[-1]
        for x, y in corpo:
            if x == head[0] and y == head[1]:
                status = False
        return status

    def atualizar_pontos(lista_cobra):
        pontos = str(len(lista_cobra))
        score = fonte.render("Scores: " + pontos, True, cor_pontos)
        tela.blit(score, [0, 0])
        return pontos

    while status == True:
        pygame.display.update()
        desenha_cobra(lista_cobra)
        dx, dy, lista_cobra, direcao_x, direcao_y = mover_cobra(
            dx, dy, lista_cobra, direcao_x, direcao_y)
        x_comida, y_comida, lista_cobra, tempo = verifica_comida(
            dx, dy, x_comida, y_comida, lista_cobra, tempo)
        status = verifica_parede(lista_cobra, status)
        status = verifica_mordeu_cobra(lista_cobra, status)
        pontuação = atualizar_pontos(lista_cobra)
        clock.tick(tempo)
    erro.play()
    pygame.display.update()
    tela.fill(cor_fim)
    fim = fonte2.render("Gamer Over: ", True, cor_pontos)
    tela.blit(fim, [100, 50])
    pontuação = fonte2.render("Pontos: " + pontuação, True, cor_pontos)
    tela.blit(pontuação, [100, 200])
    pygame.display.update()
    clock.tick(0.3)
