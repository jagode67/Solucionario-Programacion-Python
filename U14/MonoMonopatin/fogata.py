import pygame
class Fogata(pygame.sprite.Sprite):
    def __init__(self,juego,x):
        super().__init__()
        self.pa_alto=juego.pantalla_alto
        self.pa_ancho=juego.pantalla_ancho
        # animación
        fuego_1=pygame.image.load("recursos/Fuego_1.png")
        fuego_2=pygame.image.load("recursos/Fuego_2.png")
        fuego_3=pygame.image.load("recursos/Fuego_3.png")
        fuego_4=pygame.image.load("recursos/Fuego_4.png")
        self.imagenes=[fuego_1,fuego_2,fuego_3,fuego_4]
        self.index=0
        self.image=self.imagenes[self.index]
        self.t_acumulado=0.0
        self.t_fotograma=0.1
        # posición inicial        
        self.x=float(x)
        # rectángulo contenedor
        self.rect=self.image.get_rect()
        self.alto=self.rect.height
        self.ancho=self.rect.width
        self.rect.x=self.x
        self.rect.y=self.pa_alto-self.alto
        self.velocidad=-50.0
    def update(self,dt):
        # actualización de la posición
        self.x+=self.velocidad*dt
        self.rect.x=self.x
        #actualización de la animación
        self.t_acumulado+=dt
        if self.t_acumulado>=self.t_fotograma:
            self.t_acumulado=0
            self.index=(self.index+1)%len(self.imagenes)
            self.image=self.imagenes[self.index]
        # detecta choque con borde izquierdo
        if self.x<-self.ancho:
            self.x=self.pa_ancho
            self.rect.x=self.x

