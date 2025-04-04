import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_bsts(start, end):
    if start > end:
        return [None]
    
    all_trees = []
    for root_val in range(start, end + 1):
        left_subtrees = generate_bsts(start, root_val - 1)
        right_subtrees = generate_bsts(root_val + 1, end)
        
        for left in left_subtrees:
            for right in right_subtrees:
                all_trees.append(TreeNode(root_val, left, right))
    
    return all_trees

def measure_execution_time(n_values):
    execution_times = {}
    
    for n in n_values:
        start_time = time.time()
        generate_bsts(1, n)
        end_time = time.time()
        
        execution_times[n] = (end_time - start_time) * 1000  # ms
        print(f"n = {n}: {execution_times[n]:.2f} ms")
    
    return execution_times

def plot_execution_times(execution_data):
    n_values = list(execution_data.keys())
    times = list(execution_data.values())
    
    plt.figure(figsize=(12, 8))
    plt.plot(n_values, times, 'bo-', linewidth=2, markersize=8)
    plt.title('Tiempo de ejecución vs Número de nodos (BST)')
    plt.xlabel('Número de nodos (n)')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(n_values)
    plt.savefig('tiempos_bst_DaC.png')  # Guarda la gráfica como PNG
    plt.show()

# Configuración de la prueba
n_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  

# Ejecutar las pruebas y generar gráfica
print("⚡ Iniciando pruebas de rendimiento...\n")
time_data = measure_execution_time(n_values)
print("\n📊 Generando gráfica de resultados...")
plot_execution_times(time_data)