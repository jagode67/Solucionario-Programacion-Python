import pygame
class Jugador(pygame.sprite.Sprite):
    def __init__(self,juego):
        super().__init__()
        self.pa_alto=juego.pantalla_alto
        self.pa_ancho=juego.pantalla_ancho
        # animación
        mono_1=pygame.image.load("recursos/Mono_1.png")
        mono_2=pygame.image.load("recursos/Mono_2.png")
        self.imagenes=[mono_1,mono_2]
        self.index=0
        self.image=self.imagenes[self.index]
        self.t_acumulado=0.0
        self.t_fotograma=0.1
        # posición inicial del jugador
        self.rect=self.image.get_rect()
        self.alto=self.rect.height
        self.ancho=self.rect.width
        self.x=0.0
        self.y=juego.pantalla_alto-self.image.get_rect().height
        self.rect.x=self.x
        self.rect.y=self.y
        self.ensuelo=True
        self.salto=False
        self.velocidad_x=0.0
        self.velocidad_y=0.0
        self.aceleracion_y=100.0
        self.vida=100
    def update(self,dt):
        self.t_acumulado+=dt
        if self.t_acumulado>=self.t_fotograma:
            self.t_acumulado=0
            self.index=(self.index+1)%len(self.imagenes)
            self.image=self.imagenes[self.index]
        if self.ensuelo:
            if self.velocidad_x<0 and self.x>0:
                self.x+=self.velocidad_x*dt
            if self.velocidad_x>0 and self.x<self.pa_ancho-self.ancho:
                self.x+=self.velocidad_x*dt
            self.rect.x=self.x
        if self.salto:
            self.velocidad_y=-300.0
            self.ensuelo=False
            self.salto=False
        if not self.ensuelo:
            self.velocidad_y+=self.aceleracion_y*dt
            self.y+=self.velocidad_y*dt
            if self.y>self.pa_alto-self.alto:
                self.ensuelo=True
                self.velocidad_y=0.0
            else:
                self.rect.y=self.y



