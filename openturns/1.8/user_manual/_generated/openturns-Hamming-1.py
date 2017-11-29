import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
filteringWindow = ot.Hamming()
numPoints = 512
data = ot.NumericalSample(numPoints, 2)
for i in range(numPoints):
    x = -0.1 + (1.2 * i) / (numPoints - 1.0)
    data[i, 0] = x
    data[i, 1] = filteringWindow(x)
graph = ot.Graph()
graph.setXTitle('$tau$')
graph.setYTitle('W')
graph.add(ot.Curve(data))
graph.setColors(['red'])
fig = plt.figure(figsize=(10, 4))
plt.suptitle(str(filteringWindow))
filtering_axis = fig.add_subplot(111)
View(graph, figure=fig, axes=[filtering_axis], add_legend=False)