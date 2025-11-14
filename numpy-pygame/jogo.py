import pygame as pg
import numpy as np # se quiser, pode trocar por numpy depois

# ETAPA 1: inicialização básica
pg.init()

LARGURA = 800
ALTURA = 600
tela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption("Desvie dos Blocos!")

# Controle de FPS
clock = pg.time.Clock()

# Cores
PRETO   = (0, 0, 0)
BRANCO  = (255, 255, 255)
VERDE   = (0, 255, 0)
VERMELHO = (255, 0, 0)

# ETAPA 2: jogador (um quadrado)
larg_jogador = 50
alt_jogador = 50
x_jogador = LARGURA // 2 - larg_jogador // 2
y_jogador = ALTURA - alt_jogador - 10
vel_jogador = 7

# ETAPA 4: inimigo (bloco que cai)
larg_inimigo = 50
alt_inimigo = 50
x_inimigo = np.random.randint(0, LARGURA - larg_inimigo)
y_inimigo = -alt_inimigo  # começa fora da tela
vel_inimigo = 5

# ETAPA 6: pontuação
pontuacao = 0
fonte = pg.font.SysFont("arial", 24)

rodando = True
game_over = False

while rodando:
    clock.tick(60)  # 60 FPS

    # ETAPA 1: eventos básicos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

        # Reiniciar o jogo se estiver em game over e apertar espaço
        if game_over and evento.type == pg.KEYDOWN:
            if evento.key == pg.K_SPACE:
                # reset simples
                game_over = False
                pontuacao = 0
                x_jogador = LARGURA // 2 - larg_jogador // 2
                y_jogador = ALTURA - alt_jogador - 10
                x_inimigo = np.random.randint(0, LARGURA - larg_inimigo)
                y_inimigo = -alt_inimigo

    # Lógica só roda se NÃO estiver em Game Over
    if not game_over:
        # ETAPA 3: movimentação do jogador
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT] or teclas[pg.K_a]:
            x_jogador -= vel_jogador
        if teclas[pg.K_RIGHT] or teclas[pg.K_d]:
            x_jogador += vel_jogador

        # Impedir que saia da tela
        if x_jogador < 0:
            x_jogador = 0
        if x_jogador > LARGURA - larg_jogador:
            x_jogador = LARGURA - larg_jogador

        # ETAPA 4: movimento do inimigo
        y_inimigo += vel_inimigo

        # Quando o inimigo sai da tela, volta lá em cima em posição aleatória
        if y_inimigo > ALTURA:
            y_inimigo = -alt_inimigo
            x_inimigo = np.random.randint(0, LARGURA - larg_inimigo)
            pontuacao += 1  # desviou de um bloco → ganha ponto

        # ETAPA 5: colisão
        rect_jogador = pg.Rect(x_jogador, y_jogador,
                                   larg_jogador, alt_jogador)
        rect_inimigo = pg.Rect(x_inimigo, y_inimigo,
                                   larg_inimigo, alt_inimigo)

        if rect_jogador.colliderect(rect_inimigo):
            game_over = True

    # ETAPA 2/4/6: desenho na tela
    tela.fill(PRETO)

    # Desenhar jogador
    pg.draw.rect(tela, VERDE,
                     (x_jogador, y_jogador, larg_jogador, alt_jogador))

    # Desenhar inimigo
    pg.draw.rect(tela, VERMELHO,
                     (x_inimigo, y_inimigo, larg_inimigo, alt_inimigo))

    # Mostrar pontuação
    texto_pontos = fonte.render(f"Pontuação: {pontuacao}",
                                True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    # Tela de Game Over
    if game_over:
        texto_go = fonte.render("GAME OVER! Aperte ESPAÇO para reiniciar.",
                                True, BRANCO)
        tela.blit(texto_go, (100, ALTURA // 2))

    pg.display.update()

pg.quit()
