import matplotlib.pyplot as plt

class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = []

    def insertar(self, elemento):
        if len(self.elementos) < self.capacidad:
            self.elementos.append(elemento)
            self.dibujar_pila(f"insertar: {elemento}")
        else:
            print("error desbordamiento")

    def eliminar(self):
        if len(self.elementos) > 0:
            elemento = self.elementos.pop()
            self.dibujar_pila(f"eliminar: {elemento}")
        else:
            print("error subdesbordamiento")
            self.dibujar_pila("error subdesbordamiento")

    def dibujar_pila(self, operacion):
        fig, ax = plt.subplots(figsize=(5, 8))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, self.capacidad)
        
        for i, elem in enumerate(self.elementos):
            ax.barh(i, 1, color='blue', edgecolor='black')
            ax.text(0.5, i, str(elem), va='center', ha='center', color='white', fontsize=12)
        
        ax.set_yticks(range(self.capacidad))
        ax.set_yticklabels([])
        plt.title(operacion)
        plt.show()


pila = Pila(8)


pila.insertar('X')
pila.insertar('Y')
pila.eliminar()
pila.eliminar()
pila.eliminar()
pila.insertar('V')
pila.insertar('W')
pila.eliminar()
pila.insertar('R')
