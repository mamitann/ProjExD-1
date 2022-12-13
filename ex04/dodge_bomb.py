import pygame as pg
import random
import sys

def check_bound(obj_rct, scr_rct):
    #第1引数:こうかとんrectまたは爆弾rect
    #第2引数:スクリーンrect
    #範囲内:+1/範囲外:-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/7.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    scrn_sfc.blit(tori_sfc, tori_rct)

    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0 , 0), (10, 10), 50)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)

    bomb2_sfc = pg.Surface((20, 20))
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (255, 255 , 0), (10, 20), 10)
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx = random.randint(0, scrn_rct.width)
    bomb2_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb2_sfc, bomb2_rct)

    bomb3_sfc = pg.Surface((20, 20))
    bomb3_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb3_sfc, (255, 0 , 255), (10, 30), 100)
    bomb3_rct = bomb3_sfc.get_rect()
    bomb3_rct.centerx = random.randint(0, scrn_rct.width)
    bomb3_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb3_sfc, bomb3_rct)

    '''bomb4_sfc = pg.Surface((20, 20))
    bomb4_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb4_sfc, (255, 0 , 0), (10, 25), 50)
    bomb4_rct = bomb4_sfc.get_rect()
    bomb4_rct.centerx = random.randint(0, scrn_rct.width)
    bomb4_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb4_sfc, bomb4_rct)'''

    vx, vy = +1, +1
    vx2, vy2 = +2, +2
    vx3, vy3 = +3, +3
    '''vx4, vy4 = +2, +2'''

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 

        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 2
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 2
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 2
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 2
        if check_bound(tori_rct, scrn_rct) != (+1, +1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc, tori_rct)

        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        if tori_rct.colliderect(bomb_rct):

            return


        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)
        yoko, tate = check_bound(bomb2_rct, scrn_rct)
        vx2 *= yoko
        vy2 *= tate

        if tori_rct.colliderect(bomb2_rct):
            return 

        bomb3_rct.move_ip(vx3, vy3)
        scrn_sfc.blit(bomb3_sfc, bomb3_rct)
        yoko, tate = check_bound(bomb3_rct, scrn_rct)
        vx3 *= yoko
        vy3 *= tate

        if tori_rct.colliderect(bomb3_rct):
            return 

        '''bomb4_rct.move_ip(vx4, vy4)
        scrn_sfc.blit(bomb4_sfc, bomb4_rct)
        yoko, tate = check_bound(bomb4_rct, scrn_rct)
        vx *= yoko
        vy *= tate

        if tori_rct.colliderect(bomb4_rct):

            return'''

        pg.display.update()
        clock.tick(1000)


        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()