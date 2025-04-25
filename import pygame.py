import pygame

pygame.init()
window = pygame.display.set_mode((960,720))
window.fill((51,0,102))

#pygame.display.flip()

#load images
#clubs
ca = pygame.transform.scale(pygame.image.load("img/ace_of_clubs.png"),(100,145))
c7 = pygame.transform.scale(pygame.image.load("img/7_of_clubs.png"),(100,145))
c8 = pygame.transform.scale(pygame.image.load("img/8_of_clubs.png"),(100,145))
c9 = pygame.transform.scale(pygame.image.load("img/9_of_clubs.png"),(100,145))
c10 = pygame.transform.scale(pygame.image.load("img/10_of_clubs.png"),(100,145))
cj = pygame.transform.scale(pygame.image.load("img/jack_of_clubs.png"),(100,145))
cq = pygame.transform.scale(pygame.image.load("img/queen_of_clubs.png"),(100,145))
ck = pygame.transform.scale(pygame.image.load("img/king_of_clubs.png"),(100,145))
clubs = [ca, c7, c8, c9, c10, cj, cq, ck]
#diamonds
da = pygame.transform.scale(pygame.image.load("img/ace_of_diamonds.png"),(100,145))
d7 = pygame.transform.scale(pygame.image.load("img/7_of_diamonds.png"),(100,145))
d8 = pygame.transform.scale(pygame.image.load("img/8_of_diamonds.png"),(100,145))
d9 = pygame.transform.scale(pygame.image.load("img/9_of_diamonds.png"),(100,145))
d10 = pygame.transform.scale(pygame.image.load("img/10_of_diamonds.png"),(100,145))
dj = pygame.transform.scale(pygame.image.load("img/jack_of_diamonds.png"),(100,145))
dq = pygame.transform.scale(pygame.image.load("img/queen_of_diamonds.png"),(100,145))
dk = pygame.transform.scale(pygame.image.load("img/king_of_diamonds.png"),(100,145))
diamonds = [da, d7, d8, d9, d10, dj, dq, dk]
#hearts
ha = pygame.transform.scale(pygame.image.load("img/ace_of_hearts.png"),(100,145))
h7 = pygame.transform.scale(pygame.image.load("img/7_of_hearts.png"),(100,145))
h8 = pygame.transform.scale(pygame.image.load("img/8_of_hearts.png"),(100,145))
h9 = pygame.transform.scale(pygame.image.load("img/9_of_hearts.png"),(100,145))
h10 = pygame.transform.scale(pygame.image.load("img/10_of_hearts.png"),(100,145))
hj = pygame.transform.scale(pygame.image.load("img/jack_of_hearts.png"),(100,145))
hq = pygame.transform.scale(pygame.image.load("img/queen_of_hearts.png"),(100,145))
hk = pygame.transform.scale(pygame.image.load("img/king_of_hearts.png"),(100,145))
hearts = [ha, h7, h8, h9, h10, hj, hq, hk]
#spades
sa = pygame.transform.scale(pygame.image.load("img/ace_of_spades.png"),(100,145))
s7 = pygame.transform.scale(pygame.image.load("img/7_of_spades.png"),(100,145))
s8 = pygame.transform.scale(pygame.image.load("img/8_of_spades.png"),(100,145))
s9 = pygame.transform.scale(pygame.image.load("img/9_of_spades.png"),(100,145))
s10 = pygame.transform.scale(pygame.image.load("img/10_of_spades.png"),(100,145))
sj = pygame.transform.scale(pygame.image.load("img/jack_of_spades.png"),(100,145))
sq = pygame.transform.scale(pygame.image.load("img/queen_of_spades.png"),(100,145))
sk = pygame.transform.scale(pygame.image.load("img/king_of_spades.png"),(100,145))
spades = [sa, s7, s8, s9, s10, sj, sq, sk]

window.blit(ca,(160,120))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()