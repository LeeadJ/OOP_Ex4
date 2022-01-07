import heapq as hq
import json
import math
from itertools import permutations
from random import uniform
from typing import List
import sys
from matplotlib import pyplot as plt
from numpy.compat import long
from array import *
from collections import deque
from DiGraph import*
from Gnode import*
from GraphAlgoInterface import*
from GraphInterface import*

"""This class represents algorithms of a graph."""


class GraphAlgo(GraphAlgoInterface):
    """Constructor"""

    def _init_(self, graph: DiGraph = DiGraph()):
        self.graph = graph

    """This function return the graph on which the algorithm works on."""

    def get_graph(self) -> GraphInterface:
        return self.graph

    """This function loads a graph from a json file."""

    def load_from_json(self, file_name: str) -> bool:
        try:
            json_load = json.loads(file_name)
            graph = DiGraph()
            for node in json_load['Nodes']:
                if "pos" not in node:
                    graph.add_node(node["id"])
                else:
                    pos = eval(str(node["pos"]))
                    graph.add_node(node["id"], pos)
            for edge in json_load['Edges']:
                graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = graph
            return True
        except Exception as exception:
            raise NotImplementedError

    """This function saves the graph in JSON format to a file."""

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as write_file:
                json_graph = {"Edges": [], "Nodes": []}
                # save edges as json
                for id1 in self.get_graph().get_all_v().keys():
                    for id2, w in self.get_graph().all_out_edges_of_node(id1).items():
                        json_graph["Edges"].append({"src": id1, "dest": id2, "w": w})
                # save nodes as json
                for n in self.get_graph().get_all_v().values():
                    if n.location is None:
                        json_graph["Nodes"].append({"id": n.key})
                    else:
                        json_graph["Nodes"].append({"pos": str(n.location)[1: -1], "id": n.key})
                # json.dump(json_graph, write_file)
                json_output = json.dumps(json_graph, allow_nan=True, indent=len(json_graph))
                write_file.write(json_output)
            return True
        except Exception as e:
            raise NotImplementedError
        finally:
            write_file.close()

    """This function returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm."""

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        keys = self.graph.get_all_v().keys()
        # check if the nodes exist in the graph.
        if id1 not in keys or id2 not in keys:
            return float('inf'), []

        if id1 == id2:
            return 0, []

        return self.dijkstraAlgo(id1, id2)

    """This function returns True if the graph is a connected graph."""

    def isConnected(self) -> bool:
        Nlist = []
        nodeMap = {}
        nodes = 0
        for n in self.graph.node_map.values():
            temp = Gnode(n.key, n.location)
            nodeMap[n.key] = temp
            Nlist.append(temp)
            nodes += 1
        visited = [False for i in range(nodes)]
        for i in range(nodes):
            GraphAlgo.DFS(self.graph, i, visited, Nlist, nodeMap)
            for bool in visited:
                if not bool:
                    return False
        return True

    """This function searches a list of nodes using the Depth-first search method."""

    @staticmethod
    def DFS(graph: DiGraph, node_id: int, vistied: List[bool], Nlist: List[Gnode], nodeMap: dict):
        stack = deque()
        stack.append(Nlist[node_id])
        while len(stack) > 0:
            node_id = Nlist.index(stack[-1])
            stack.pop()

            if not vistied[node_id]:
                vistied[node_id] = True
            for e in graph.all_out_edges_of_node(Nlist[node_id].key):
                if not vistied[e]:
                    stack.append(Nlist[e])

    """This function finds the shortest path that visits all the nodes in the list."""

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        best_weight = sys.maxsize
        # loop through all the nodes in the list and check each one as the starting point.
        for starting_n in node_lst:
            if self.tsp_helper(starting_n, node_lst)[1] < best_weight:
                best_weight = self.tsp_helper(starting_n, node_lst)[1]
                best_path, weight = self.tsp_helper(starting_n, node_lst)
        if best_weight == sys.maxsize:
            return [], float('inf')
        return best_path, weight

    """This function is a helper function to the TSP function."""

    def tsp_helper(self, starting_n, node_list):
        best_path = []
        path = []
        temp_list = []
        # create a list of the nodes without the starting one.
        for i in node_list:
            if i != starting_n:
                temp_list.append(i)

        min_weight = sys.maxsize
        # create permutations of all the nodes
        permu = permutations(temp_list)

        # loop through all the permutations.
        for curr_permu in permu:
            path.clear()  # reset the path for each iteration.
            relevant = True
            curr_weight = 0
            k = starting_n
            path.append(k)
            # loop through the permutation
            for j in curr_permu:
                weight = self.dijkstraAlgo(k, j)[0]
                # loop through the nodes in the list and find the shortest path using dijkstras.
                for n in range(len(self.dijkstraAlgo(k, j)[1])):
                    if n != 0:
                        path.append(self.dijkstraAlgo(k, j)[1][n])
                if weight == float('inf'):  # weight does not exist
                    relevant = False
                    break
                curr_weight += weight
                k = j
            if relevant:  # relevant remains true, so all edges exist
                if min_weight > curr_weight:
                    min_weight = curr_weight
                    best_path = path
        return best_path, min_weight

    """This function finds the node that has the shortest distance to it's farthest node."""

    def centerPoint(self) -> (int, float):
        # continue only if the graph is connected.
        if self.isConnected():
            min_distance = math.inf
            node_id = 0
            curr_max = 0
            for Node1 in self.get_graph().get_all_v().values():
                for Node2 in self.get_graph().get_all_v().values():
                    distance = self.shortest_path(Node1.key, Node2.key)[0]
                    if distance > curr_max:
                        curr_max = distance
                if curr_max < min_distance:
                    min_distance = curr_max
                    node_id = Node1.key
                curr_max = 0
            ans = (node_id, min_distance)
            return ans
        else:
            return -1, float('inf')

    """This function plots the graph."""

    def plot_graph(self) -> None:
        for node in self.get_graph().get_all_v().values():
            x, y, z = node.location
            plt.plot(x, y, markersize=25, marker='.', color='#14D5F0')
            plt.text(x, y, str(node.key), color='#7D2F9F', fontsize=12)
            for dest_id, w in self.graph.all_out_edges_of_node(node.key).items():
                dest = self.graph.node_map.get(dest_id)
                x2, y2, z2 = dest.location
                plt.annotate("", xy=(x, y), xytext=(x2, y2), arrowprops=dict(arrowstyle="<-"))
                # mid_x = (x+x2)/2
                # mid_y = (y+y2)/2
                # plt.text(mid_x, mid_y, str(w)[0:4], color='black', fontsize=10)
        plt.show()

    """This is the Dijkstra's Algorithm implementation It finds the shortest path between two given nodes.."""

    def dijkstraAlgo(self, src: int, dest: int) -> (float, list):
        # initializing the dist.
        # dist[src] is going to be zero and the rest inf.
        inf = sys.maxsize
        dist = {node: inf for node in self.graph.get_all_v()}
        dist[src] = 0
        # initializing a dictionary with the previous node of each node in the path and set the previous node of the source node to inf
        prev_nodes = {src: inf}
        # initializing a heap queue and insert the source node
        q = []
        hq.heappush(q, (0, src))  # hq = heap queue

        while q:
            # Step 1: find the unvisited node with the smallest distance, first iteration starts at current node.
            curr_node = hq.heappop(q)[1]

            # Condition 1: If the smallest distance among the unvisited nodes is infinity, then break.
            if dist[curr_node] == inf:
                break

            # loop through the unvisited nodes and calculate their distance from the src node.
            edges = self.graph.all_out_edges_of_node(curr_node)
            for neighbor in edges.keys():
                new_path = dist[curr_node] + edges.get(neighbor)
                # if the new_path is smaller than the current one, update..
                if new_path < dist[neighbor]:
                    dist[neighbor] = new_path
                    prev_nodes[neighbor] = curr_node
                    # Mark the current node as visited, insert it in the hq.
                    hq.heappush(q, (dist[neighbor], neighbor))
                # Condition 2: If the dest node is reached, break.
                if curr_node == dest:
                    break
        # Condition 3: If there is no path from src to dest:
        if dist[dest] == inf:
            return float('inf'), []
        # Creating the path list
        path = []
        curr_node = dest
        while curr_node != src:
            path.insert(0, curr_node)
            curr_node = prev_nodes[curr_node]
        if path:
            path.insert(0, curr_node)
        return dist[dest] / 1.0, path


