﻿import tensorflow as tf

print(tf.__version__)

h = tf.constant("Hello")
w = tf.constant(" World!")

hw = h + w

with tf.compat.v1.Session() as sess:
    ans = sess.run(hw)

print(ans)

print(hw)