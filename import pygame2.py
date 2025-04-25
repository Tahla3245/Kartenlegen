import pygame
from datetime import datetime
import os

pygame.init()
w = 1040
h = (w//4)*3
window = pygame.display.set_mode((w,h))
window.fill((51,0,102))

status = False #True==Done, False==Start

button_x = ((w*19)//48)
button_y = ((h*17)//18)
button_w = ((w*5)//24)
button_h = (h//26)
load_x = button_x - ((button_x)*2//3)
load_y = ((h*17)//18)
save_x = button_x + ((button_x)*2//3)
save_y = ((h*17)//18)
neu_x = ((w*19)//48)
neu_y = h-button_y-button_h
savesuc_x = save_x
savesuc_y = neu_y
load_table_x = w//4
load_table_h = (h//9)*8
load_table_y = h//17
load_table_w = w//2

button_font = pygame.font.SysFont("Arial",h//36)
load_font = pygame.font.SysFont("Arial",h//24)
fertig = button_font.render("Fertig",True,(205,205,205))
beenden = button_font.render("Beenden",True,(205,205,205))
save = button_font.render("Speichern",True,(205,205,205))
load = button_font.render("Laden",True,(205,205,205))
neu = button_font.render("Neu",True,(205,205,205))
savesuc = button_font.render("Speichern erfolgreich!",True,(205,205,205))
datum = load_font.render("Wähle ein Datum:",True,(205,205,205))

#load images
cw = (w*10)//96
ch = (h*29)//144
#mouse over size
mow = (15*w)//96
moh = (29*h)//96
#clubs
ca = pygame.transform.scale(pygame.image.load("img/ace_of_clubs.png"),(cw,ch))
ck = pygame.transform.scale(pygame.image.load("img/king_of_clubs.png"),(cw,ch))
cq = pygame.transform.scale(pygame.image.load("img/queen_of_clubs.png"),(cw,ch))
cj = pygame.transform.scale(pygame.image.load("img/jack_of_clubs.png"),(cw,ch))
c10 = pygame.transform.scale(pygame.image.load("img/10_of_clubs.png"),(cw,ch))
c9 = pygame.transform.scale(pygame.image.load("img/9_of_clubs.png"),(cw,ch))
c8 = pygame.transform.scale(pygame.image.load("img/8_of_clubs.png"),(cw,ch))
c7 = pygame.transform.scale(pygame.image.load("img/7_of_clubs.png"),(cw,ch))
#hearts
ha = pygame.transform.scale(pygame.image.load("img/ace_of_hearts.png"),(cw,ch))
hk = pygame.transform.scale(pygame.image.load("img/king_of_hearts.png"),(cw,ch))
hq = pygame.transform.scale(pygame.image.load("img/queen_of_hearts.png"),(cw,ch))
hj = pygame.transform.scale(pygame.image.load("img/jack_of_hearts.png"),(cw,ch))
h10 = pygame.transform.scale(pygame.image.load("img/10_of_hearts.png"),(cw,ch))
h9 = pygame.transform.scale(pygame.image.load("img/9_of_hearts.png"),(cw,ch))
h8 = pygame.transform.scale(pygame.image.load("img/8_of_hearts.png"),(cw,ch))
h7 = pygame.transform.scale(pygame.image.load("img/7_of_hearts.png"),(cw,ch))
#spades
sa = pygame.transform.scale(pygame.image.load("img/ace_of_spades.png"),(cw,ch))
sk = pygame.transform.scale(pygame.image.load("img/king_of_spades.png"),(cw,ch))
sq = pygame.transform.scale(pygame.image.load("img/queen_of_spades.png"),(cw,ch))
sj = pygame.transform.scale(pygame.image.load("img/jack_of_spades.png"),(cw,ch))
s10 = pygame.transform.scale(pygame.image.load("img/10_of_spades.png"),(cw,ch))
s9 = pygame.transform.scale(pygame.image.load("img/9_of_spades.png"),(cw,ch))
s8 = pygame.transform.scale(pygame.image.load("img/8_of_spades.png"),(cw,ch))
s7 = pygame.transform.scale(pygame.image.load("img/7_of_spades.png"),(cw,ch))
#diamonds
da = pygame.transform.scale(pygame.image.load("img/ace_of_diamonds.png"),(cw,ch))
dk = pygame.transform.scale(pygame.image.load("img/king_of_diamonds.png"),(cw,ch))
dq = pygame.transform.scale(pygame.image.load("img/queen_of_diamonds.png"),(cw,ch))
dj = pygame.transform.scale(pygame.image.load("img/jack_of_diamonds.png"),(cw,ch))
d10 = pygame.transform.scale(pygame.image.load("img/10_of_diamonds.png"),(cw,ch))
d9 = pygame.transform.scale(pygame.image.load("img/9_of_diamonds.png"),(cw,ch))
d8 = pygame.transform.scale(pygame.image.load("img/8_of_diamonds.png"),(cw,ch))
d7 = pygame.transform.scale(pygame.image.load("img/7_of_diamonds.png"),(cw,ch))
#other
colours = pygame.transform.scale(pygame.image.load("img/colours.png"),(cw,ch))
black = pygame.transform.scale(pygame.image.load("img/black.png"),(cw,ch))
red = pygame.transform.scale(pygame.image.load("img/red.png"),(cw,ch))
#entries

cards = [ca,ck,cq,cj,c10,c9,c8,c7,ha,hk,hq,hj,h10,h9,h8,h7,sa,sk,sq,sj,s10,s9,s8,s7,da,dk,dq,dj,d10,d9,d8,d7]

#create coordinates
coords = []
x = w//96
y = (h*5)//72
for i in range(4):
    for j in range(8):
        coords.append((x,y))
        x += (w*12)//96
    y += (h*16)//72
    x = w//96

#variables ""="empty", "clubs", "hearts", "spades", "diamonds", 
#    "0"="club ace", "1"="club king", ...

#create dictionary {0 = [variable, coords, cards]}
info = {}
for i in range(32):
    info[i] = ["", coords[i], cards[i]]

#create list with entries
entries = []
#entries = ["0","1",..."1023"]
for i in range(1024):
    i = pygame.transform.scale(pygame.image.load(f"cards entries/{i}.png"),(cw,ch))
    entries.append(i)

#hardcode
#status = True
#for i in range(32):
 #   info[i][0] = i

while True:
    if status == False:
        pygame.draw.rect(window,(205,205,205),(button_x,button_y,button_w,button_h),width=2,border_radius=5)
        pygame.draw.rect(window,(205,205,205),(load_x,load_y,button_w,button_h),width=2,border_radius=5)
        pygame.draw.rect(window,(51,0,102),(button_x+5,button_y+5,button_w-10,button_h-10))
        window.blit(fertig,((button_x + (button_w//2) - (fertig.get_width()//2)),(button_y + (button_h//2) - (fertig.get_height()//2))))
        window.blit(load,((load_x + (button_w//2) - (load.get_width()//2)),((button_y + (button_h//2) - (fertig.get_height()//2)))))
    else:
        pygame.draw.rect(window,(205,205,205),(button_x,button_y,button_w,button_h),width=2,border_radius=5)
        pygame.draw.rect(window,(205,205,205),(load_x,load_y,button_w,button_h),width=2,border_radius=5)
        pygame.draw.rect(window,(51,0,102),(button_x+5,button_y+5,button_w-10,button_h-10))
        window.blit(beenden,((button_x + (button_w//2) - (beenden.get_width()//2)),((button_y + (button_h//2) - (fertig.get_height()//2)))))
        window.blit(load,((load_x + (button_w//2) - (load.get_width()//2)),((button_y + (button_h//2) - (fertig.get_height()//2)))))
        pygame.draw.rect(window,(205,205,205),(save_x,save_y,button_w,button_h),width=2,border_radius=5)
        window.blit(save,((save_x + (button_w//2) - (save.get_width()//2)),((button_y + (button_h//2) - (fertig.get_height()//2)))))
        pygame.draw.rect(window,(205,205,205),(neu_x,neu_y,button_w,button_h),width=2,border_radius=5)
        window.blit(neu,((neu_x + (button_w//2) - (neu.get_width()//2)),(neu_y + (button_h//2) - (neu.get_height()//2))))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.MOUSEMOTION: 
            mp = event.pos
            
            if status == False:
                for i in range(32):
                    var = info[i][0]
                    x = info[i][1][0]
                    y = info[i][1][1]
                    img = info[i][2]
                    if var == "":
                        if pygame.Rect(x,y,cw,ch).collidepoint(mp):
                            window.blit(colours,(x,y))
                    
                        else:
                            img.set_alpha(50)
                            pygame.draw.rect(window,(51,0,102),(x,y,cw,ch))
                            window.blit(img,(x,y))
                            img.set_alpha(255)
                    pygame.display.flip()
            
            if status == True:
                pass
                #for i in range(32):
                    #card = info[i][0]
                    #x = info[i][1][0]
                    #y = info[i][1][1]
                    #entry = (i*32) + card 
                    #ent = pygame.transform.scale(pygame.image.load(f"cards entries/{entry}.png"),(mow,moh))
                    #if pygame.Rect(x,y,cw,ch).collidepoint(mp):
                        #window.blit(ent,(x,y))
                        #pygame.display.flip()
                    #else:
                        #pygame.draw.rect(window,(51,0,102),(x,y,cw,ch))
                        #window.blit(entries[entry],(x,y))
                        ##pygame.display.flip()
                    
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mp = event.pos

            if status == False:
                if pygame.Rect(button_x,button_y,button_w,button_h).collidepoint(mp): #Fertig
                    status = True
                if pygame.Rect(load_x,load_y,button_w,button_h).collidepoint(mp): #load
                    files = os.listdir()
                    status = "load"

                for i in range(32):
                    var = info[i][0]
                    x = info[i][1][0]
                    y = info[i][1][1]
                    img = info[i][2]

                    if var == "":
                        if pygame.Rect(x,y,cw//2,ch//2).collidepoint(mp):
                            window.blit(black,(x,y))
                            info[i][0] = "clubs"
                        elif pygame.Rect(x+(cw//2),y,cw//2,ch//2).collidepoint(mp):
                            window.blit(red,(x,y))
                            info[i][0] = "hearts"
                        elif pygame.Rect(x,y+(ch//2),cw//2,ch//2).collidepoint(mp):
                            window.blit(black,(x,y))
                            info[i][0] = "spades"
                        elif pygame.Rect(x+(cw//2),y+(ch//2),cw//2,ch//2).collidepoint(mp):
                            window.blit(red,(x,y))
                            info[i][0] = "diamonds"
                
                    if var == "clubs":
                        if pygame.Rect(x,y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[0],(x,y))
                            info[i][0] = 0
                        elif pygame.Rect(x+(cw//2),y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[1],(x,y))
                            info[i][0] = 1
                        elif pygame.Rect(x,y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[2],(x,y))
                            info[i][0] = 2
                        elif pygame.Rect(x+(cw//2),y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[3],(x,y))
                            info[i][0] = 3
                        elif pygame.Rect(x,y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[4],(x,y))
                            info[i][0] = 4
                        elif pygame.Rect(x+(cw//2),y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[5],(x,y))
                            info[i][0] = 5
                        elif pygame.Rect(x,y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[6],(x,y))
                            info[i][0] = 6
                        elif pygame.Rect(x+(cw//2),y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[7],(x,y))
                            info[i][0] = 7
                    elif var == "hearts":
                        if pygame.Rect(x,y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[8],(x,y))
                            info[i][0] = 8
                        elif pygame.Rect(x+(cw//2),y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[9],(x,y))
                            info[i][0] = 9
                        elif pygame.Rect(x,y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[10],(x,y))
                            info[i][0] = 10
                        elif pygame.Rect(x+(cw//2),y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[11],(x,y))
                            info[i][0] = 11
                        elif pygame.Rect(x,y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[12],(x,y))
                            info[i][0] = 12
                        elif pygame.Rect(x+(cw//2),y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[13],(x,y))
                            info[i][0] = 13
                        elif pygame.Rect(x,y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[14],(x,y))
                            info[i][0] = 14
                        elif pygame.Rect(x+(cw//2),y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[15],(x,y)) 
                            info[i][0] = 15
                    elif var == "spades":
                        if pygame.Rect(x,y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[16],(x,y))
                            info[i][0] = 16
                        elif pygame.Rect(x+(cw//2),y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[17],(x,y))
                            info[i][0] = 17
                        elif pygame.Rect(x,y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[18],(x,y))
                            info[i][0] = 18
                        elif pygame.Rect(x+(cw//2),y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[19],(x,y))
                            info[i][0] = 19
                        elif pygame.Rect(x,y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[20],(x,y))
                            info[i][0] = 20
                        elif pygame.Rect(x+(cw//2),y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[21],(x,y))
                            info[i][0] = 21
                        elif pygame.Rect(x,y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[22],(x,y))
                            info[i][0] = 22
                        elif pygame.Rect(x+(cw//2),y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[23],(x,y))
                            info[i][0] = 23
                    elif var == "diamonds":
                        if pygame.Rect(x,y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[24],(x,y))
                            info[i][0] = 24
                        elif pygame.Rect(x+(cw//2),y,cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[25],(x,y))
                            info[i][0] = 25
                        elif pygame.Rect(x,y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[26],(x,y))
                            info[i][0] = 26
                        elif pygame.Rect(x+(cw//2),y+(ch//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[27],(x,y))
                            info[i][0] = 27
                        elif pygame.Rect(x,y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[28],(x,y))
                            info[i][0] = 28
                        elif pygame.Rect(x+(cw//2),y+(ch//2),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[29],(x,y))
                            info[i][0] = 29
                        elif pygame.Rect(x,y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[30],(x,y))
                            info[i][0] = 30
                        elif pygame.Rect(x+(cw//2),y+((ch*3)//4),cw//2,ch//4).collidepoint(mp):
                            window.blit(cards[31],(x,y))
                            info[i][0] = 31

                    if var in range(32):
                        if pygame.Rect(x,y,cw,ch).collidepoint(mp):
                            info[i][0] = ""
                            window.blit(colours,(x,y))
                
            elif status == True:
                if pygame.Rect(button_x,button_y,button_w,button_h).collidepoint(mp): #beenden
                    exit()
                elif pygame.Rect(neu_x,neu_y,button_w,button_h).collidepoint(mp): #neu
                    status = False
                    for i in range(32):
                        info[i][0] = ""
                elif pygame.Rect(save_x,save_y,button_w,button_h).collidepoint(mp): #speichern
                    now = datetime.now()
                    today = now.strftime(f"%d-%m-%Y %H-%M")
                    with open(f"save/{today}.csv","w") as file:
                        for i in range(32):
                            line = str(info[i][0])
                            file.write(line+",")
                    window.blit(savesuc,(savesuc_x + (button_w//2) - (savesuc.get_width()//2),savesuc_y))

            elif status == "load":
                pygame.draw.rect(window,(51,0,102),(load_table_x,load_table_y,load_table_w,load_table_h))
                pygame.draw.rect(window, (205,205,205),(load_table_x,load_table_y,load_table_w,load_table_h),width=2,border_radius=5)
                window.blit(datum,((load_table_x + load_table_w//2 - datum.get_width()//2),(load_table_y + 3*datum.get_height()//5)))

        if status == True:
            for i in range(32):
                card = info[i][0]
                x = info[i][1][0]
                y = info[i][1][1]
                entry = (i*32) + card 
                    #ent = pygame.transform.scale(pygame.image.load(f"cards entries/{entry}.png"),(mow,moh))
                    #if pygame.Rect(x,y,cw,ch).collidepoint(mp):
                        #window.blit(ent,(x,y))
                        #pygame.display.flip()
                    #else:
                        #pygame.draw.rect(window,(51,0,102),(x,y,cw,ch))
                window.blit(entries[entry],(x,y))
                        ##pygame.display.flip()

        pygame.display.flip()