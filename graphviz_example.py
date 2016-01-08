# this is adapted from
#  https://gist.github.com/matthiaseisen/3278cedcd53afe62c3f3


svgoutputname = "test_graphviz"

import graphviz as gv

nodes = ['web01','web01','web01','switch01']
edges = [['web01', 'switch01'],
			['web02', 'switch01'],
			['web03', 'switch01'] ]

g1 = gv.Graph(format='svg')

for node in nodes:
	g1.node( node )

for edge in edges:
	fromNode, toNode = edge
	g1.edge( fromNode, toNode )

print "Resulting dot text (put his in a file and use it with graphviz)"
print(g1.source)
print ""

filename = g1.render(filename=svgoutputname)
print "output file is ", filename
print "   ristretto", filename
