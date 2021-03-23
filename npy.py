#coding:utf-8
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import tensorflow as  tf
a=tf.constant([[1.0,2.0]])#定义一个二阶张量，几个【】为几阶
b=tf.constant([[3.0],[4.0]])
y=tf.matmul(a,b)
print (y)
with tf.Session() as sess:
    print (sess.run(y))