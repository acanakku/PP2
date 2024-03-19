import pygame 
pygame.init()

clock = pygame.time.Clock()
W,H = 1080,720
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0 , 0 , 0)  
FPS = 60


sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Clock")
pygame.display.set_icon(pygame.image.load("D:\Programms\Labs\lab07\image\mickeyclock.jpeg"))

maincl = pygame.image.load('lab07\image\main-clock.png').convert_alpha()
maincl_rect = maincl.get_rect(center=(W//2,H//2))
sec = pygame.image.load('lab07\image\left-hand.png').convert_alpha()
sec = pygame.transform.rotate(sec , 90) 
sec_rect = sec.get_rect()
sec_rect.center = (W//2, H//2)

min = pygame.image.load('lab07\image\min-hand.png').convert_alpha()
min = pygame.transform.rotate(min , 90) 
min_rect = min.get_rect()
min_rect.center = (W//2, H//2)








angle = 0
angle1 = 0
run = True
while run:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False
            
    angle -= 0.1
    img1 = pygame.transform.rotate(sec , angle) 
    rect1 = img1.get_rect()
    rect1.center = sec_rect.center
    
    angle1 -= 0.00166666667
    img2 = pygame.transform.rotate(min , angle1) 
    rect2 = img2.get_rect()
    rect2.center = min_rect.center


    sc.fill(BLACK)
    sc.blit(maincl, maincl_rect)
    sc.blit(img1,rect1)
    sc.blit(img2, rect2)
    
    clock.tick(FPS)
    pygame.display.flip()


pygame.quit()
