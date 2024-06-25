from sklearn.tree import export_graphviz
# Assuming clf is a trained decision tree classifier
tree.export_graphviz(clf, out_file='tree.dot')
