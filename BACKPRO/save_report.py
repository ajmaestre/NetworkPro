import numpy as np
import datetime


def saveResultTraining(entradas, salidas, epochs, error, rate, iters, weights, umbrals, weightsInit, umbralsInit, typenet):
    fileReport = np.array(["--------------------------------------------------------------------------------------"])
    header = "--------------------------------------------------------------------------------------"
    fecha_hora_actual = datetime.datetime.now()
    fecha_hora_actual = fecha_hora_actual.strftime('%Y-%m-%d-%H-%M-%S')
    title = f"Reporte de entrenamiento utilizando {typenet} - {fecha_hora_actual}"
    fileReport = np.append(fileReport, title)
    fileReport = np.append(fileReport, "--------------------------------------------------------------------------------------")
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Numero de entradas")
    fileReport = np.append(fileReport, entradas.shape[1])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Numero de salidas")
    fileReport = np.append(fileReport, salidas.shape[1])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Numero de patrones")
    fileReport = np.append(fileReport, entradas.shape[0])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Pesos iniciales")
    fileReport = np.append(fileReport, np.around(weightsInit, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Umbrales iniciales")
    fileReport = np.append(fileReport, np.around(umbralsInit, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Pesos finales")
    fileReport = np.append(fileReport, np.around(weights, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Umbrales finales")
    fileReport = np.append(fileReport, np.around(umbrals, decimals=2))
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Iteraciones alcanzadas")
    fileReport = np.append(fileReport, iters[-1])
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Iteraciones totales")
    fileReport = np.append(fileReport, epochs)
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Error maximo permitido")
    fileReport = np.append(fileReport, error)
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "Rata de aprendizaje")
    fileReport = np.append(fileReport, rate)
    fileReport = np.append(fileReport, "")
    fileReport = np.append(fileReport, "--------------------------------------------------------------------------------------")
    fileReport = np.append(fileReport, f'Fecha de registo {fecha_hora_actual}')
    np.savetxt(f'report/report_{fecha_hora_actual}.txt', fileReport, fmt='%s', delimiter=',', header=header, footer=header)
