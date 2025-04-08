from caballo.lanzador import run_visual as run_caballo
from reina.lanzador import run_visual as run_reinas

if __name__ == "__main__":
    run_caballo(k=2)   # Muestra movimientos del caballo
    run_reinas(n=8)    # Muestra solución del problema de las N-reinas
