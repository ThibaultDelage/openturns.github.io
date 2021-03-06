import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

# Generate points with the given sequence
sequence = ot.SobolSequence(2)
sample = sequence.generate(1000)

# Create the graph
graph = ot.Graph("", "x1", "x2", True, "")
cloud = ot.Cloud(sample)
graph.add(cloud)

# Draw the graph
fig = plt.figure(figsize=(4, 4))
plt.suptitle("Sequence of 1000 points")
axis = fig.add_subplot(111)
View(graph, figure=fig, axes=[axis], add_legend=False)
axis.set_xlim(auto=True)