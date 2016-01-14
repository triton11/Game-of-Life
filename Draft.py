#Draft GoL

import pygame

all_sprites = pygame.sprite.Group()
array = []
item = 0
alive = False
birth = 0
ii = (5, 105, False)

check_array = []
for i in range(5, 26, 10):
    item = i
    for i in range(5, 26, 10):
        array.append([item, i, alive])

true_list = []
false_list = []

for item in array:
        this = item
        print(item)
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

        print (check_array)
        for i in check_array:
                if i[2] == True:
                        birth += 1
                        print (birth)
                        
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
print (array)
