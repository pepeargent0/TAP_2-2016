from sys import stdin, stdout
import time
inicio = time.time()
N, M = map(int, stdin.readline().split())
correlatividades = {i: set() for i in range(1, N + 1)}
for _ in range(M):
    A, B = map(int, stdin.readline().split())
    correlatividades[B].add(A)

orden_aprobacion = list(map(int, stdin.readline().split()))

# Inicialización de variables
materias_registradas = [0] * (N + 1)

# Procesamiento del orden de aprobación
for _ in orden_aprobacion:
    correlativas = correlatividades[_]
    todas_correlativas_registradas = all(materias_registradas[correlativa] > 0 for correlativa in correlativas)
    if todas_correlativas_registradas:
        materias_registradas[_] = materias_registradas[_ - 1] + 1
    else:
        materias_registradas[_] = materias_registradas[_ - 1]
    stdout.write(f'{materias_registradas[_]}\n')
    stdout.flush()
stdout.write(f'{time.time() - inicio}')
stdout.flush()

'''
3 2
1 2
2 3
1 2 3
4.267967939376831
'''