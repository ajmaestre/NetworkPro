# BACKPRO

## RNA - Red Neuronal Artificial
Este proyecto implementa una Red Neuronal Artificial (RNA) en Python utilizando la biblioteca NumPy. La RNA es capaz de entrenarse con conjuntos de datos proporcionados por el usuario y realizar predicciones una vez entrenada. Además, se proporciona una interfaz gráfica de usuario (GUI) para interactuar con la RNA de manera más intuitiva.

## Contenido del Repositorio
* rna_back.py: Contiene la implementación de la clase NeuralNetwork, que representa la red neuronal y sus funciones asociadas, como la propagación hacia adelante, la retropropagación y el entrenamiento.
* rna.py: Incluye una versión simplificada de la clase NeuralNetwork para ser utilizada en la GUI.
* window_msg.py: Proporciona una ventana de mensaje para mostrar alertas y notificaciones en la interfaz gráfica.
* w_umbral_weight.py: Contiene las ventanas para mostrar los umbrales y pesos de la RNA.
* w_config_net.py: Proporciona una ventana para mostrar la configuración de la red neuronal.
* label_header.py: Define etiquetas personalizadas para la interfaz gráfica.
* panel_dataset.py: Implementa el panel para cargar y mostrar conjuntos de datos CSV.
* panel_grafica_error.py: Crea el panel para mostrar la gráfica de error durante el entrenamiento.
* panel_param_train.py: Define el panel para ajustar los parámetros de entrenamiento de la RNA.
* panel_weight_umbral.py: Crea el panel para mostrar los pesos y umbrales de la RNA.
* panel_predict.py: Implementa el panel para realizar predicciones con la RNA.
* save_report.py: Contiene funciones para guardar los resultados del entrenamiento en un archivo.
## Uso
* Clona este repositorio en tu máquina local.
* Instala las dependencias necesarias ejecutando `pip install -r requirements.txt`.
* Ejecuta el archivo main.py para iniciar la interfaz gráfica de usuario.
* Carga un conjunto de datos CSV utilizando la opción "Cargar dataset" en el menú "Modelo".
* Ajusta los parámetros de entrenamiento según sea necesario y haz clic en "Entrenar" para iniciar el entrenamiento de la RNA.
* Una vez entrenada la RNA, puedes utilizar el panel de predicción para realizar predicciones con nuevos datos.
