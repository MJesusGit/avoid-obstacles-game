import pygame
import sys
import random 

#constantes
ancho=800
alto=800
colorPlayer=(74,171,160)
black=(0,0,0)


#player
size_player=[50,50]
#position_player=[400,400]
#to center the player we should do:
position_player=[ancho/2, alto-size_player[0]*2 ]

#Enemy(ies)
enemies_color=(188,204,255)
size_enemy=50
position_enemy=[random.randint(0,ancho-size_enemy),0]

# To create the window we need to have has arguent in set_mode a tupla with the height and weight
ventana= pygame.display.set_mode((ancho,alto))

#Tu run the window we need a loop
gameOver = False
clock=pygame.time.Clock()

def detection_of_collitions(position_player,position_enemy):
    px=position_player[0]
    py=position_player[1]
    ex=position_enemy[0]
    ey=position_enemy[1]

    if (ex >= px and ex<(px + size_player[0])) or (px >= ex and  px < (ex + size_enemy)):
        if(ey >= py and ey<(py + size_player[0])) or (py >= ey and  py < (ey + size_enemy)):
            return True
    return False

while not gameOver:
   
    for event in pygame.event.get():
         #close window
        if event.type==pygame.QUIT:
            sys.exit()
        #movement of keys
        if event.type==pygame.KEYDOWN:
            x= position_player[0]
            if event.key== pygame.K_LEFT:
               x -= size_player[0]
            if event.key==pygame.K_RIGHT:
                x += size_player[0]

            position_player[0]= x


    #clean the window when we move the player
    ventana.fill(black)


    #movement of the enemies
    if position_enemy[1]>=0 and position_enemy[1]<alto:
        position_enemy[1]+=20
    else:
        position_enemy[1]=0
        position_enemy[0]=random.randint(0,ancho-size_enemy)




    #collisions
    if detection_of_collitions (position_player,position_enemy):
        gameOver = True


    #Draw enemy
    pygame.draw.rect(ventana,enemies_color,
                    (position_enemy[0],position_enemy[1],
                    size_enemy,size_enemy))
   



    #Draw player
    #color,position,size
    pygame.draw.rect(ventana,colorPlayer,
                    (position_player[0],position_player[1], #x ,y
                    size_player[0],size_player[1]))# w,h


    

    clock.tick(40)

    pygame.display.update()


   