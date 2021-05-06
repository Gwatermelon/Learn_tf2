#该段代码用于检验是否安装环境成功，如果运行出现tf.Tesnsor() 即代表环境安装成功
import tensorflow as tf

tensorflw_version  = tf.__version__
gpu_available = tf.test.is_gpu_available()

print("tensorflow verison:",  tensorflw_version,"\tGPU available:", gpu_available)

a = tf.constant([1.0, 2.0], name = "a")
b = tf.constant([1.0, 2.0], name = "b")
result = tf.add(a, b, name="add")
print(result)
