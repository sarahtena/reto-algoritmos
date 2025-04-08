import pygame
from .reina import Reina

def run_visual(n=8):
    reina = Reina()
    soluciones = reina.resolver(n)
    if not soluciones:
        print("No hay solución.")
        return

    solucion = soluciones[0]

    pygame.init()
    size = 60
    pantalla = pygame.display.set_mode((n * size, n * size))
    pygame.display.set_caption(f"{n}-Reinas")
    reina_img = pygame.Surface((size, size))
    pygame.draw.circle(reina_img, (0, 0, 0), (size // 2, size // 2), size // 3)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        for fila in range(n):
            for col in range(n):
                color = (240, 217, 181) if (fila + col) % 2 == 0 else (181, 136, 99)
                pygame.draw.rect(pantalla, color, pygame.Rect(col * size, fila * size, size, size))

        for col, fila in enumerate(solucion):
            pantalla.blit(reina_img, (col * size, fila * size))

        pygame.display.flip()

    pygame.quit()
