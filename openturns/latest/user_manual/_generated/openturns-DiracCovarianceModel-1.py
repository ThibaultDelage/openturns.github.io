import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
covarianceModel = ot.DiracCovarianceModel()
if covarianceModel.getInputDimension() == 1:
    scale = covarianceModel.getScale()[0]
    if covarianceModel.isStationary():
        def f(x):
            return [covarianceModel(x)[0, 0]]
        func = ot.PythonFunction(1,1,f)
        func.setDescription(['$tau$', '$cov$'])
        cov_graph = func.draw(-3.0 * scale, 3.0 * scale, 129)
        fig = plt.figure(figsize=(10, 4))
        plt.suptitle(str(covarianceModel))
        cov_axis = fig.add_subplot(111)
        View(cov_graph, figure=fig, axes=[cov_axis], add_legend=False)
    else:
        def f(x):
            return [covarianceModel([x[0]], [x[1]])[0, 0]]
        func = ot.PythonFunction(2,1,f)
        func.setDescription(['$s$', '$t$', '$cov$'])
        cov_graph = func.draw([-3.0 * scale]*2, [3.0 * scale]*2, [129]*2)
        fig = plt.figure(figsize=(10, 4))
        plt.suptitle(str(covarianceModel))
        cov_axis = fig.add_subplot(111)
        View(cov_graph, figure=fig, axes=[cov_axis], add_legend=False, square_axes=True)