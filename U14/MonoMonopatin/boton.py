import pygame
class Boton():
    def __init__(self,juego,texto):
        self.ventana=juego.ventana
        self.ventana_rect=self.ventana.get_rect()
        #dimensiones del boton
        self.ancho, self.alto= 200,70
        self.color=(0,0,0)
        self.color_texto =(255,255,255)
        self.fuente=pygame.font.Font(
                           "recursos/Nise.ttf", 50)
        #rectangulo contenedor centrado en pantalla
        self.rect=pygame.Rect(0,0,self.ancho,self.alto)
        self.rect.center=self.ventana_rect.center
        # Mensaje del boton
        self.label=self.fuente.render(texto,True,
                            self.color_texto,self.color)
        self.label_rect=self.label.get_rect()
        self.label_rect.center=self.rect.center
    def render_boton(self):
        self.ventana.fill(self.color,self.rect)
        self.ventana.blit(self.label,self.label_rect)
    def pulsado(self,pos):
        if self.rect.collidepoint(pos):
            return True
        else:
            return False
