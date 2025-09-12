from sklearn.model_selection import train_test_split
import numpy as np

x = np.random.randint(0, 10, 100) # data, x
y = np.random.randint(0, 2, 100) # label, 정답지, target

x_train, x_test, y_train, y_test = train_test_split(x,
                                                   y,
                                                   test_size = 0.2,
                                                   random_state = 2025)

print(x_train[:5], x_test[:5])
print(y_train[:5], y_test[:5])
print(len(x_train), len(x_test))
print(len(y_train), len(y_test))