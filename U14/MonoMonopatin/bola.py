import pygame
import random
class Bola(pygame.sprite.Sprite):
    def __init__(self,juego,x,y):
        super().__init__()
        self.pa_alto=juego.pantalla_alto
        self.pa_ancho=juego.pantalla_ancho
        self.image= pygame.image.load("recursos/BolaDeFuego.png")
        self.x=float(x)
        self.y=float(y)
        # rectángulo contenedor
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.alto=self.rect.height
        self.ancho=self.rect.width
        self.velocidad_x=-300.0
        self.velocidad_y=0.0
    def update(self,dt):
        if self.x<-self.ancho or self.y<-self.alto:
            self.x=float(self.pa_ancho)
            self.y=float(200)
            self.velocidad_y=float(random.randint(0,200))
        self.x+=self.velocidad_x*dt
        self.y+=self.velocidad_y*dt
        self.rect.x=self.x
        self.rect.y=self.y
