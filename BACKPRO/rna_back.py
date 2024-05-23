import numpy as np


class NeuralNetwork:
    def __init__(self, input_size, hidden_layers, hidden_functions, output_size):
        self.input_size = input_size
        self.hidden_layers = hidden_layers
        self.hidden_functions = hidden_functions
        self.output_size = output_size

        self.list_functions_activations = [self.sigmoid, self.tanh_activation, self.sin_activation, self.linear_activation]
        self.list_functions_derivative = [self.sigmoid_derivative, self.tanh_derivative, self.sin_derivative, self.linear_derivative]
        
        # Inicialización de los pesos y sesgos de las capas
        self.weights_input_hidden = np.round(np.random.randn(self.input_size, self.hidden_layers[0]), decimals=5)
        self.bias_input_hidden = np.round(np.random.randn(1, self.hidden_layers[0]), decimals=5)
        self.weights_hiddens = [np.round(np.random.randn(self.hidden_layers[i], self.hidden_layers[i+1]), decimals=5) for i in range(len(self.hidden_layers) - 1)]
        self.bias_hiddens = [np.round(np.random.randn(1, self.hidden_layers[i+1]), decimals=5) for i in range(len(self.hidden_layers) - 1)]        
        self.weights_hidden_output = np.round(np.random.randn(self.hidden_layers[-1], self.output_size), decimals=5)
        self.bias_hidden_output = np.round(np.random.randn(1, self.output_size), decimals=5)

        self.list_weights_input_hidden = [np.copy(arr) for arr in self.weights_input_hidden]
        self.list_bias_input_hidden = [np.copy(arr) for arr in self.bias_input_hidden]
        self.list_weights_hiddens = [np.copy(arr) for arr in self.weights_hiddens]
        self.list_bias_hiddens = [np.copy(arr) for arr in self.bias_hiddens]
        self.list_weights_hidden_output = [np.copy(arr) for arr in self.weights_hidden_output]
        self.list_bias_hidden_output = [np.copy(arr) for arr in self.bias_hidden_output]

    # función sigmoide
    def sigmoid(self, x):
        x_ = np.around(x, decimals=10)
        res = np.around(1 / (1 + np.around(np.exp(-x_), decimals=10)), decimals=10)
        return res

    # derivada de la función sigmoide
    def sigmoid_derivative(self, x):
        x_ = np.around(x, decimals=10)
        res = np.around(x_ * (1 - x), decimals=10)
        return res

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
        self.layer_outputs = []
        hidden_output = np.around(self.list_functions_activations[self.hidden_functions[0]](np.dot(X, self.weights_input_hidden) + self.bias_input_hidden), decimals=8)
        self.layer_outputs.append(hidden_output)
        for i in range(len(self.hidden_layers) - 1):
            hidden_output = np.around(self.list_functions_activations[self.hidden_functions[i+1]](np.dot(hidden_output, self.weights_hiddens[i]) + self.bias_hiddens[i]), decimals=8)
            self.layer_outputs.append(hidden_output)
        if self.hidden_functions[-1] == 3:
            self.output = np.around(np.dot(self.layer_outputs[-1], self.weights_hidden_output) + self.bias_hidden_output, decimals=8)
        else:
            self.output = np.around(self.list_functions_activations[self.hidden_functions[-1]](np.dot(self.layer_outputs[-1], self.weights_hidden_output) + self.bias_hidden_output), decimals=8)
        return self.output

    def backward(self, X, y, learning_rate):
        # Retropropagación
        errors_hidden = []
        deltas_hidden = []
        # Cálculo del error en la capa de salida
        output_error = y - self.output
        if self.hidden_functions[-1] == 3:
            output_delta = np.around(output_error, decimals=8) 
        else:
            output_delta = np.around(output_error * self.list_functions_derivative[self.hidden_functions[-1]](self.output), decimals=8)
        # Retropropagación de los errores
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = np.around(hidden_error * self.list_functions_derivative[self.hidden_functions[-2]](self.layer_outputs[-1]), decimals=8)
        errors_hidden.append(hidden_error)
        deltas_hidden.append(hidden_delta)
        for i in range(len(self.hidden_layers)-1):
            hidden_error = errors_hidden[i].dot(self.weights_hiddens[-(i+1)].T)
            hidden_delta = np.around(hidden_error * self.list_functions_derivative[self.hidden_functions[-(i+3)]](self.layer_outputs[-(i+2)]), decimals=8)
            errors_hidden.append(hidden_error)
            deltas_hidden.append(hidden_delta)
        # Actualización de pesos y sesgos
        self.weights_hidden_output += self.layer_outputs[-1].T.dot(output_delta) * learning_rate
        self.bias_hidden_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        for i in range(len(self.hidden_layers)-1):
            self.weights_hiddens[-(i+1)] += self.layer_outputs[-(i+2)].T.dot(deltas_hidden[i]) * learning_rate
            self.bias_hiddens[-(i+1)] += np.sum(deltas_hidden[i], axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += X.T.dot(deltas_hidden[-1]) * learning_rate
        self.bias_input_hidden += np.sum(deltas_hidden[-1], axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs, learning_rate, tol):
        list_loss = []
        list_epoch = []
        for epoch in range(epochs):
            # Propagación hacia adelante
            output = self.forward(X)
            # Retropropagación
            self.backward(X, y, learning_rate)
            # Calcular la pérdida
            loss = np.around(np.mean(np.square(y - output)), decimals=8)
            if epoch % 10 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')
                list_loss.append(loss)
                list_epoch.append(epoch)
                if loss <= tol:
                    return False, list_loss, list_epoch, [self.list_weights_input_hidden, self.list_bias_input_hidden], [self.list_weights_hiddens, self.list_bias_hiddens], [self.list_weights_hidden_output, self.list_bias_hidden_output], [self.weights_input_hidden, self.bias_input_hidden], [self.weights_hiddens, self.bias_hiddens], [self.weights_hidden_output, self.bias_hidden_output]
                if np.isnan(loss):
                    return True, list_loss, list_epoch, [self.list_weights_input_hidden, self.list_bias_input_hidden], [self.list_weights_hiddens, self.list_bias_hiddens], [self.list_weights_hidden_output, self.list_bias_hidden_output], [self.weights_input_hidden, self.bias_input_hidden], [self.weights_hiddens, self.bias_hiddens], [self.weights_hidden_output, self.bias_hidden_output]
        return False, list_loss, list_epoch, [self.list_weights_input_hidden, self.list_bias_input_hidden], [self.list_weights_hiddens, self.list_bias_hiddens], [self.list_weights_hidden_output, self.list_bias_hidden_output], [self.weights_input_hidden, self.bias_input_hidden], [self.weights_hiddens, self.bias_hiddens], [self.weights_hidden_output, self.bias_hidden_output]