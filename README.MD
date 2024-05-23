# Proyectos de Redes Neuronales

Este documento resume tres proyectos diferentes que involucran el uso de redes neuronales en Python.

## RNADelta

### Descripción
Este proyecto implementa una red neuronal artificial utilizando el algoritmo de retropropagación del error (backpropagation) para entrenar el modelo. Se utiliza la biblioteca NumPy para realizar cálculos numéricos eficientes y la biblioteca Tkinter para crear la interfaz gráfica de usuario (GUI).

### Contenido del Repositorio
* El repositorio contiene los siguientes archivos:
    - rna.py: Implementación de la red neuronal.
    - window_msg.py: Implementación de la ventana de mensajes para mostrar alertas.
    - icono.ico: Icono de la aplicación.
    - bg-1.png: Imagen de fondo para la interfaz gráfica de usuario.
    - main.py: Código principal que configura la interfaz gráfica de usuario y maneja las interacciones del usuario.
    - report/: Carpeta que contendrá los reportes generados durante el entrenamiento del modelo.

### Requisitos
* Para ejecutar el programa, asegúrate de tener instaladas las siguientes bibliotecas de Python:
    - NumPy
    - Tkinter

### Uso
* Clona o descarga el repositorio en tu máquina local.
* Asegúrate de tener instaladas las dependencias mencionadas anteriormente.
* Ejecuta el archivo main.py con Python.
* La aplicación abrirá una ventana donde puedes cargar datos de entrada y salida, entrenar el modelo y realizar predicciones.

### Notas Adicionales
* El entrenamiento del modelo puede tomar tiempo dependiendo del tamaño de los datos y la complejidad del modelo.
* Los resultados del entrenamiento se guardan en la carpeta report/ en archivos de texto con información detallada sobre el proceso de entrenamiento.
* Si tienes algún problema o pregunta, consulta la ventana de mensajes para recibir alertas sobre posibles errores.

## ROCHAR

### Reconocimiento de caracteres en imágenes
Este programa está diseñado para reconocer caracteres en imágenes mediante el uso de redes neuronales artificiales. Utiliza la biblioteca scikit-learn para implementar un clasificador de perceptrón multicapa (MLP), que puede entrenarse con datos de entrada y sus respectivas etiquetas.

### Contenido del Repositorio
* El repositorio contiene los siguientes archivos y carpetas:
    - main.py: Código fuente del programa.
    - images/: Carpeta que contiene las imágenes de muestra utilizadas para entrenar y probar el modelo.
    - README.md: Archivo que proporciona información sobre el proyecto.

### Requisitos
* Para ejecutar el programa, asegúrate de tener instaladas las siguientes bibliotecas de Python:
    - NumPy
    - OpenCV
    - scikit-learn
    - Matplotlib

### Uso
* Clona o descarga el repositorio en tu máquina local.
* Asegúrate de tener instaladas las dependencias mencionadas anteriormente.
* Ejecuta el archivo main.py con Python.
* El programa entrenará el modelo utilizando las imágenes de muestra proporcionadas en la carpeta images/ y luego realizará predicciones sobre las imágenes de prueba.

### Notas Adicionales
* Puedes modificar los parámetros del clasificador MLP en el archivo main.py para ajustar su rendimiento.
* Asegúrate de tener suficiente poder de procesamiento y memoria disponible para entrenar el modelo, ya que el proceso puede ser intensivo en recursos.

## BACKPRO

### RNA - Red Neuronal Artificial
Este proyecto implementa una Red Neuronal Artificial (RNA) en Python utilizando la biblioteca NumPy. La RNA es capaz de entrenarse con conjuntos de datos proporcionados por el usuario y realizar predicciones una vez entrenada. Además, se proporciona una interfaz gráfica de usuario (GUI) para interactuar con la RNA de manera más intuitiva.

### Contenido del Repositorio
* Varios archivos que incluyen implementaciones de la RNA, ventanas de mensajes, configuraciones de red neuronal, etc.

### Uso
* Clona este repositorio en tu máquina local.
* Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
* Ejecuta el archivo main.py para iniciar la interfaz gráfica de usuario.
* Carga un conjunto de datos CSV utilizando la opción "Cargar dataset" en el menú "Modelo".
* Ajusta los parámetros de entrenamiento según sea necesario y haz clic en "Entrenar" para iniciar el entrenamiento de la RNA.
* Una vez entrenada la RNA, puedes utilizar el panel de predicción para realizar predicciones con nuevos datos.

¡Disfruta explorando estos proyectos y experimentando con las redes neuronales implementadas en cada uno!