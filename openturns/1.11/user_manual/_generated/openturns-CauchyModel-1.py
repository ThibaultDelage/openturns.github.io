import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
spectralModel = ot.CauchyModel()
if spectralModel.getInputDimension() == 1:
    spec_graph = spectralModel.draw(0, 0, True)
    spec_graph.setXTitle('f')
    spec_graph.setYTitle('Spectral Density')
    fig = plt.figure(figsize=(10, 4))
    plt.suptitle(str(spectralModel))
    spec_axis = fig.add_subplot(111)
    View(spec_graph, figure=fig, axes=[spec_axis], add_legend=False)