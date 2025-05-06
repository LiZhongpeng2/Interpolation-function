import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import os

"""
Cubic spline interpolation properties:
# 1. The curve passes through all given data points
# 2. The adjacent polynomials are continuous at the connecting points (smooth curve)
# 3. The adjacent polynomials are continuous at the connecting points (continuous curvature change)
"""

#using Chinese font
plt.rcParams['font.family'] = 'SimHei'

x_data = np.array([0,1,4,9,16,25,36,49,64])
y_data = np.array([0,1,2,3,4,5,6,7,8])

# create the cubic spline interpolation function S(x)
# CubicSpline will construct a cubic polynomial between each two data points
# - bc_type='natural': specify the boundary condition type, 'natural' means the second derivative is 0 at the boundary
S = CubicSpline(x_data, y_data, bc_type='natural')

x_plot = np.linspace(0, 64, 1000)
#S is a callable object, accepts an x value and returns the corresponding interpolation result
y_plot = S(x_plot)
y_true = np.sqrt(x_plot)

#create the directory to save the plot
save_dir = 'verify_results/CubicSpline'
os.makedirs(save_dir, exist_ok=True)

plt.figure(figsize=(12, 6))
plt.plot(x_plot, y_plot, color='blue', label='三次样条插值')
plt.plot(x_plot, y_true, color='red', label='真实值')

plt.title('[0-64]区间 三次样条插值 VS 真实值')
plt.legend()

#save the plot
plt.savefig(os.path.join(save_dir, 'CubicSpline_0_64.png'))

#----range in [0,1]----
x_range_0_1 = np.linspace(0, 1, 1000)
y_plot_0_1 = S(x_range_0_1)
y_true_0_1 = np.sqrt(x_range_0_1)

plt.figure(figsize=(12, 6))
plt.plot(x_range_0_1, y_plot_0_1, color='blue', label='三次样条插值')
plt.plot(x_range_0_1, y_true_0_1, color='red', label='真实值')

plt.title('[0-1]区间 三次样条插值 VS 真实值')
plt.legend()

#save the plot
plt.savefig(os.path.join(save_dir, 'CubicSpline_0_1.png'))




