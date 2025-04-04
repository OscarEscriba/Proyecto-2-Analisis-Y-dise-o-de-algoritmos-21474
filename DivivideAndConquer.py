import time 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_bsts(start, end):
    """
    Genera todos los BST en el rango [start, end] usando Divide and Conquer.
    """
    if start > end:
        return [None]
    
    all_trees = []
    for root_val in range(start, end + 1):
        left_subtrees = generate_bsts(start, root_val - 1)    # Divide: subárbol izquierdo
        right_subtrees = generate_bsts(root_val + 1, end)     # Divide: subárbol derecho
        
        # Combine: combina todas las opciones
        for left in left_subtrees:
            for right in right_subtrees:
                root = TreeNode(root_val)
                root.left = left
                root.right = right
                all_trees.append(root)
    
    return all_trees

def print_tree(root, level=0, prefix="Raíz: "):
    """
    Imprime el árbol en consola con formato jerárquico.
    """
    if root is not None:
        print("    " * level + f"{prefix}{root.val}")
        if root.left or root.right:
            print_tree(root.left, level + 1, "Izq:  ")
            print_tree(root.right, level + 1, "Der:  ")

def visualize_tree_jpg(root, filename):
    """
    Genera una imagen JPG del árbol usando graphviz.
    """
    from graphviz import Digraph
    dot = Digraph(format='jpg')
    dot.attr('node', shape='circle')
    
    def add_nodes_edges(node):
        if node:
            dot.node(str(id(node)), str(node.val))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes_edges(node.right)
    
    add_nodes_edges(root)
    dot.render(filename, view=False)  # Genera el archivo JPG sin abrirlo automáticamente

n = 15  # Este es para saber el n. 
start_time = time.time()
all_bsts = generate_bsts(1, n)
end_time = time.time()

print(f"\n🔍 Total de BSTs para n={n}: {len(all_bsts)}\n")
print(f"⏱️ Tiempo de ejecución: {(end_time - start_time) * 1000:.2f} milisegundos\n")

""""
# Imprimir en consola y generar JPG
for idx, bst in enumerate(all_bsts, 1):
    print(f"🌳 Árbol {idx}:")
    print_tree(bst)
    visualize_tree_jpg(bst, f"bst_{idx}")  # Genera JPG
    print("\n" + "-" * 40 + "\n")

print("✅ ¡Imágenes JPG generadas en el directorio actual!")
"""