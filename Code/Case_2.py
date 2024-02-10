import matplotlib.pyplot as plt
from draw_line import draw_line

# Case 2: (1, 1), (4, 8)
points_case2 = draw_line(1, 1, 4, 8)

# Plotting
x_case2, y_case2 = zip(*points_case2)

plt.plot(x_case2, y_case2, label='Case 2: (1,1), (4,8)')
plt.scatter(x_case2, y_case2, color='blue')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Bresenham\'s Line Drawing Algorithm - Case 2')
plt.legend()
plt.grid(True)
plt.show()
