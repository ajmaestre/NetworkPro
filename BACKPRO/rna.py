import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_functions, output_size):
        self.input_size = input_size
        self.hidden_functions = hidden_functions
        self.output_size = output_size

        self.list_functions_activations = [self.sigmoid, self.tanh_activation, self.sin_activation, self.linear_activation]
        self.list_functions_derivative = [self.sigmoid_derivative, self.tanh_derivative, self.sin_derivative, self.linear_derivative]

        # Inicialización de pesos y sesgos
        self.W = np.random.randn(input_size, output_size)
        self.b = np.zeros((1, output_size))

        self.list_weights = np.copy(self.W)
        self.list_bias = np.copy(self.b)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)

     # función tangente hiperbólica
    def tanh_activation(self, x):
        res = np.tanh(x)
        return res

    # derivada de la función tangente hiperbólica
    def tanh_derivative(self, x):
        res = 1 - np.tanh(x)**2
        return res

    # función seno
    def sin_activation(self, x):
        res = np.sin(x)
        return res

    # derivada de la función seno
    def sin_derivative(self, x):
        res = np.cos(x)
        return res

    # función lineal
    def linear_activation(self, x):
        return np.around(x, decimals=8)

    # derivada de una función lineal
    def linear_derivative(self, x):
        res = 1
        return res
    
    def forward(self, X):
        # Propagación hacia adelante
        self.z = np.dot(X, self.W) + self.b
        self.a = self.list_functions_activations[self.hidden_functions[0]](self.z)
        return self.a
    
    def backward(self, X, y, output, learning_rate):
        # Retropropagación
        error = y - output
        delta = error * self.list_functions_derivative[self.hidden_functions[0]](output)
        
        # Actualización de pesos y sesgos
        self.W += learning_rate * np.dot(X.T, delta)
        self.b += learning_rate * np.sum(delta, axis=0, keepdims=True)
    
    def train(self, X, y, epochs, learning_rate, tol):
        try:
            list_loss = []
            list_epoch = []
            for epoch in range(epochs):
                # Propagación hacia adelante
                output = self.forward(X)
                # Retropropagación
                self.backward(X, y, output, learning_rate)
                # Calcular pérdida
                loss = np.mean(np.square(y - output))
                if epoch % 10 == 0:
                    print(f'Epoch {epoch}, Loss: {loss}')
                    list_loss.append(loss)
                    list_epoch.append(epoch)
                    if loss <= tol or np.isnan(loss):
                        return False, list_loss, list_epoch, [self.list_weights, self.list_bias], [self.W, self.b]
            return False, list_loss, list_epoch, [self.list_weights, self.list_bias], [self.W, self.b]
        except RuntimeWarning:
            print("Over here")
            return True, list_loss, list_epoch, [self.list_weights, self.list_bias], [self.W, self.b]


