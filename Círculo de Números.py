import math

def draw_circle_of_numbers(radius):
    diameter = 2 * radius + 1
    center = radius

    for y in range(diameter):
        for x in range(diameter):
            # Calcula a distância do ponto (x, y) ao centro
            distance = math.sqrt((x - center) ** 2 + (y - center) ** 2)
            
            # Verifica se o ponto está próximo da borda do círculo
            if radius - 0.5 <= distance <= radius + 0.5:
                # Imprime o número correspondente à posição do ponto
                print((x + y) % 10, end=" ")
            else:
                # Espaço vazio para manter o formato do círculo
                print(" ", end=" ")
        print()  # Quebra de linha para a próxima linha do círculo

# Exemplo de uso
draw_circle_of_numbers(5)
input()