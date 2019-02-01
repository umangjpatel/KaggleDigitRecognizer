import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

training_dataset = pd.read_csv('train.csv')
testing_dataset = pd.read_csv('test.csv')
features = training_dataset.iloc[:, 1:].values
labels = pd.get_dummies(training_dataset['label']).values
print(features.shape)
print(labels.shape)


_, axarr = plt.subplots(10,10,figsize=(10,10))
for i in range(10):
    for j in range(10):
        axarr[i,j].imshow(features[np.random.randint(features.shape[0])].reshape((28,28)))
        axarr[i,j].axis('off')

model = Sequential()
model.add(Dense(features.shape[1], input_shape=(features.shape[1],), activation='sigmoid'))
model.add(Dense(16, activation='sigmoid'))
model.add(Dense(16, activation='sigmoid'))
model.add(Dense(10, activation='sigmoid'))

model.compile(optimizer="rmsprop", loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(features, labels, batch_size=128, epochs=100, verbose=False, validation_split=.1)
loss, accuracy  = model.evaluate(features, labels, verbose=False)
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='best')
plt.show()


print("Accuracy : ", accuracy * 100)


predictions = model.predict(testing_dataset.values)
predictions = np.argmax(predictions, axis = 1)
print(predictions)

image_ids = [i + 1 for i in range(testing_dataset.shape[0])]
from collections import defaultdict
submission = defaultdict(list)
submission['ImageId'] = image_ids
submission['Label'] = predictions
submission = pd.DataFrame(data=submission)
print(submission.head())

submission.to_csv("submission.csv", index=False)
