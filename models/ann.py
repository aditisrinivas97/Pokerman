'''
ANN with back-propagation.
'''

# -------------------- Imports -------------------- #
from keras.models import Sequential
from keras.layers import Dense

from pokerman_common import *


# -------------------- Model -------------------- #
model = Sequential()

# Input layer
model.add(Dense(config.features, input_dim = train_x.shape[1], activation='relu'))

# Hidden layers
model.add(Dense(config.features//2 , activation='relu'))
model.add(Dense(config.features//2 , activation='relu'))

# Output layer
model.add(Dense(1, activation='softmax'))


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_x, train_y, epochs = 5000, batch_size = 500)

scores = model.evaluate(train_x, train_y)
print("Train =", model.metrics_names[1], scores[1] * 100)

scores = model.evaluate(test_x, test_y)
print("Test =", model.metrics_names[1], scores[1] * 100)