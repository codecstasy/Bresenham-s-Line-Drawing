import matplotlib.pyplot as plt
from draw_line import draw_line

# Case 1: (1, 1), (8, 4)
points_case1 = draw_line(1, 1, 8, 4)

# Plotting
x_case1, y_case1 = zip(*points_case1)

plt.plot(x_case1, y_case1, label='Case 1: (1,1), (8,4)')
plt.scatter(x_case1, y_case1, color='red')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham\'s Line Drawing Algorithm - Case 1')
plt.legend()
plt.grid(True)
plt.show()
