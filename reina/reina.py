class Reina:
    def resolver(self, n):
        soluciones = []
        self._backtrack([], n, soluciones)
        return soluciones

    def _es_valido(self, solucion, fila, col):
        for i in range(fila):
            if solucion[i] == col or abs(solucion[i] - col) == abs(i - fila):
                return False
        return True

    def _backtrack(self, solucion_actual, n, soluciones):
        fila = len(solucion_actual)
        if fila == n:
            soluciones.append(solucion_actual[:])
            return
        for col in range(n):
            if self._es_valido(solucion_actual, fila, col):
                solucion_actual.append(col)
                self._backtrack(solucion_actual, n, soluciones)
                solucion_actual.pop()
