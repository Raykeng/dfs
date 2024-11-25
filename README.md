### Guía para usar el código en **Visual Studio Code**

Este tutorial te ayudará a configurar y ejecutar el código en Visual Studio Code (VS Code) para visualizar la búsqueda en profundidad (DFS) y el algoritmo de Dijkstra en un grafo.

---

### **1. Requisitos previos**
Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- **Python** (versión 3.6 o superior): Descárgalo e instálalo desde [python.org](https://www.python.org/).
- **Visual Studio Code**: Descárgalo desde [code.visualstudio.com](https://code.visualstudio.com/).

---

### **2. Instalación de librerías necesarias**
El código utiliza las siguientes librerías:
- **NetworkX**: Para trabajar con grafos.
- **Matplotlib**: Para la visualización gráfica de los algoritmos.

#### Comandos para instalar las librerías:
Abre una terminal y ejecuta los siguientes comandos:

```bash
pip install networkx matplotlib
```

---

### **3. Configuración en Visual Studio Code**
1. **Abre Visual Studio Code**.
2. **Crea un nuevo archivo de Python**:
   - Ve a `File > New File` y guarda el archivo con extensión `.py` (por ejemplo, `graph_visualization.py`).
3. **Selecciona el intérprete de Python**:
   - Presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en macOS) para abrir la barra de comandos.
   - Busca `Python: Select Interpreter`.
   - Selecciona la versión de Python que instalaste.

---

### **4. Copia el código**
Pega el código que te compartí anteriormente en el archivo `.py`.

---

### **5. Ejecuta el programa**
1. Abre la terminal integrada en VS Code:
   - Ve a `View > Terminal` o presiona `Ctrl + ~` (o `Cmd + ~` en macOS).
2. Ejecuta el archivo de Python:
   ```bash
   python graph_visualization.py
   ```

---

### **6. Interacción con el programa**
- **DFS Visualización**:
  - La ventana de Matplotlib se abrirá y mostrará cómo se visitan los nodos del grafo paso a paso.
- **Dijkstra Visualización**:
  - La ventana de Matplotlib mostrará la ruta más corta desde el nodo `'A'` hasta `'D'` si existe.

---

### **7. Errores comunes y soluciones**
1. **Error: "ModuleNotFoundError: No module named 'networkx'"**
   - Asegúrate de haber instalado las librerías usando el comando:
     ```bash
     pip install networkx matplotlib
     ```
   - Si el problema persiste, verifica que estás usando el mismo intérprete de Python donde instalaste las librerías.

2. **Error: "Python no está reconocido como un comando"**
   - Asegúrate de que Python esté agregado al PATH. Reinstala Python y marca la casilla "Add Python to PATH" durante la instalación.

3. **La ventana gráfica no se abre**:
   - En algunos entornos, Matplotlib puede no funcionar correctamente. Intenta añadir estas líneas al inicio del script:
     ```python
     import matplotlib
     matplotlib.use('TkAgg')
     ```

---

### **8. Personalización**
Si deseas cambiar el grafo o los parámetros, modifica las siguientes partes del código:
- **Nodos y aristas del grafo**:
  ```python
  edges = [
      ('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 1), ('B', 'E', 2), ('C', 'F', 1), ('C', 'G', 3)
  ]
  ```
  Cambia las aristas o los pesos según tu preferencia.

- **Nodos inicial y objetivo para Dijkstra**:
  ```python
  start_node = 'A'
  target_node = 'D'
  ```

---

### **9. Extensiones recomendadas para VS Code**
Instala estas extensiones para facilitar tu trabajo con Python en VS Code:
- **Python (Microsoft)**: Proporciona soporte para ejecutar y depurar Python.
- **Pylance**: Ofrece autocompletado inteligente y detección de errores.

---

### **10. Finalización**
Con estos pasos, deberías ser capaz de ejecutar el código en Visual Studio Code y ver las visualizaciones interactivas de DFS y Dijkstra. ¡Disfruta aprendiendo y explorando algoritmos de grafos!
