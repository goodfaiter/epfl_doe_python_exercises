import numpy as np
import scipy

x = np.array([[1, -1, -1, -1, -1, -1],
              [1, 1, -1, -1, -1, -1],
              [1, -1, 1, -1, -1, -1],
              [1, -1, -1, 1, -1, -1],
              [1, -1, -1, -1, 1, -1],
              [1, -1, -1, -1, -1, 1]])

disp = np.linalg.inv(x.T @ x)
print("First run, all the factors at the minimum and then for each factor, one factor at the maximum, the other ones at the minimum (6 runs)")
print(disp)
print(disp.trace())

x = np.array([[1, 1, 1, 1, 1, 1],
              [1, 1, -1, -1, -1, -1],
              [1, -1, 1, -1, -1, -1],
              [1, -1, -1, 1, -1, -1],
              [1, -1, -1, -1, 1, -1],
              [1, -1, -1, -1, -1, 1]])

disp = np.linalg.inv(x.T @ x)
print("First run, all the factors at the maximum and then for each factor, one factor at the maximum, the other ones at the minimum (6 runs)")
print(disp)
print(disp.trace())

x = np.array([[1, -1, -1, -1, -1, -1],
              [1, 1, 1, -1, -1, -1],
              [1, -1, 1, 1, -1, -1],
              [1, -1, -1, 1, 1, -1],
              [1, -1, -1, -1, 1, 1],
              [1, 1, -1, -1, -1, 1]])

disp = np.linalg.inv(x.T @ x)
print("First run, all the factors at the minimum and then, two by two, two factors at the maximum, the other ones at the minimum (6 runs)")
print(disp)
print(disp.trace())

x = scipy.linalg.hadamard(8)
disp = np.linalg.inv(x.T @ x)
print("The factors are varied using 5 columns (2 to 6), the first column is filled with ’1’, which is the HADAMARD design obtained with the command")
print(disp)
print(disp.trace())