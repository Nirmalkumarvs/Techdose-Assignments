from collections import *
from heapq import heappop, heappush, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.build_graph(words)
        print(graph)
        if not graph:
            return ""

        return self.topological_order(graph)

    def build_graph(self, words):
        graph = {}

        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        n = len(words)
        print(n)
        for i in range(n-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    break
                if j == min(len(words[i]), len(words[i+1])) - 1:
                    if len(words[i]) > len(words[i+1]):
                        print("ISSUE")
                        print(words[i])
                        print(words[i+1])
                        return None

        return graph

    def topological_order(self, graph):
        indegree = self.get_indegree(graph)

        queue = [node for node in graph if indegree[node] == 0]

        heapify(queue)

        order = ""

        while queue:
            now = heappop(queue)
            order += now

            for node in graph[now]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    heappush(queue, node)
        print(order)
        return order if len(order) == len(graph) else ""

    def get_indegree(self, graph):
        indegree = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        print(indegree)
        return indegree

s=Solution()

words =["zet","zexr"]
print(s.alienOrder(words))
