# Tensorflow

## 1. Tensorflow 模型文件

```
|--checkpoint_dir
|    |--checkpoint                  # 文本文件，记录最新的checkpoint文件及其它checkpoint文件的列表
|    |--MyModel.meta                # 保存图结构，meta文件是pb文件，包含变量、op、集合等
|    |--MyModel.data-00000-of-00001 # 二进制文件，保存了所有的 weights、biases、gradients等变量
|    |--MyModel.index               # 二进制文件和上述文件的作用相同
```

## 2. 保存 tensorflow 模型

使用 `tf.train.Saver` 保存模型，在保存变量时需要传入 session，例子：

```python
import tensorflow as tf

w1 = tf.Variable(tf.random_normal(shape=[2]), name='w1')
w2 = tf.Variable(tf.random_normal(shape=[5]), name='w2')

saver = tf.train.Saver()
saver = tf.train.Saver([w1, w2])    # 只保存一部分数据

sess = tf.Session()
sess.run(tf.global_variables_initializer())

saver.save(sess, './checkpoint_dir/MyModel')
saver.save(sess, './checkpoint_dir/MyModel',global_step=1000)   # 在 1000 次迭代后保存模型
saver.save(sess, './checkpoint_dir/MyModel',global_step=step,write_meta_graph=False)    # 只保存模型数据，不保存计算图

```

## 3. 已保存模型的加载

### 3.1 加载计算图

`saver=tf.train.import_meta_graph('./checkpoint_dir/MyModel-1000.meta')`

### 3.2 加载模型数据

```python
import tensorflow as tf
with tf.Session() as sess:
    saver = tf.train.import_meta_graph('./checkpoint_dir/MyModel-1000.meta')
    saver.restore(sess,tf.train.latest_checkpoint('./checkpoint_dir'))
    print(sess.run('w1:0'))         # 打印出加载进图的 w1 数据
```

## 参考

- https://blog.csdn.net/huachao1001/article/details/78501928