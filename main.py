import tensorflow as tf

with tf.compat.v1.Session() as sess:
    message = tf.constant('Welcome to the exciting world of Deep Neural Networks!')
    print(sess.run(message))
