import openturns as ot
from openturns.viewer import View

d = ot.Axial([1.5, 2.5, 3.5], [1, 2, 3])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("Axial experiment")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)