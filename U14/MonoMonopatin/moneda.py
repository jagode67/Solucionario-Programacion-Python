import pygame
import random
class Moneda(pygame.sprite.Sprite):
    def __init__(self,juego,x,y):
        super().__init__()
        self.pa_alto=juego.pantalla_alto
        self.pa_ancho=juego.pantalla_ancho
        self.image= pygame.image.load("recursos/Moneda.png")
        self.x=float(x)
        self.y=float(y)
        # rectángulo contenedor
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
        self.alto=self.rect.height
        self.ancho=self.rect.width
        self.velocidad=-300.0
        self.incremento_velocidad=-10.0
        self.n_monedas=juego.numero_monedas
        self.limite_y=self.pa_alto-juego.jugador.alto-self.alto
    def update(self,dt):
        if self.x<-self.ancho:
            self.velocidad+=self.incremento_velocidad
            self.x=float(self.pa_ancho+
                       random.randint(0,self.pa_ancho))
            self.y=float(random.randint(2*self.alto,
                                        self.limite_y))
            self.rect.x=self.x
            self.rect.y=self.y
        self.x+=self.velocidad*dt
        self.rect.x=self.x 
