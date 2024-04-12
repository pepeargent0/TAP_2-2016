import time
from sys import stdin, stdout
inicio = time.time()
palabra = map(str, stdin.readline().strip())
if 'i' in palabra:
    stdout.write("N\n")
else:
    stdout.write("S\n")
stdout.flush()
print(time.time() - inicio)