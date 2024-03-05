def runge_kutta(y, t, h):
    k1 = h * (-2*y + 4*t)
    k2 = h * (-2*(y + 0.5*k1) + 4*(t + 0.5*h))
    k3 = h * (-2*(y + 0.5*k2) + 4*(t + 0.5*h))
    k4 = h * (-2*(y + k3) + 4*(t + h))
    
    y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0
    return y_new

# Condição inicial
y_0 = 1

# Tamanho do passo
h = 0.1

# Número total de passos
num_steps = 100

# Inicialização de listas para armazenar resultados
t_values = [i * h for i in range(num_steps + 1)]
y_values = [y_0]

# Iterações RK4
for i in range(num_steps):
    y_0 = runge_kutta(y_0, t_values[i], h)
    y_values.append(y_0)

# Resultados
for t, y in zip(t_values, y_values):
    print(f"t = {t:.2f}, y = {y:.4f}")
