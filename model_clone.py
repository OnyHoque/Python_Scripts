from keras.models import clone_model

def model_cloner(model):
    model_copy = clone_model(model)
    model_copy.set_weights(model.get_weights())
    model_copy.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model_copy
