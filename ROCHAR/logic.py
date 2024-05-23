
import matplotlib.pyplot as plt
import cv2
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn import preprocessing


images = []
mayus = []
mayus_ = []
minus = []
minus_ = []
num = []
num_ = []
manus = []

letters_mayus = [ "J", "G", "K", "N", "A", "E", "F", "H", "I", "L", "M", "B", "C", "D", "O", 
                 "S", "T", "V", "Y", "P", "Q", "R", "Ñ", "U", "W", "X", "Z" ]
letters_mayus_1 = [ "N", "Ñ", "M", "J", "K", "L", "G", "H", "I", "A", "F", "E", "B", "D", "C", 
                 "W", "Y", "Z", "X", "U", "V", "T", "P", "R", "Q", "O" ]
letters_mayus_2 = [ "N", "M", "K", "Ñ", "L", "A", "J", "G", "H", "I", "C", "E", "F", "B", 
                 "D", "Y", "Z", "V", "W", "Z", "U", "X", "P", "R", "S", "T", "Q", "O", "Ñ" ]
letters_mayus_3 = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                 "P", "Q", "V", "Ñ", "S", "R", "U", "Y", "T", "W", "X", "Z", "Z" ]
letters_mayus_4 = [ "A", "B", "C", "D", "E", "J", "F", "G", "H", "I", "Ñ", "O",
                 "P", "R", "Q", "S", "T", "U", "V", "W"]
letters_mayus_5 = [ "A", "L", "B", "J", "K", "M", "N", "C", "D", "E", "F", "G", "H",
                 "I", "V", "Y", "Z", "R", "S", "U", "Z", "P", "W", "X", "O", "Q", "T", "Ñ"]
letters_mayus_6 = [ "A", "B", "H", "C", "D", "E", "G", "I", "J", "F", "K", "L", "M", "N", "Ñ", "O", 
                 "P", "R", "W", "Y", "Q", "S", "T", "U", "V", "X", "Z", "Z" ]
letters_mayus_7 = [ "A", "K", "N", "B", "D", "I", "J", "M", "C", "E", "F", "G", "H", "L", 
                 "Y", "O", "T", "U", "W", "P", "R", "S", "X", "Z", "Z", "Ñ", "Q", "V" ]
letters_mayus_8 = [ "J", "L", "H", "K", "G", "I", "M", "F", "N", "A", "B", "D", "E", 
                 "C", "Q", "Y", "R", "W", "X", "Z", "Z", "O", "P", "S", "T", "U", "V", "Ñ" ]
letters_mayus_9 = [ "A", "B", "D", "G", "H", "C", "E", "F", "H", "J", "K", "L", "I", "M", "N", "U", "Y", 
                 "P", "Q", "V", "W", "X", "Ñ", "O", "R", "S", "T", "Z", "Z" ]
letters_mayus_10 = [ "H", "L", "A", "D", "G", "H", "J", "K", "M", "B", "E", "F", "I", "N", "C", "Y", 
                 "U", "X", "V", "W", "Z", "Z", "Q", "S", "P", "R", "T", "Ñ", "O" ]
letters_mayus_11 = [ "K", "A", "B", "H", "I", "J", "L", "C", "E", "G", "M", "N", "D", "F", 
                 "Z", "Z", "Y", "V", "X", "W", "T", "Q", "R", "S", "U", "O", "P" ]
letters_mayus_12 = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                 "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]
letters_mayus_13 = [ "A", "B", "K", "E", "J", "M", "C", "D", "G", "H", "I", "L",
                 "N", "F", "Q", "O", "P", "R", "W", "Ñ", "S", "T", "U", "V", "X", "Y", "Z", "Z" ]
letters_mayus_14 = [ "A", "B", "E", "F", "G", "I", "K", "N", "C", "D", "H", "J", "L", "M",
                 "S", "Y", "Z", "q", "U", "V", "Ñ", "P", "W", "X", "Z", "O", "R", "T" ]
letters_mayus_15 = [ "A", "H", "B", "F", "J", "K", "L", "M", "N", "G", "I", "C", "D", "E",
                 "W", "Y", "U", "X", "Z", "Z", "O", "P", "Q", "G", "T", "V", "R", "Ñ" ]
letters_mayus_16 = [ "A", "H", "K", "L", "N", "B", "E", "F", "I", "J", "C", "D", "G", "M",
                 "P", "X", "Y", "Z", "O", "R", "S", "W", "Z", "Q", "T", "U", "V", "Ñ" ]
letters_mayus_17 = [ "J", "A", "H", "I", "K", "N", "B", "G", "L", "M", "C", "D", "E", "F",
                 "P", "W", "Q", "R", "S", "T", "U", "X", "Y", "Z", "Ñ", "O", "V", "Z" ]

letters_minus = [ "d", "b", "h", "k", "a", "l", "c", "j", "k", "m", "e", "f", "g", "i", "n", 
                 "t", "ñ", "q", "s", "y", "o", "p", "r", "u", "v", "w", "x", "s", "z", "ñ" ]
letters_minus_1 = [ "ñ", "d", "h", "l", "k", "o", "m", "ñ", "n", "b", "k", "j", "f", "g", "e", 
                 "a", "c", "t", "y", "z", "w", "x", "r", "u", "v", "q", "p", "s" ]
letters_minus_2 = [ "l", "ñ", "b", "h", "k", "ñ", "j", "m", "n", "g", "a", "c", "e", "f", "t", 
                 "y", "z", "w", "z", "v", "x", "q", "r", "s", "u", "o", "p", "ñ" ]
letters_minus_3 = [ "d", "b", "h", "l", "j", "a", "f", "g", "k", "c", "e", "n", "m", 
                 "t", "o", "q", "r", "ñ", "p", "w", "y", "u", "v", "z", "x", "z", "s" ]
letters_minus_4 = [ "d", "b", "i", "j", "h", "a", "j", "c", "e", "f", "g", "i", 
                 "ñ", "q", "t", "o", "r", "u", "ñ", "p", "v", "w"]
letters_minus_5 = [ "d", "b", "h", "l", "e", "f", "j", "k", "g", "m", "n", "a", "c",
                 "t", "ñ", "r", "s", "u", "w", "z", "z", "v", "x", "y", "o", "q", "ñ", "p" ]
letters_minus_6 = [ "b", "d", "a", "h", "k", "c", "e", "f", "l", "g", "j", "n", "i", "m",
                 "t", "o", "q", "r", "ñ", "p", "s", "w", "v", "u", "x", "z", "y", "z" ]
letters_minus_7 = [ "d", "b", "g", "h", "k", "l", "a", "m", "c", "f", "j", "e", "i", "n",
                 "t", "y", "x", "q", "r", "s", "u", "v", "z", "w", "ñ", "o", "p", "z" ]
letters_minus_8 = [ "d", "j", "b", "h", "k", "l", "j", "f", "g", "i", "m", "n", "a", "c", "e",
                 "t", "q", "w", "z", "z", "o", "v", "x", "y", "p", "r", "s", "u", "ñ" ]
letters_minus_9 = [ "b", "d", "l", "h", "ñ", "a", "f", "g", "j", "k", "e", "i", "m", "c", "ñ",
                 "t", "y", "q", "v", "z", "z", "n", "o", "r", "s", "x", "u", "w", "p" ]
letters_minus_10 = [ "b", "l", "d", "h", "ñ", "j", "k", "m", "ñ", "a", "f", "g", "i", "e", "c",
                 "t", "y", "z", "z", "n", "q", "u", "x", "r", "s", "w", "o", "v", "p" ]
letters_minus_11 = [ "d", "b", "j", "h", "l", "n", "k", "m", "j", "e", "f", "g", "c", "a", "a",
                 "z", "z", "t", "x", "y", "w", "v", "u", "o", "q", "s", "p", "r", "ñ" ]
letters_minus_12 = [ "b", "d", "f", "h", "g", "k", "L", "e", "a", "c", "j", "m", "n", "t",
                 "s", "v", "y", "o", "p", "q", "r", "u", "x", "z", "ñ", "w", "z" ]
letters_minus_13 = [ "b", "d", "h", "l", "g", "j", "f", "k", "m", "n", "a", "c", "e", "t",
                 "w", "y", "v", "z", "z", "r", "u", "x", "o", "q", "s", "p", "ñ"]
letters_minus_14 = [ "b", "d", "h", "l", "k", "g", "j", "f", "i", "n", "m", "e", "a", "c", "t",
                 "w", "z", "x", "y", "z", "v", "u", "o", "r", "q", "ñ", "p"]
letters_minus_15 = [ "d", "b", "h", "j", "l", "g", "f", "k", "j", "n", "a", "c", "e", "i", "m",
                 "t", "s", "v", "w", "x", "y", "z", "z", "o", "u", "ñ", "q", "r", "p" ]
letters_minus_16 = [ "b", "d", "i", "h", "l", "k", "f", "g", "i", "j", "c", "e", "m", "n", "a",
                 "t", "p", "u", "q", "s", "w", "r", "v", "x", "y", "ñ", "o", "z", "z"]

numbers = [ "5", "8", "9", "2", "4", "6", "7", "1", "3", "0" ]
numbers_1 = [ "7", "9", "6", "8", "0", "5", "3", "4", "1", "2" ]
numbers_2 = [ "6", "7", "8", "9", "0", "2", "3", "5", "1", "4" ]
numbers_3 = [ "1", "4", "2", "3", "5", "9", "7", "8", "0", "6" ]
numbers_4 = [ "4", "3", "5", "6", "2", "7", "1", "8", "9", "0" ]
numbers_5 = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" ]
numbers_6 = [ "5", "3", "4", "6", "7", "9", "0", "1", "2", "8" ]
numbers_7 = [ "0", "4", "5", "6", "8", "9", "1", "7", "2", "3" ]
numbers_8 = [ "7", "9", "6", "8", "0", "3", "5", "1", "4", "2" ]
numbers_9 = [ "9", "6", "7", "8", "0", "5", "3", "4", "1", "2" ]
numbers_10 = [ "9", "8", "4", "5", "6", "7", "0", "3", "2", "1" ]
numbers_11 = [ "3", "4", "6", "6", "7", "8", "9", "0", "1", "2" ]
numbers_12 = [ "5", "6", "7", "9", "8", "0", "3", "4", "1", "2" ]
numbers_13 = [ "3", "5", "6", "1", "2", "4", "7", "8", "9", "0" ]
numbers_14 = [ "5", "0", "6", "8", "9", "1", "3", "7", "2", "4" ]
numbers_15 = [ "0", "6", "8", "9", "1", "7", "5", "2", "3", "4" ]

letters = []
letters_ = []
X_train = 0
X_test = 0
y_train = 0
y_test = 0

# mlp = Perceptron(random_state=5)
# mlp = MLPClassifier(random_state=15, learning_rate='invscaling', 
#                     hidden_layer_sizes=(950, 950, 950,), activation='logistic', max_iter=1000)

mlp = MLPClassifier(random_state=1, 
                    learning_rate='invscaling', 
                    hidden_layer_sizes=(850, 850, 850), 
                    activation='logistic', max_iter=1000)


norm_img = np.zeros((300, 300))

textPredicted = []


def import_images(path, w, h):
    imgs_ = cv2.imread(f"images/{path}")
    imgs_ = cv2.normalize(imgs_, norm_img, 0, 255, cv2.NORM_MINMAX)
    imgs_ = cv2.cvtColor(imgs_, cv2.COLOR_BGR2GRAY)
    imgs_ = cv2.resize(imgs_, (w, h))
    return imgs_


def show_img(index):
    plt.matshow(letters_[index].reshape(40,40), cmap=plt.cm.gray)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def load_images_letters(imagens, pixs):   
    mascaras = []
    umbral, imagenMetodo = cv2.threshold(imagens, 0, 255, cv2.THRESH_OTSU)
    mascara = np.uint8((imagens < umbral) * 255)
    # Extraemos el numero de elementos de la imagen
    num_labels, labels, stats, centroides = cv2.connectedComponentsWithStats(mascara, 4, cv2.CV_32S)
    valor_max_pix = (np.max(stats[:,4][1:])) / pixs
    for i in range(0, len(stats)):
        if(stats[i][4] > valor_max_pix):
            p1 = int(stats[i][0])
            p2 = int(stats[i][1])
            mask = mascara[p2 - 10: p2 + 30, p1 - 10: p1 + 30]
            mask = mask.flatten() 
            mascaras.append(mask)
    return mascaras


def dataset_letters(imagen_mayus, pixs, r_imsp, r_imsn, letters_mays, mayus, mayus_):
    mayus = []
    mayus_.clear()
    mayus = load_images_letters(imagen_mayus, pixs)
    for i in range(r_imsp, len(mayus) - r_imsn):
        mayus_.append(mayus[i])
    for i in range(0, len(mayus_)):
        letters_.append(mayus_[i])
        letters.append(letters_mays[i])


def create_dataset(letters_, letters):

    img_may = import_images("MAYUS/mayus.jpg", 827, 116)
    dataset_letters(img_may, 4, 1, 0, letters_mayus, mayus, mayus_)
    img_may_1 = import_images("MAYUS/mayus_1.jpg", 827, 116)
    dataset_letters(img_may_1, 25, 2, 1, letters_mayus_1, mayus, mayus_)
    img_may_2 = import_images("MAYUS/mayus_2.jpg", 827, 116)
    dataset_letters(img_may_2, 3, 1, 0, letters_mayus_2, mayus, mayus_)
    img_may_3 = import_images("MAYUS/mayus_4.jpg", 827, 116)
    dataset_letters(img_may_3, 3, 1, 0, letters_mayus_3, mayus, mayus_)
    img_may_4 = import_images("MAYUS/mayus_3.jpg", 827, 116)
    dataset_letters(img_may_4, 7, 1, 0, letters_mayus_4, mayus, mayus_)
    img_may_5 = import_images("MAYUS/mayus_5.jpg", 827, 116)
    dataset_letters(img_may_5, 3, 1, 0, letters_mayus_5, mayus, mayus_)
    img_may_6 = import_images("MAYUS/mayus_6.jpg", 827, 116)
    dataset_letters(img_may_6, 5, 1, 0, letters_mayus_6, mayus, mayus_)
    img_may_7 = import_images("MAYUS/mayus_7.jpg", 827, 116)
    dataset_letters(img_may_7, 5, 1, 0, letters_mayus_7, mayus, mayus_)
    img_may_8 = import_images("MAYUS/mayus_8.jpg", 827, 116)
    dataset_letters(img_may_8, 5, 1, 0, letters_mayus_8, mayus, mayus_)
    img_may_9 = import_images("MAYUS/mayus_9.jpg", 827, 116)
    dataset_letters(img_may_9, 5, 1, 0, letters_mayus_9, mayus, mayus_)
    img_may_10 = import_images("MAYUS/mayus_10.jpg", 827, 116)
    dataset_letters(img_may_10, 5, 1, 0, letters_mayus_10, mayus, mayus_)
    img_may_11 = import_images("MAYUS/mayus_11.jpg", 827, 116)
    dataset_letters(img_may_11, 5, 1, 1, letters_mayus_11, mayus, mayus_)
    train_mayus()
    img_may_13 = import_images("MAYUS/mayus_13.jpg", 827, 116)
    dataset_letters(img_may_13, 5, 1, 1, letters_mayus_13, mayus, mayus_)
    img_may_14 = import_images("MAYUS/mayus_14.jpg", 827, 116)
    dataset_letters(img_may_14, 5, 1, 1, letters_mayus_14, mayus, mayus_)
    img_may_15 = import_images("MAYUS/mayus_15.jpg", 827, 116)
    dataset_letters(img_may_15, 5, 1, 1, letters_mayus_15, mayus, mayus_)
    img_may_16 = import_images("MAYUS/mayus_16.jpg", 827, 116)
    dataset_letters(img_may_16, 5, 1, 1, letters_mayus_16, mayus, mayus_)
    img_may_17 = import_images("MAYUS/mayus_17.jpg", 827, 116)
    dataset_letters(img_may_17, 5, 1, 1, letters_mayus_17, mayus, mayus_)

    # img_min = import_images("MINUS/minus.jpg", 829, 128)
    # dataset_letters(img_min, 7, 1, 0, letters_minus, minus, minus_)
    # img_min_1 = import_images("MINUS/minus_1.jpg", 829, 128)
    # dataset_letters(img_min_1, 6, 1, 0, letters_minus_1, minus, minus_)
    # img_min_2 = import_images("MINUS/minus_2.jpg", 829, 128)
    # dataset_letters(img_min_2, 4, 2, 0, letters_minus_2, minus, minus_)
    # img_min_3 = import_images("MINUS/minus_4.jpg", 829, 128)
    # dataset_letters(img_min_3, 4, 2, 0, letters_minus_3, minus, minus_)
    # img_min_4 = import_images("MINUS/minus_3.jpg", 829, 128)
    # dataset_letters(img_min_4, 4, 1, 0, letters_minus_4, minus, minus_)
    # img_min_5 = import_images("MINUS/minus_5.jpg", 829, 128)
    # dataset_letters(img_min_5, 5, 1, 0, letters_minus_5, minus, minus_)
    # img_min_6 = import_images("MINUS/minus_6.jpg", 829, 128)
    # dataset_letters(img_min_6, 5, 1, 0, letters_minus_6, minus, minus_)
    # img_min_7 = import_images("MINUS/minus_7.jpg", 829, 128)
    # dataset_letters(img_min_7, 5, 1, 0, letters_minus_7, minus, minus_)
    # img_min_8 = import_images("MINUS/minus_8.jpg", 829, 128)
    # dataset_letters(img_min_8, 5, 1, 0, letters_minus_8, minus, minus_)
    # img_min_9 = import_images("MINUS/minus_9.jpg", 829, 128)
    # dataset_letters(img_min_9, 5, 1, 0, letters_minus_9, minus, minus_)
    # img_min_10 = import_images("MINUS/minus_10.jpg", 829, 128)
    # dataset_letters(img_min_10, 5, 1, 0, letters_minus_10, minus, minus_)
    # img_min_11 = import_images("MINUS/minus_11.jpg", 829, 128)
    # dataset_letters(img_min_11, 6, 1, 0, letters_minus_11, minus, minus_)
    # img_min_12 = import_images("MINUS/minus_12.jpg", 829, 128)
    # dataset_letters(img_min_12, 5, 1, 0, letters_minus_12, minus, minus_)
    # img_min_13 = import_images("MINUS/minus_13.jpg", 829, 128)
    # dataset_letters(img_min_13, 5, 1, 0, letters_minus_13, minus, minus_)
    # img_min_14 = import_images("MINUS/minus_14.jpg", 829, 128)
    # dataset_letters(img_min_14, 5, 1, 0, letters_minus_14, minus, minus_)
    # img_min_15 = import_images("MINUS/minus_15.jpg", 829, 128)
    # dataset_letters(img_min_15, 5, 1, 0, letters_minus_15, minus, minus_)
    # img_min_16 = import_images("MINUS/minus_16.jpg", 829, 128)
    # dataset_letters(img_min_16, 5, 1, 0, letters_minus_16, minus, minus_)

    # img_num = import_images("NUM/num.jpg", 591, 61)
    # dataset_letters(img_num, 5, 1, 0, numbers, num, num_)
    # img_num_1 = import_images("NUM/num_1.jpg", 591, 61)
    # dataset_letters(img_num_1, 5, 1, 0, numbers_1, num, num_)
    # img_num_2 = import_images("NUM/num_2.jpg", 591, 61)
    # dataset_letters(img_num_2, 2, 1, 0, numbers_2, num, num_)
    # img_num_3 = import_images("NUM/num_3.jpg", 591, 61)
    # dataset_letters(img_num_3, 5, 1, 0, numbers_3, num, num_)
    # img_num_4 = import_images("NUM/num_4.jpg", 591, 61)
    # dataset_letters(img_num_4, 3, 1, 0, numbers_4, num, num_)
    # img_num_5 = import_images("NUM/num_5.jpg", 591, 61)
    # dataset_letters(img_num_5, 2, 1, 0, numbers_5, num, num_)
    # img_num_6 = import_images("NUM/num_6.jpg", 591, 61)
    # dataset_letters(img_num_6, 3, 1, 0, numbers_6, num, num_)
    # img_num_7 = import_images("NUM/num_7.jpg", 591, 61)
    # dataset_letters(img_num_7, 3, 1, 0, numbers_7, num, num_)
    # img_num_8 = import_images("NUM/num_8.jpg", 591, 61)
    # dataset_letters(img_num_8, 3, 1, 0, numbers_8, num, num_)
    # img_num_9 = import_images("NUM/num_9.jpg", 591, 61)
    # dataset_letters(img_num_9, 3, 1, 0, numbers_9, num, num_)
    # img_num_10 = import_images("NUM/num_10.jpg", 591, 61)
    # dataset_letters(img_num_10, 5, 1, 0, numbers_10, num, num_)
    # img_num_11 = import_images("NUM/num_11.jpg", 591, 61)
    # dataset_letters(img_num_11, 3, 1, 0, numbers_11, num, num_)
    # img_num_12 = import_images("NUM/num_12.jpg", 591, 61)
    # dataset_letters(img_num_12, 3, 1, 0, numbers_12, num, num_)
    # img_num_13 = import_images("NUM/num_13.jpg", 591, 61)
    # dataset_letters(img_num_13, 3, 1, 0, numbers_13, num, num_)
    # img_num_14 = import_images("NUM/num_14.jpg", 591, 61)
    # dataset_letters(img_num_14, 3, 1, 0, numbers_14, num, num_)
    # img_num_15 = import_images("NUM/num_15.jpg", 591, 61)
    # dataset_letters(img_num_15, 3, 1, 0, numbers_15, num, num_)

    letters_ = np.array(letters_)
    letters = np.array(letters)


def train_model():
    X_train, X_test, y_train, y_test = train_test_split(letters_, letters, random_state=1, test_size=0.25)
    mlp.fit(X_train, y_train)
    return round(mlp.score(X_test, y_test), 2)


def predict(X):
    y = mlp.predict(X)
    return y[0]


def charge_mayus():
    images = []
    for i in range(1, 28):
        img = cv2.imread(f"images/LETRAS/L{i}.jpg")
        width = 40
        height = 40
        img = cv2.resize(img, (width, height))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        umbral, imagenMetodo = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
        mascara = np.uint8((img < umbral) * 255)
        mascara = mascara.flatten()
        images.append(mascara)
    return images


def train_mayus():
    mm_yus = charge_mayus()
    for i in range(0, len(mm_yus)):
        letters_.append(mm_yus[i])
        letters.append(letters_mayus_12[i])


def load_letter(img_letter):
    width = 40
    height = 40
    img = cv2.imread(img_letter)
    img = cv2.resize(img, (width, height))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    umbral, imagenMetodo = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    mascara = np.uint8((img < umbral) * 255)
    mascara = mascara.flatten()
    y = predict([mascara])
    return y


def load_manuscrito(manuscrito):   
    textPredicted = []
    imagens = cv2.imread(manuscrito)
    imagens = cv2.normalize(imagens, norm_img, 0, 255, cv2.NORM_MINMAX)
    imagens = cv2.cvtColor(imagens, cv2.COLOR_BGR2GRAY)
    mascaras = []
    umbral, imagenMetodo = cv2.threshold(imagens, 0, 255, cv2.THRESH_OTSU)
    mascara = np.uint8((imagens < umbral) * 255)
    # Extraemos el numero de elementos de la imagen
    num_labels, labels, stats, centroides = cv2.connectedComponentsWithStats(mascara, 4, cv2.CV_32S)
    valor_max_pix = (np.max(stats[:,4][1:])) / 9
    for i in range(0, len(stats)):
        if(stats[i][4] > valor_max_pix):
            p1 = int(stats[i][0])
            p2 = int(stats[i][1])
            mask = i == labels
            mask = mask[p2 - 10: p2 + 30, p1 - 10: p1 + 30]
            mask = mask.flatten() 
            mascaras.append(mask)
    for i in range(1, len(mascaras)):
        y = predict([mascaras[i]])
        textPredicted.append(y)
    return textPredicted


def reconstruct(noisy_pattern):
    network = HopfieldNetwork(len(letters_[0]))
    network.train(letters_)
    plt.matshow(noisy_pattern.reshape(40, 40), cmap=plt.cm.gray)
    plt.xticks(())
    plt.yticks(())
    plt.show()
    retrieved_pattern = network.predict(noisy_pattern)
    plt.matshow(retrieved_pattern.reshape(40, 40), cmap=plt.cm.gray)
    plt.xticks(())
    plt.yticks(())
    plt.show()
    return retrieved_pattern


class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        num_patterns = len(patterns)
        for pattern in patterns:
            pattern = np.array(pattern)
            self.weights += np.outer(pattern, pattern)
        self.weights /= num_patterns
        np.fill_diagonal(self.weights, 0)

    def predict(self, input_pattern, max_iterations=100):
        input_pattern = np.array(input_pattern)
        for _ in range(max_iterations):
            old_pattern = np.copy(input_pattern)
            activations = np.dot(self.weights, input_pattern)
            input_pattern = np.sign(activations)
            if np.array_equal(input_pattern, old_pattern):
                break
        return input_pattern
    





