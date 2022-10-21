from Game_of_Life import *
g1 = Grid(5, 5, {Cell(x, 2) for x in range(1, 4)})
print(g1)
for i in range(5):
	g1 = Grid(5, 5, g1.evolve())
	print(g1)
