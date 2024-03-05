import numpy as np
import matplotlib.pyplot as plt

# Definindo as equações diferenciais
def sistema(x, y):
    dxdt = 2*x - y
    dydt = x + 3*y
    return dxdt, dydt

# Condições iniciais
x0, y0 = 1, 2

# Parâmetros de discretização
delta_t = 0.1
tempo = np.arange(0, 2.1, delta_t)

# Inicializando arrays para armazenar as soluções
x_sol = np.zeros_like(tempo)
y_sol = np.zeros_like(tempo)

# Condições iniciais
x_sol[0] = x0
y_sol[0] = y0

# Método de Euler para resolver o sistema de equações diferenciais
for i in range(1, len(tempo)):
    dxdt, dydt = sistema(x_sol[i-1], y_sol[i-1])
    x_sol[i] = x_sol[i-1] + delta_t * dxdt
    y_sol[i] = y_sol[i-1] + delta_t * dydt

# Plotando as soluções
plt.plot(tempo, x_sol, label='x(t)')
plt.plot(tempo, y_sol, label='y(t)')
plt.xlabel('Tempo')
plt.ylabel('Variáveis de Estado')
plt.legend()
plt.show()
