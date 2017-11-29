import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
if (ot.Weibull().__class__.__name__=='ComposedDistribution'):
    correlation = ot.CorrelationMatrix(2)
    correlation[1, 0] = 0.25
    aCopula = ot.NormalCopula(correlation)
    marginals = [ot.Normal(1.0, 2.0), ot.Normal(2.0, 3.0)]
    distribution = ot.ComposedDistribution(marginals, aCopula)
elif (ot.Weibull().__class__.__name__=='CumulativeDistributionNetwork'):
    distribution = ot.CumulativeDistributionNetwork([ot.Normal(2),ot.Dirichlet([0.5, 1.0, 1.5])], ot.BipartiteGraph([[0,1], [0,1]]))
else:
    distribution = ot.Weibull()
dimension = distribution.getDimension()
if dimension <= 2:
    if distribution.getDimension() == 1:
        distribution.setDescription(['$x$'])
        pdf_graph = distribution.drawPDF()
        cdf_graph = distribution.drawCDF()
        fig = plt.figure(figsize=(10, 4))
        plt.suptitle(str(distribution))
        pdf_axis = fig.add_subplot(121)
        cdf_axis = fig.add_subplot(122)
        View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False)
        View(cdf_graph, figure=fig, axes=[cdf_axis], add_legend=False)
    else:
        distribution.setDescription(['$x_1$', '$x_2$'])
        pdf_graph = distribution.drawPDF()
        fig = plt.figure(figsize=(10, 5))
        plt.suptitle(str(distribution))
        pdf_axis = fig.add_subplot(111)
        View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False)