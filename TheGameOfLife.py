#TheGameOfLife

import random
import pygame

#Classes
class Life(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("GoL.png").convert()
        self.rect = self.image.get_rect()
        
        

    

#Pygame set-up
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

screen_x = 211
screen_y = 211
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The Game of Life")

done = False

clock = pygame.time.Clock()

frame_rate = 60
#Variables

all_sprites = pygame.sprite.Group()
array = []
item = 0
alive = False
birth = 0
ii = (5, 105, False)
true_list = []
false_list = []
check_array = []
for i in range(5, 206, 10):
    item = i
    for i in range(5, 206, 10):
        array.append([item, i, alive])


#objects

selector = Life()
all_sprites.add(selector)


#Main 
while not done:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selector.rect.x -= 10
            if event.key == pygame.K_RIGHT:
                selector.rect.x += 10
            if event.key == pygame.K_DOWN:
                selector.rect.y += 10
            if event.key == pygame.K_UP:
                selector.rect.y -= 10
            if event.key == pygame.K_SPACE:
                for item in array:
                    if item[0] == selector.rect.x+5 and item[1] == selector.rect.y+5:
                        if item[2] == True:
                            item[2] = False
                        if item[2] == False:
                            item[2] = True
            if event.key == pygame.K_TAB:
                for item in array:
                    this = item
        
                    for i in array:
                        if i[0] == this[0] - 10 and i[1] == this[1]:
                            check_array.append(i)
                        if i[0] == this[0] + 10 and i[1] == this[1]:
                            check_array.append(i)
                        if i[1] == this[1] - 10 and i[0] == this[0]:
                            check_array.append(i)
                        if i[1] == this[1] + 10 and i[0] == this[0]:
                            check_array.append(i)
                        if i[0] == this[0] - 10 and i[1] == this[1] - 10:
                            check_array.append(i)
                        if i[0] == this[0] - 10 and i[1] == this[1] + 10:
                            check_array.append(i)
                        if i[0] == this[0] + 10 and i[1] == this[1] - 10:
                            check_array.append(i)
                        if i[0] == this[0] + 10 and i[1] == this[1] + 10:
                            check_array.append(i)

        
                    for i in check_array:
                        if i[2] == True:
                            birth += 1  
                    if birth >= 4:
                        false_list.append(item)
                    if birth <= 1:
                        false_list.append(item)
                    if birth == 3:
                        true_list.append(item)
                    birth = 0
                    check_array = []
    
                counter = 0

                for item in array:
                    change = item
                    for item in false_list:
                        if item == change:
                            array[counter][2] = False
                    for item in true_list:
                        if item == change:
                            array[counter][2] = True
                    counter += 1
                true_list = []
                false_list = []
                
          
    
    #Draw
    screen.fill(WHITE)

       

    for i in array:
        if i[2] == True:
            pygame.draw.rect(screen, BLACK, (i[0]-5, i[1]-5, 10, 10))
        if i[2] == False:
            pygame.draw.rect(screen, WHITE, (i[0]-5, i[1]-5, 10, 10))

    for i in range(0,510,10):
        pygame.draw.line(screen, BLACK, [0,i], [500,i])
    for i in range(0,510,10):
        pygame.draw.line(screen, BLACK, [i,0], [i,500])

    all_sprites.draw(screen)
                

    
            

    
            
    pygame.display.flip()
    
    
    clock.tick(frame_rate)
    
pygame.quit()

