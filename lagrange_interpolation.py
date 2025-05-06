import numpy as np
import matplotlib.pyplot as plt
import os

#using Chinese font
plt.rcParams['font.family'] = 'SimHei'

#数据点
#x从0^2到8^2
x = np.array([0,1,4,9,16,25,36,49,64])
y = np.array([0,1,2,3,4,5,6,7,8])

#拉格朗日插值多项式函数
"""
拉格朗日插值通过构造n次多项式来插值n+1个数据点
使得n次多项式全部通过n+1个数据点
"""
def lagrange_interpolation(x_data, y_data):
    #先拿到数组的大小，用于控制Ln的次数
    n = len(x_data)

    #定义一个函数，用于构造
    #传入x并返回该点处的插值结果
    def lagrange_function(x):

        #初始化x点处的插值结果result = 0
        result = 0

        #第一层控制的是Ln的n
        for i in range(n):
            #Ln的初始值为该点的y值
            Ln_value = y_data[i]

            #第二层
            for j in range(n):
                if i != j:
                    Ln_value *= (x - x_data[j]) / (x_data[i] - x_data[j])

            #将每一项的Ln加入最终结果
            result += Ln_value
        return result
    return lagrange_function #return this function so can be used later


#创建题目的L8
#L8(x)接受一个x值并返回x处的插值结果 例如L8(1)
L8 = lagrange_interpolation(x, y)

#----verify process----
save_dir = 'verify_results/lagrange'
#exist_ok=True means if this directory already exists, it will not be overwritten
os.makedirs(save_dir, exist_ok=True)

#integer in range 0-64
x_integer = np.arange(0,65)
y_lagrange = np.array([L8(x) for x in x_integer])
y_true = np.sqrt(x_integer)

#draw the plot
plt.figure(figsize=(12,6))
plt.plot(x_integer, y_lagrange, color='blue', label='拉格朗日插值')
plt.plot(x_integer, y_true, color='red', label='真实值')

plt.title('拉格朗日插值 VS 真实值')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

#save the plot
plt.savefig(os.path.join(save_dir, 'lagrange_interpolation.png'))










        


