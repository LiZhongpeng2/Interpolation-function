import numpy as np
import matplotlib.pyplot as plt
import os

#using Chinese font
plt.rcParams['font.family'] = 'SimHei'

#data points
#x from 0^2 to 8^2
x = np.array([0,1,4,9,16,25,36,49,64])
y = np.array([0,1,2,3,4,5,6,7,8])

#Lagrange interpolation polynomial function
"""
Lagrange interpolation constructs an nth-degree polynomial
to interpolate n+1 data points,
ensuring that the polynomial passes through all n+1 points.
"""
def lagrange_interpolation(x_data, y_data):
    #the size of x_data's length -> used to determine the degree of the polynomial
    n = len(x_data)

    #function, used to construct the Lagrange interpolation polynomial
    #传入x并返回该点处的插值结果
    def lagrange_function(x):

        #initialize the result of the interpolation at x
        result = 0

        #the outer loop controls the n of Ln
        for i in range(n):
            #Ln's initial value is the y value of the i-th point
            Ln_value = y_data[i]

            #the inner loop controls the j of Ln
            for j in range(n):
                if i != j:
                    Ln_value *= (x - x_data[j]) / (x_data[i] - x_data[j])

            #add each Ln to the final result
            result += Ln_value
        return result
    return lagrange_function #return this function so can be used later


#create the L8 function
#L8(x) accepts an x value and returns the interpolation result at x, e.g. L8(1)
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

plt.title('[0-64]区间 拉格朗日插值 VS 真实值')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

#save the plot
plt.savefig(os.path.join(save_dir, 'lagrange_interpolation_0_64.png'))

#----range in [0,1]----
x_range_0_1 = np.arange(0,1,0.01)
y_lagrange_0_1 = np.array([L8(x) for x in x_range_0_1])
y_true_0_1 = np.sqrt(x_range_0_1)

#result visualization
plt.figure(figsize=(12,6))
plt.plot(x_range_0_1, y_lagrange_0_1, color='blue', label='拉格朗日插值')
plt.plot(x_range_0_1, y_true_0_1, color='red', label='真实值')

plt.title('[0-1]区间 拉格朗日插值 VS 真实值')
#show the legend（legend:图例）
plt.legend()

#save the plot
plt.savefig(os.path.join(save_dir, 'lagrange_interpolation_0_1.png'))
















        


