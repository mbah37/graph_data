import math
import matplotlib.pyplot as plt

# Number of full rotations the spiral will complete
NUM_ROTATIONS = 15

# Each rotation consists of 360 degrees
DEGREES_PER_ROTATION = 360

# Creates a list of degree values from 0 up to (NUM_ROTATIONS * 360)
degree_list = range(0, NUM_ROTATIONS * DEGREES_PER_ROTATION)


# Controls how quickly the spiral expands outward from the center
SPIRAL_EXPANSION_RATE = 0.008

# Lists to store computed x and y coordinate values
x_values = []
y_values = []

# Loop over each degree and calculate its x/y position
for degree in degree_list:
    # Convert degrees to radians
    theta = math.radians(degree)

    # radius is the distance from center/origin
    radius = SPIRAL_EXPANSION_RATE * degree

    # Convert from polar (radius,θ) to Cartesian
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)

    # Save point coordinates
    x_values.append(x)
    y_values.append(y)

#background for the graph
plt.style.use('seaborn-v0_8')

# Create a figure and axes object
figure, graph = plt.subplots()

# Scatter plot using degree_list for color mapping
graph.scatter(x_values, y_values, s=10 ,c=degree_list, cmap=plt.cm.viridis)

# Customize labels and appearance
graph.set_title('Spiral Function', fontsize=20)
graph.set_xlabel('Horizontal Position', fontsize=14)
graph.set_ylabel('Vertical Position', fontsize=14)
graph.tick_params(labelsize=14)

# Display the plot window
plt.show()
