Composite
===================

.. plot::
    :include-source: False

    import openturns as ot
    from matplotlib import pyplot as plt
    from openturns.viewer import View

    # Generate sample with the given plane
    center = [0.5, 1.5]
    levels = [4, 8, 16]

    myPlane = ot.Composite(center, levels)
    sample = myPlane.generate()

    # Create the graph
    graph = ot.Graph("", "x1", "x2", True, "")
    cloud = ot.Cloud(sample, "blue", "fsquare", "")
    graph.add(cloud)

    # Draw the graph
    fig = plt.figure(figsize=(4, 4))
    plt.suptitle(sample.getName())
    axis = fig.add_subplot(111)
    View(graph, figure=fig, axes=[axis], add_legend=False)
    axis.set_xlim(auto=True)

.. currentmodule:: openturns

.. autoclass:: Composite

   
   .. automethod:: __init__
   