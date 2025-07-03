import pygame
class Marcador():
    def __init__(self,juego):
        self.ventana=juego.ventana
        self.num_monedas=0
        self.img_moneda= pygame.image.load(
                            "recursos/Moneda.png")
        self.alto_moneda=self.img_moneda.get_rect().height
        self.ancho_moneda=self.img_moneda.get_rect().width
        self.fuente=pygame.font.Font(
                           "recursos/Nise.ttf", 50)
        self.img_jugador=pygame.image.load(
                     "recursos/Mono_small.png")
        self.alto_jugador=self.img_jugador.get_rect().height
        self.ancho_jugador=self.img_jugador.get_rect().width

    def update(self,monedas_capturadas):
        self.num_monedas+=monedas_capturadas
    def render_marcador(self,vida):
        if self.num_monedas>0:
            x,y = 5,5
            self.ventana.blit(self.img_jugador,(x,y))
            x+=self.ancho_jugador*1.5
            texto_vida=str(vida)
            texto_vida_render=self.fuente.render(texto_vida,True,(0,0,0))
            self.ventana.blit(texto_vida_render,(x,y))
            x+=texto_vida_render.get_rect().width
            for i in range(self.num_monedas):
                self.ventana.blit(self.img_moneda,(x,y))
                x+=10
            x+=1.5*self.ancho_moneda
            texto= str(self.num_monedas)
            texto_render=self.fuente.render(texto,True, (0,0,0))
            self.ventana.blit(texto_render,(x,y))


