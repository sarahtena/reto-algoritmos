MOVIMIENTOS = {
    0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
    4: [0, 3, 9], 5: [], 6: [0, 1, 7],
    7: [2, 6], 8: [1, 3], 9: [2, 4]
}

TECLADO_POS = {
    0: (1, 3), 1: (0, 0), 2: (1, 0), 3: (2, 0),
    4: (0, 1), 5: (1, 1), 6: (2, 1),
    7: (0, 2), 8: (1, 2), 9: (2, 2)
}

class Caballo:
    def __init__(self):
        self.memo = {}

    def contar_movimientos(self, d, k):
        if k == 0:
            return 1
        if (d, k) in self.memo:
            return self.memo[(d, k)]
        total = sum(self.contar_movimientos(n, k - 1) for n in MOVIMIENTOS[d])
        self.memo[(d, k)] = total
        return total

    def total_movimientos(self, k):
        self.memo.clear()
        return sum(self.contar_movimientos(d, k) for d in range(10))
