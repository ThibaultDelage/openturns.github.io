import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
if ot.Wishart().__class__.__name__ == 'Bernoulli':
    distribution = ot.Bernoulli(0.7)
elif ot.Wishart().__class__.__name__ == 'Binomial':
    distribution = ot.Binomial(5, 0.2)
elif ot.Wishart().__class__.__name__ == 'ComposedDistribution':
    copula = ot.IndependentCopula(2)
    marginals = [ot.Uniform(1.0, 2.0), ot.Normal(2.0, 3.0)]
    distribution = ot.ComposedDistribution(marginals, copula)
elif ot.Wishart().__class__.__name__ == 'CumulativeDistributionNetwork':
    coll = [ot.Normal(2),ot.Dirichlet([0.5, 1.0, 1.5])]
    distribution = ot.CumulativeDistributionNetwork(coll, ot.BipartiteGraph([[0,1], [0,1]]))
elif ot.Wishart().__class__.__name__ == 'Histogram':
    distribution = ot.Histogram([-1.0, 0.5, 1.0, 2.0], [0.45, 0.4, 0.15])
elif ot.Wishart().__class__.__name__ == 'KernelMixture':
    kernel = ot.Uniform()
    sample = ot.Normal().getSample(5)
    bandwith = [1.0]
    distribution = ot.KernelMixture(kernel, bandwith, sample)
elif ot.Wishart().__class__.__name__ == 'MaximumDistribution':
    coll = [ot.Uniform(2.5, 3.5), ot.LogUniform(1.0, 1.2), ot.Triangular(2.0, 3.0, 4.0)]
    distribution = ot.MaximumDistribution(coll)
elif ot.Wishart().__class__.__name__ == 'Multinomial':
    distribution = ot.Multinomial(5, [0.2])
elif ot.Wishart().__class__.__name__ == 'RandomMixture':
    coll = [ot.Triangular(0.0, 1.0, 5.0), ot.Uniform(-2.0, 2.0)]
    weights = [0.8, 0.2]
    cst = 3.0
    distribution = ot.RandomMixture(coll, weights, cst)
elif ot.Wishart().__class__.__name__ == 'TruncatedDistribution':
    distribution = ot.TruncatedDistribution(ot.Normal(2.0, 1.5), 1.0, 4.0)
elif ot.Wishart().__class__.__name__ == 'UserDefined':
    distribution = ot.UserDefined([[0.0], [1.0], [2.0]], [0.2, 0.7, 0.1])
elif ot.Wishart().__class__.__name__ == 'ZipfMandelbrot':
    distribution = ot.ZipfMandelbrot(10, 2.5, 0.3)
else:
    distribution = ot.Wishart()
dimension = distribution.getDimension()
title = str(distribution)[:100].split('\n')[0]
if dimension == 1:
    distribution.setDescription(['$x$'])
    pdf_graph = distribution.drawPDF()
    cdf_graph = distribution.drawCDF()
    fig = plt.figure(figsize=(10, 4))
    pdf_axis = fig.add_subplot(121)
    cdf_axis = fig.add_subplot(122)
    View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False)
    View(cdf_graph, figure=fig, axes=[cdf_axis], add_legend=False)
    fig.suptitle(title)
elif dimension == 2:
    distribution.setDescription(['$x_1$', '$x_2$'])
    pdf_graph = distribution.drawPDF()
    pdf_graph.setTitle(title)
    fig = plt.figure(figsize=(10, 5))
    pdf_axis = fig.add_subplot(111)
    View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False, square_axes=True)