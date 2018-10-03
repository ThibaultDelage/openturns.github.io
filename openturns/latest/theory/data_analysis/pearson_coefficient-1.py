import openturns as ot
from openturns.viewer import View

N = 20
ot.RandomGenerator.SetSeed(10)
x = ot.Uniform(0.0, 10.0).getSample(N)
f = ot.SymbolicFunction(['x'], ['5*x+10'])
y = f(x) + ot.Normal(0.0, 5.0).getSample(N)
graph = f.draw(0.0, 10.0)
graph.setTitle('A linear relationship exists between U and V:\n Pearson\'s coefficient is a relevant measure of dependency')
graph.setXTitle('u')
graph.setYTitle('v')
cloud = ot.Cloud(x, y)
cloud.setPointStyle('circle')
cloud.setColor('orange')
graph.add(cloud)
View(graph)