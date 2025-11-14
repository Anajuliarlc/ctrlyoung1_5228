import pygame
import random

# Inicialização
pygame.init()

LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvie dos Blocos - Versão Difícil")

clock = pygame.time.Clock()

# Cores
PRETO    = (0, 0, 0)
BRANCO   = (255, 255, 255)
VERDE    = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Jogador
larg_jogador = 50
alt_jogador = 50
x_jogador = LARGURA // 2 - larg_jogador // 2
y_jogador = ALTURA - alt_jogador - 10
vel_jogador = 7

# Inimigos (blocos vermelhos)
larg_inimigo = 50
alt_inimigo = 50

def criar_inimigo():
    """Cria um inimigo em posição X aleatória, acima da tela."""
    x = random.randint(0, LARGURA - larg_inimigo)
    y = random.randint(-300, -alt_inimigo)  # começa fora da tela
    return [x, y]  # usamos [x, y] para poder alterar depois

inimigos = [criar_inimigo()]  # começamos com 1 inimigo

# Pontuação e fonte
pontuacao = 0
fonte = pygame.font.SysFont("arial", 24)

rodando = True
game_over = False

while rodando:
    clock.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Reinicia o jogo no Game Over ao apertar espaço
        if game_over and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                game_over = False
                pontuacao = 0
                x_jogador = LARGURA // 2 - larg_jogador // 2
                y_jogador = ALTURA - alt_jogador - 10
                inimigos = [criar_inimigo()]  # volta para 1 inimigo

    if not game_over:
        # --- Movimento do jogador ---
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            x_jogador -= vel_jogador
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            x_jogador += vel_jogador

        # Limitar o jogador à tela
        if x_jogador < 0:
            x_jogador = 0
        if x_jogador > LARGURA - larg_jogador:
            x_jogador = LARGURA - larg_jogador

        # --- Aumentar dificuldade ---
        # Velocidade dos inimigos cresce com a pontuação
        vel_inimigo = 5 + pontuacao // 5

        # Quantidade de inimigos também cresce com a pontuação
        # Ex.: 0-9 pontos -> 1 inimigo
        #     10-19 pontos -> 2 inimigos
        #     20-29 pontos -> 3 inimigos, etc.
        qtd_inimigos_desejada = 1 + pontuacao // 10

        # Garante que a lista tenha a quantidade desejada de inimigos
        while len(inimigos) < qtd_inimigos_desejada:
            inimigos.append(criar_inimigo())

        # --- Movimento dos inimigos ---
        for inimigo in inimigos:
            inimigo[1] += vel_inimigo  # y += velocidade

            # Se sair da tela, reposiciona acima e soma ponto
            if inimigo[1] > ALTURA:
                inimigo[0] = random.randint(0, LARGURA - larg_inimigo)
                inimigo[1] = random.randint(-300, -alt_inimigo)
                pontuacao += 1

        # --- Colisão ---
        rect_jogador = pygame.Rect(x_jogador, y_jogador,
                                   larg_jogador, alt_jogador)

        for inimigo in inimigos:
            rect_inimigo = pygame.Rect(inimigo[0], inimigo[1],
                                       larg_inimigo, alt_inimigo)
            if rect_jogador.colliderect(rect_inimigo):
                game_over = True
                break

    # --- Desenho na tela ---
    tela.fill(PRETO)

    # Jogador
    pygame.draw.rect(
        tela, VERDE,
        (x_jogador, y_jogador, larg_jogador, alt_jogador)
    )

    # Inimigos
    for inimigo in inimigos:
        pygame.draw.rect(
            tela, VERMELHO,
            (inimigo[0], inimigo[1], larg_inimigo, alt_inimigo)
        )

    # Pontuação
    texto_pontos = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    # Mensagem de Game Over
    if game_over:
        texto_go = fonte.render(
            "GAME OVER! Aperte ESPAÇO para reiniciar.",
            True, BRANCO
        )
        tela.blit(texto_go, (200, ALTURA // 2))

    pygame.display.update()

pygame.quit()
