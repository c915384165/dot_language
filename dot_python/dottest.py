from graphviz import Digraph

dot = Digraph(comment="The Round Table")

dot.node('A', 'King Arthur')
dot.view()

dot.node('B', 'Sir Bedevere the Wise')
