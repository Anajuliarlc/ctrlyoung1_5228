import pygame as pg

pg.init()

tela = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

x, y = 400, 300
vel = 5

rodando = True
while rodando:
    clock.tick(60)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False
    teclas = pg.key.get_pressed()
    if teclas[pg.K_w]: y -= vel
    if teclas[pg.K_s]: y += vel
    if teclas[pg.K_a]: x -= vel
    if teclas[pg.K_d]: x += vel
    tela.fill((20, 20, 20))
    pg.draw.rect(tela, (0, 200, 50), (x, y, 40, 40))
    pg.display.update()

pg.quit()