from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.optimizers import SGD
import mlflow
import mlflow.keras
from mlflow.models.signature import infer_signature

if __name__ == "__main__":
    # mlflow.set_tracking_uri("http://43.143.136.241:10003")
    # mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_tracking_uri("http://10.3.74.221:5000")
    (train_X, train_Y), (test_X, test_Y) = mnist.load_data()
    trainX = train_X.reshape((train_X.shape[0], 28, 28, 1))
    testX = test_X.reshape((test_X.shape[0], 28, 28, 1))
    trainY = to_categorical(train_Y)
    testY = to_categorical(test_Y)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(100, activation='relu', kernel_initializer='he_uniform'))
    model.add(Dense(10, activation='softmax'))
    opt = SGD(lr=0.01, momentum=0.9)
    model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(trainX, trainY, epochs=10, batch_size=32, validation_data=(testX, testY))

    signature = infer_signature(testX, model.predict(testX))
    mlflow.keras.log_model(model, "mnist_cnn", signature=signature)
