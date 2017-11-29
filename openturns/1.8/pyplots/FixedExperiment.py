import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
ot.RandomGenerator.SetSeed(0)

# Generate sample with the given plane
size = 20
dim = 2
refSample = ot.NumericalSample(size, dim)
for i in range(size):
    p = ot.NumericalPoint(dim)
    for j in range(dim):
        p[j] = i + j
    refSample[i] = p

myPlane = ot.FixedExperiment(refSample)

sample = myPlane.generate()

# Create an empty graph
graph = ot.Graph("", "x1", "x2", True, "")

# Create the cloud
cloud = ot.Cloud(sample, "blue", "fsquare", "")

# Then, draw it
graph.add(cloud)
fig = plt.figure(figsize=(4, 4))
plt.suptitle("Fixed experiment")
axis = fig.add_subplot(111)
axis.set_xlim(auto=True)
View(graph, figure=fig, axes=[axis], add_legend=False)
