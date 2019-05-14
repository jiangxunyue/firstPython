import tensorflow as tf
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data = np.float32(np.random.rand(2, 100))
y_data = np.dot([0.100, 0.200], x_data) + 0.300

# construct linear model
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 启动图 (graph)
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

class Sample:
    def __enter__(self):
        print("go in __enter__()")
        return "--Foo--"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('go in __exit__()')

def get_sample():
    return Sample()

with Sample() as sample:
    print("sample:", sample)

def h():
    print('Wen Chuan')
    m = yield 5  # Fighting!
    print(m)
    d = yield 12
    print('We are together!')
    return

# c = h()
# c.send(None)  #相当于c.send(None)
# c.send('Fighting!')  #(yield 5)表达式被赋予了'Fighting!'
# c.send(None)