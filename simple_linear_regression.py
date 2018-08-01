import tensorflow as tf
import numpy as np

# Model and Data
x_data = np.random.rand(100).astype(np.float32)
y_data = 30*x_data + 5
y_data = np.vectorize(lambda y: y + np.random.normal(loc=0.0, scale = 0.1))(y_data)


m = tf.Variable(30.0)
b = tf.Variable(0.0)
c = tf.Variable(0.0)
y = m*x_data + b
init = tf.global_variables_initializer()
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train_step = optimizer.minimize(loss)

with tf.Session() as sess:
	print(sess.run(init))
	for _ in range(50):
		print(sess.run([train_step, m, b, c, loss]))



