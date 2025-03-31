import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv("fashion-mnist_train.csv")
X = data.iloc[:, 1:].values / 255.0
Y = data.iloc[:, 0].values
X = X.reshape(-1, 28, 28, 1)
X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size=0.2, random_state=42)
print(f"Train X,y: {X_train.shape}, {y_train.shape} | Test X,y: {X_val.shape}, {y_val.shape}")

test_data = pd.read_csv("fashion-mnist_test.csv")
X_test = test_data.iloc[:, 1:].values / 255.0
y_test = test_data.iloc[:, 0].values
X_test = X_test.reshape(-1, 28, 28, 1)


model = keras.Sequential([
    keras.layers.Input((28, 28, 1)),

    keras.layers.Conv2D(64, (3,3), activation='relu', padding='same'),
    keras.layers.Conv2D(64, (3,3), activation='relu', padding='same'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.BatchNormalization(),

    keras.layers.Conv2D(128, (3,3), activation='relu', padding='same'),
    keras.layers.Conv2D(128, (3,3), activation='relu', padding='same'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.BatchNormalization(),

    keras.layers.Conv2D(256, (3,3), activation='relu', padding='same'),
    keras.layers.Conv2D(256, (3,3), activation='relu', padding='same'),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.BatchNormalization(),

    keras.layers.Flatten(),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_val, y_val))

Y_pred = np.argmax(model.predict(X_test), axis=1)
accuracy = accuracy_score(y_test, Y_pred),
precision = precision_score(y_test, Y_pred, average='macro'),
recall = recall_score(y_test, Y_pred, average='macro')

print(f"Accuracy : {accuracy} \nPrecision : {precision} \nRecall : {recall}")
