def contar_triangulos_semejantes(puntos):
    """
    Cuenta la cantidad de triángulos semejantes al triángulo formado por los primeros tres puntos.
    """
    # Obtener los primeros tres puntos
    A, B, C = puntos[:3]

    # Inicializar el contador de triángulos semejantes
    count = 0

    # Iterar sobre todos los puntos
    for punto in puntos:
        if punto == A or punto == B or punto == C:
            continue  # Saltar los puntos que son parte del triángulo inicial

        # Calcular las pendientes de las líneas formadas por cada par de puntos con respecto a A, B y C
        pendiente_AB = (B[1] - A[1]) * (punto[0] - A[0]) - (B[0] - A[0]) * (punto[1] - A[1])
        pendiente_BC = (C[1] - B[1]) * (punto[0] - B[0]) - (C[0] - B[0]) * (punto[1] - B[1])
        pendiente_CA = (A[1] - C[1]) * (punto[0] - C[0]) - (A[0] - C[0]) * (punto[1] - C[1])

        # Verificar si los triángulos formados con el punto actual son semejantes al triángulo inicial
        if pendiente_AB == pendiente_BC == pendiente_CA:
            count += 1

    return count

# Lectura de la entrada
N = int(input())
puntos = [tuple(map(int, input().split())) for _ in range(N)]

# Contar triángulos semejantes
resultado = contar_triangulos_semejantes(puntos)

# Imprimir el resultado
print(resultado)



"""
6
0 0 
1 1 
-2 1 
5 2 
5 0 
2 3
"""