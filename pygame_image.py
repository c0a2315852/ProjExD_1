import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")  #画像を読み込む関数
    img_3 = pg.image.load("fig/3.png") #3.png の読み込み
    img_3 = pg.transform.flip(img_3, True, False) #上下左右反転
    bg_img_2 = pg.transform.flip(bg_img, True, False) #練習7-1
    img_3_rct = img_3.get_rect()
    img_3_rct.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            img_3_rct.move_ip([0, -1])
        if key_lst[pg.K_DOWN]:
            img_3_rct.move_ip([0, +1])
        if key_lst[pg.K_LEFT]:
            img_3_rct.move_ip([-1, 0])
        if key_lst[pg.K_RIGHT]:
            img_3_rct.move_ip([+1, 0])
        x = tmr % 3200 #練習6(tmr % 800) 変更後 練習7-2
        screen.blit(bg_img, [-x, 0]) #練習6
        screen.blit(bg_img_2, [-x + 1600, 0]) #練習7-1 x座標
        screen.blit(bg_img, [-x + 3200, 0])  #練習7-2
        screen.blit(bg_img_2, [-x + 4800, 0]) #練習7-2
        
        #screen.blit(img_3, [300, 200]) #こうかとんを横300縦200の位置にblit
        screen.blit(img_3, img_3_rct)

        pg.display.update()
        tmr += 1    
        clock.tick(200) #FPSを200へ


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()