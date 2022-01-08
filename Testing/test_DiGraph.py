from unittest import TestCase
from DiGraph import DiGraph

"""This is the test class for the Digraph class."""

class TestDiGraph(TestCase):

    """This test checks the amount of nodes in the graph."""
    def test_v_size(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertEqual(graph_test.v_size(), 4)

    """This test checks the return of all the nodes in the graph."""
    def test_get_all_v(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        print(graph_test.get_all_v().get(1).location)

    """This test checks the size of all the edges in the graph."""
    def test_e_size(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertEqual(graph_test.e_size(), 4)

    """This test checks the return of the in edges in the graph."""
    def test_all_in_edges_of_node(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        print(graph_test.all_in_edges_of_node(4))

    """This test checks the return of the out edges in the graph."""
    def test_all_out_edges_of_node(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        print(graph_test.all_out_edges_of_node(1))

    """This test checks the return of the MC o the graph."""
    def test_get_mc(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertEqual(graph_test.mc, 8)

    """This test checks if an edge was added properly to the graph."""
    def test_add_edge(self):
        graph_test = DiGraph()
        self.assertFalse(graph_test.add_edge(1, 2, 1))
        graph_test.add_node(1, (0, 0, 0))
        self.assertFalse(graph_test.add_edge(1, 2, 1))
        graph_test.add_node(2, (0, 0, 0))
        self.assertTrue(graph_test.add_edge(1, 2, 1))

    """This test if a node was added properly to the graph."""
    def test_add_node(self):
        graph_test = DiGraph()
        self.assertTrue(graph_test.add_node(1, (0, 0, 0)))
        self.assertTrue(graph_test.add_node(2, (0, 0, 0)))
        self.assertTrue(graph_test.add_node(3, (0, 0, 0)))
        self.assertTrue(graph_test.add_node(4, (0, 0, 0)))

    """This test checks if a node was removed properly from the graph."""
    def test_remove_node(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        self.assertTrue(graph_test.remove_node(1))
        self.assertTrue(graph_test.remove_node(2))

    """This test checks if an edge was properly removed from the graph."""
    def test_remove_edge(self):
        graph_test = DiGraph()
        graph_test.add_node(1, (0, 0, 0))
        graph_test.add_node(2, (0, 0, 0))
        graph_test.add_node(3, (0, 0, 0))
        graph_test.add_node(4, (0, 0, 0))
        graph_test.add_edge(1, 2, 1)
        graph_test.add_edge(1, 3, 1)
        graph_test.add_edge(1, 4, 1)
        graph_test.add_edge(2, 4, 1)
        self.assertTrue(graph_test.remove_edge(1, 2))
        self.assertTrue(graph_test.remove_edge(2, 4))