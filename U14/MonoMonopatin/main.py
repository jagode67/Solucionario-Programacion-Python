import pygame
from jugador import Jugador
from moneda import Moneda
from marcador import Marcador
from boton import Boton
from fogata import Fogata
from bola import Bola
import random
class Juego:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("recursos/Lucky_Day.mp3")
        pygame.mixer.music.set_volume(0.3)
        self.cash=pygame.mixer.Sound("recursos/cash.wav")
        self.pierdeVida=pygame.mixer.Sound("recursos/PierdeVida.wav")
        info = pygame.display.Info()
        self.pantalla_ancho = info.current_w-25
        self.pantalla_alto = info.current_h-100
        self.ventana=pygame.display.set_mode((
            self.pantalla_ancho,self.pantalla_alto))
        pygame.display.set_caption("Mono Monopatín")
        self.salir=False
        self.jugador= Jugador(self)
        self.clock=pygame.time.Clock()
        self.numero_monedas=50
        self.monedas=pygame.sprite.Group()
        for i in range(self.numero_monedas):
            self.monedas.add(Moneda(self, self.pantalla_ancho*(i+1),self.pantalla_alto/2))
        self.marcador=Marcador(self)
        self.activo= False
        self.boton_play=Boton(self,"Play")
        self.fogatas=pygame.sprite.Group()
        self.fogatas.add(Fogata(self,self.pantalla_ancho))
        self.fogatas.add(Fogata(self, self.pantalla_ancho*1.5))
        self.bolas=pygame.sprite.Group()

    def arrancarJuego(self):
        while not self.salir:
            dt=self.clock.tick(60)/1000
            self.gestionEventos()
            if self.activo:
                self.actualizaciones(dt)
            self.renderizacion()
        pygame.quit()
    def gestionEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.salir=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos= pygame.mouse.get_pos()
                if self.boton_play.pulsado(pos):
                    self.activo=True
                    pygame.mixer.music.play(-1)
                    self.jugador.vida=100
                    self.bolas.empty()
                    if len(self.monedas)==0:
                        for i in range(self.numero_monedas):
                            self.monedas.add(Moneda(self,self.pantalla_ancho*(i+1),self.pantalla_alto/2))
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.jugador.velocidad_x=-200.0
                if event.key==pygame.K_RIGHT:
                    self.jugador.velocidad_x=200.0
                if event.key==pygame.K_SPACE:
                    if self.jugador.ensuelo:
                        self.jugador.salto=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    self.jugador.velocidad_x=0.0
    def actualizaciones(self,dt):
        self.jugador.update(dt)
        self.monedas.update(dt)
        colisiones_monedas=pygame.sprite.spritecollide(self.jugador, self.monedas,True)
        self.marcador.update(len(colisiones_monedas))
        self.fogatas.update(dt)
        colisiones_fogatas=pygame.sprite.spritecollide(self.jugador,self.fogatas,True)
        if colisiones_fogatas:
            self.pierdeVida.play()
            self.jugador.vida-=10
            self.fogatas.add(Fogata(self,self.pantalla_ancho))
        self.bolas.update(dt)
        limite_alto=int(self.pantalla_alto*0.8)
        limite_bajo=int(self.pantalla_alto*0.2)
        if colisiones_monedas:
            self.cash.play()
            self.bolas.add(Bola(self,self.pantalla_ancho, random.randint(limite_bajo,limite_alto)))
        colisiones_bolas=pygame.sprite.spritecollide(self.jugador,self.bolas,True)
        if colisiones_bolas:
            self.pierdeVida.play()
            self.jugador.vida-=2
            self.bolas.add(Bola(self,self.pantalla_ancho,random.randint(limite_bajo,limite_alto)))
        if len(self.monedas)==0:
            self.activo=False
            pygame.mixer.music.stop()
        if self.jugador.vida<=0:
            self.activo=False
            pygame.mixer.music.stop()

    def renderizacion(self):
        self.ventana.fill((150,220,230))
        self.ventana.blit(self.jugador.image,self.jugador.rect)
        self.monedas.draw(self.ventana)
        self.marcador.render_marcador(self.jugador.vida)
        if not self.activo:
            self.boton_play.render_boton()
        self.fogatas.draw(self.ventana)
        self.bolas.draw(self.ventana)
        pygame.display.flip()
if __name__ == "__main__":
    juego=Juego()
    juego.arrancarJuego()
    