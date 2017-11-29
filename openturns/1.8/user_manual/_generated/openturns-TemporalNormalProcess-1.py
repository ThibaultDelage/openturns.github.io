import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
process = ot.TemporalNormalProcess()
process.setTimeGrid(ot.RegularGrid(0.0, 0.02, 50))
process.setDescription(['$x$'])
sample = process.getSample(6)
sample_graph = sample.drawMarginal(0)
fig = plt.figure(figsize=(10, 4))
plt.suptitle(str(process))
sample_axis = fig.add_subplot(111)
View(sample_graph, figure=fig, axes=[sample_axis], add_legend=False)