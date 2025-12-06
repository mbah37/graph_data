import math
import matplotlib.pyplot as plt


NUM_ROTATIONS = 15
DEGREES_PER_ROTATION = 360

degree_list = range(0, NUM_ROTATIONS * DEGREES_PER_ROTATION, 1)


SPIRAL_EXPANSION_RATE = 0.008

x_values = []
y_values = []

for degree in degree_list:
    theta = math.radians(degree)

    r = SPIRAL_EXPANSION_RATE * degree

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    x_values.append(x)
    y_values.append(y)

figure, graph = plt.subplots()
graph.plot(x_values, y_values)

graph.set_title('Spiral Function', fontsize=20)
graph.set_xlabel('Horizontal Position', fontsize=14)
graph.set_ylabel('Vertical Position', fontsize=14)
graph.tick_params(labelsize=14)

plt.show()
