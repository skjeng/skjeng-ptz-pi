import sys
import pygame
import pygame.camera

def servo_up():
    sb = open('/dev/servoblaster', 'w')
    print("P1-18=-"+str(2), file=sb)

def servo_down():
    sb = open('/dev/servoblaster', 'w')
    print("P1-18=+"+str(2), file=sb)

def servo_left():
    sb = open('/dev/servoblaster', 'w')
    print("P1-12=+"+str(2), file=sb)

def servo_right():
    sb = open('/dev/servoblaster', 'w')
    print("P1-12=-"+str(2), file=sb)


pygame.display.init()
pygame.camera.init()

display_width = 800
display_height = 600
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CamServo")
clock = pygame.time.Clock()

cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(800,600))
cam.start()

old_repeat = pygame.key.get_repeat()
pygame.key.set_repeat(1,1)

print(old_repeat)

while True:
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1,(800,600))
    gameDisplay.blit(image1,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            cam.stop()
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                servo_left()
            if event.key == pygame.K_UP:
                servo_up()
            if event.key == pygame.K_RIGHT:
                servo_right()
            if event.key == pygame.K_DOWN:
                servo_down()
                
    pygame.display.update()
    clock.tick(120)

