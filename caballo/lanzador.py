import pygame
from .caballo import Caballo, TECLADO_POS

def run_visual(k=1):
    caballo = Caballo()
    total = caballo.total_movimientos(k)

    pygame.init()
    pantalla = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("Movimientos del Caballo")
    fuente = pygame.font.SysFont(None, 36)

    corriendo = True
    while corriendo:
        pantalla.fill((255, 255, 255))

        # Dibujar teclado
        for num, (x, y) in TECLADO_POS.items():
            rect = pygame.Rect(x * 100 + 20, y * 100 + 20, 80, 80)
            pygame.draw.rect(pantalla, (200, 200, 200), rect)
            texto = fuente.render(str(num), True, (0, 0, 0))
            pantalla.blit(texto, (rect.x + 30, rect.y + 25))

        texto_total = fuente.render(f"Movimientos válidos: {total}", True, (0, 0, 255))
        pantalla.blit(texto_total, (20, 350))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pygame.display.flip()

    pygame.quit()
