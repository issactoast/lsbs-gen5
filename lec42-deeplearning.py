# pip install tensorflow
# pip intall keras
# import keras
# print(keras.__version__)

from tensorflow import keras
from tensorflow.keras import layers
# 선형 유닛 네트워크 생성
model = keras.Sequential([
    layers.Dense(units=2, input_shape=[3])
])

model.weights

model.summary()

# YOUR CODE HERE
w, b = model.weights

print("Weights\n{}\n\nBias\n{}".format(w, b))

import tensorflow as tf
x = tf.linspace(-1.0, 1.0, 3)      # (3,)
x = tf.reshape(x, (1, 3))          
y = model.predict(x)
y
# y = -0.13701558


import numpy as np
w = np.array([1.0793215, -0.32281893, 0.9423059])
b = np.array([0.0])

x = np.linspace(-1.0, 1.0, 3)
x

np.sum(w * x) + b


model = keras.Sequential([
    # 은닉층 (ReLU 활성화 함수 사용)
    layers.Dense(units=4, activation='relu', input_shape=[2]),
    layers.Dense(units=3, activation='relu'),
    # 출력층 (선형 활성화)
    layers.Dense(units=1),
])


import tensorflow as tf
x = tf.linspace(0.0, 1.0, 2)
x = tf.reshape(x, (1, 2))  
y = model.predict(x)
y

model.compile(
    optimizer="adam",
    loss="mae",
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=10,
)






import numpy as np

def f(x):
    return (x - 1)**2 + 3

def df(x):
    return 2*(x - 1)

# 하이퍼파라미터
alpha = 0.02      # 학습률(스텝 사이즈)
x = 5.0           # 시작점
tol = 1e-8        # 기울기 절댓값 기준
max_iters = 5000  # 최대 반복

history = []      # 진행 기록 (스텝, x, f(x), grad)

for k in range(max_iters):
    g = df(x)
    history.append((k, x, f(x), g))
    if abs(g) < tol:
        break
    x = x - alpha * g

print(f"반복 횟수: {k}")
print(f"추정 최소점 x*: {x:.12f}")
print(f"f(x*): {f(x):.12f}")
print(f"기울기: {df(x):.3e}")

# 필요하면 진행 기록 확인
# for row in history[:5] + history[-5:]:
#     print(row)
