import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
if ot.Process().__class__.__name__ == 'Process':
    # default to Gaussian for the interface class
    process = ot.GaussianProcess()
else:
    process = ot.Process()
process.setTimeGrid(ot.RegularGrid(0.0, 0.02, 50))
process.setDescription(['$x$'])
sample = process.getSample(6)
sample_graph = sample.drawMarginal(0)
sample_graph.setTitle(str(process))

fig = plt.figure(figsize=(10, 4))
sample_axis = fig.add_subplot(111)
View(sample_graph, figure=fig, axes=[sample_axis], add_legend=False)