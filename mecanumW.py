import math

def calcular_ruedas(vx, vy, omega):
    """Matriz de cinemática para 4 ruedas mecanum (configuración en X)."""
    return {
        "FL": vx - vy - omega,
        "FR": vx + vy + omega,
        "RL": vx + vy - omega,
        "RR": vx - vy + omega,
    }

def normalizar(ruedas):
    """Si algún valor pasa de 1, escala todos para que el máximo sea 1."""
    maximo = max(abs(v) for v in ruedas.values())
    if maximo > 1:
        return {k: v / maximo for k, v in ruedas.items()}
    return ruedas

def angulo_a_componentes(angulo_grados, velocidad):
    """Convierte un ángulo y una velocidad en vx y vy usando sin y cos."""
    theta = math.radians(angulo_grados)
    vx = velocidad * math.cos(theta)
    vy = velocidad * math.sin(theta)
    return vx, vy

def main():
    print("=== Control de carro mecanum ===")
    print("Ángulo: 0 = adelante, 90 = izquierda, 180 = atrás, 270 = derecha")
    angulo = float(input("Dirección (grados): "))
    velocidad = float(input("Velocidad (0 a 1): "))
    omega = float(input("Rotación (-1 a 1, positivo = izquierda, 0 = no girar): "))

    vx, vy = angulo_a_componentes(angulo, velocidad)
    ruedas = normalizar(calcular_ruedas(vx, vy, omega))

    print("\n--- Resultado por rueda ---")
    for nombre, valor in ruedas.items():
        pwm = round(abs(valor) * 255)
        if pwm == 0:
            sentido = "parada"
        elif valor > 0:
            sentido = "adelante"
        else:
            sentido = "atrás"
        print(f"{nombre}: {sentido:8s}  valor = {valor:+.3f}  PWM = {pwm}")

if __name__ == "__main__":
    main()