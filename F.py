from sys import stdin, stdout

F = int(stdin.readline())
amigos = []
for _ in range(F):
    amigo = stdin.readline()
    amigos.append(amigo)
max_dr = 0
stack = ''
found_r = False

for amigo in amigos:
    for letra in amigo:
        if letra == 'D':
            stack = 'D'
        elif letra == 'R' and stack != '':
            stack = ''
            max_dr += 1
stdout.write(f'{max_dr}\n')
stdout.flush()

"""
10
RAMIRO
AUGUSTO
JOAQUIN
JACINTO
NICOLAS
ALEJANDRO
DIJKSTRA
KAJITA
MCDONALD
SCHRODINGER
"""