#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
fig, axs = plt.subplots(3, 2, figsize=(10, 10))
fig.suptitle("All in One")

# First subplot
axs[0, 0].plot(y0, color='red')
axs[0, 0].set_title("y = x^3")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")  
axs[0, 0].set_xlim([0, 10])
axs[0, 0].set_ylim([0, 1000])
axs[0, 0].grid(True)
# Second subplot
axs[0, 1].scatter(x1, y1, color='magenta', s=10)
axs[0, 1].set_title("Men's Height vs Weight")
axs[0, 1].set_xlabel("Height (inches)")
axs[0, 1].set_ylabel("Weight (pounds)")
axs[0, 1].set_xlim([55, 90])
axs[0, 1].set_ylim([100, 250])
# Third subplot
axs[1, 0].plot(x2, y2, color='blue')
axs[1, 0].set_title("Exponential Decay of C-14")
axs[1, 0].set_xlabel("Time (years)")
axs[1, 0].set_ylabel("Fraction Remaining")
axs[1, 0].set_yscale('log')
axs[1, 0].set_xlim([0, 28650])
axs[1, 0].set_ylim([0.0001, 1])
# Fourth subplot
axs[1, 1].plot(x3, y31, 'r--', label='C-14 (5730 yrs)')
axs[1, 1].plot(x3, y32, 'g-', label='Ra-226 (1600 yrs)')
axs[1, 1].set_title("Exponential Decay of Radioactive Elements")
axs[1, 1].set_xlabel("Time (years)")
axs[1, 1].set_ylabel("Fraction Remaining")
axs[1, 1].set_xlim([0, 20000])
axs[1, 1].set_ylim([0, 1])
axs[1, 1].legend()
# Fifth subplot
axs[2, 0].hist(student_grades, bins=10, color='green', edgecolor='black')
axs[2, 0].set_title("Project A: Student Grades")
axs[2, 0].set_xlabel("Grades")
axs[2, 0].set_ylabel("Number of Students")
axs[2, 0].set_xlim([0, 100])
axs[2, 0].set_ylim([0, 30])
axs[2, 0].grid(axis='y')
# Hide the unused subplot
axs[2, 1].axis('off')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
