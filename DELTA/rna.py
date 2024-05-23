import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        # Inicialización de pesos y umbrales de manera aleatoria
        self.list_weight = np.random.randn(input_size, output_size)
        self.list_umbral = np.random.randn(1, output_size)
        self.weights = np.copy(self.list_weight)
        self.bias = np.copy(self.list_umbral)
        
    def hard_limiter(self, x):
        # Función de activación limitador duro
        return np.where(x >= 0, 1, 0)
    
    def forward(self, X):
        # Propagación hacia adelante
        self.output = self.hard_limiter(np.dot(X, self.weights) + self.bias)
        return self.output
    
    def backward(self, X, y, output, learning_rate):
        # Retropropagación del error utilizando la regla delta
        error = y - output
        delta = error
        # Actualización de pesos y sesgo
        self.weights += X.T.dot(delta) * learning_rate
        self.bias += np.sum(delta, axis=0, keepdims=True) * learning_rate
    
    def train(self, X, y, epochs, learning_rate, tol):
        list_loss = []
        list_epoch = []
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output, learning_rate)
            if epoch % 2 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss}")
                list_loss.append(loss)
                list_epoch.append(epoch)
                if loss <= tol:
                    return list_loss, list_epoch, self.weights, self.bias, self.list_weight, self.list_umbral

