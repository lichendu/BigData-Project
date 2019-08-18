import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import sys
import urllib

print sys.version
print urllib.__version__

mnist = input_data.read_data_sets("MNIST_data_2/", one_hot=True)
print("Download Done!")

x = tf.placeholder(tf.float32, [None, 784])

# paras
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder(tf.float32, [None, 10])

# loss func
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
saver = tf.train.Saver()
# init

sess = tf.Session()
loading = False #first run False. Subsequent runs change to True. Personally I try to load and if it fails ask if it should initialise a new one.
if (loading) :
   #no need to initialise when loading. 
   save_path = "./model/minist_softmax.ckpt"
   saver.restore(sess,save_path)
else :
  init = tf.initialize_all_variables()
  sess.run(init)

# train 
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

print("Accuarcy on Test-dataset: ", sess.run(accuracy, feed_dict={x:        mnist.test.images, y_: mnist.test.labels}))

# save model 
saver = tf.train.Saver()
save_path = "./model/minist_softmax.ckpt"
saver.restore(sess, save_path)
print("Model restored.")
print(sess.run(xData))
