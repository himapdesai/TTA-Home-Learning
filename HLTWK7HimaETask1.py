import os
from sys import path
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.python.eager import def_function
from tensorflow.python.ops.gradients_util import _Inputs


print (tf.__version__)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

#opt = tf.keras.optimize.SGD(learning_rate=0.01, momentum=0.9)

#model.compile(optimizer=opt, loss='binary_crossentropy')


# Whereas if you specify the input shape, the model gets built
# continuously as you are adding layers:

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(8, input_shape=(16,)))
model.add(tf.keras.layers.Dense(4))
test = len(model.weights)
print(test) # print answer as 4

# When using the delayed-build pattern (no input shape specified), you can
# choose to manually build your model by calling
# `build(batch_input_shape)`:

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(8))
model.add(tf.keras.layers.Dense(4))
model.build((None, 16))
test = len(model.weights)
print(test) #print answer as 4


# Note that when using the delayed-build pattern (no input shape specified),
# the model gets built the first time you call `fit`, `eval`, or `predict`,
# or the first time you call the model on some input data.
x = np.random.random((2, 3))
y = np.random.randint(0, 2, (2,2))
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(8))
model.add(tf.keras.layers.Dense(1))
model.compile(optimizer='sgd', loss='mse')
model.fit(x, y, batch_size=32, epochs=10)
# model.fit(x, y)
# model.metrics_name['loss', 'mae']

from tensorflow.keras import Model
from tensorflow.keras import Input
from tensorflow.keras.layers import Dense
#define the layers
x_in = Input(shape=(8, ))
x = Dense(10)(x_in)
x_out = Dense(1)(x)
#define the model
model = Model(inputs=x_in, outputs=x_out)
print (model)


