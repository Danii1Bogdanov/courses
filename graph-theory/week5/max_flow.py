#!/usr/bin/env python3
# coding=utf-8

import sys


def build_graph(n, m, reader):
    graph = [[None for _ in range(n)] for _ in range(n)]
    residual_graph = [[None for _ in range(n)] for _ in range(n)]

    for i in range(m):
        u, v, w = next(reader)
        graph[u][v] = w
        residual_graph[u][v] = 0
        residual_graph[v][u] = w

    return graph, residual_graph


def augmented(origin_graph, residual_graph, path):
    def update_flow(s, t, flow):
        if origin_graph[s][t] is not None:
            # path contains forward edge
            residual_graph[s][t] += flow
            residual_graph[t][s] -= flow
        else:
            # path contains backward edge
            residual_graph[t][s] += flow
            residual_graph[s][t] -= flow

    # mask edge capacity in that task is 50
    min_flow = 51
    # find the bottleneck flow
    for i in range(len(path) - 1):
        edge_flow = residual_graph[path[i + 1]][path[i]]
        min_flow = min(min_flow, edge_flow)

    for i in range(len(path) - 1):
        update_flow(path[i], path[i + 1], min_flow)

    return min_flow


def max_flow(source: 'vertice', sink: 'vertice', graph):
    def dfs(s, t):
        visited[s] = True

        if s == t:
            return [s]

        neighbours = [i for i, w in enumerate(residual_graph[s]) if w is not None]
        # print(s, " neighbours - ", neighbours)
        for n in neighbours:
            capacity = origin_graph[s][n]
            cur_flow = residual_graph[s][n]
            back_flow = residual_graph[n][s]
            # print("capacity", s, "->", n, ":", capacity)
            # print("cur flow:", cur_flow, "back flow:", back_flow)
            if not visited[n]:
                if (capacity is not None and cur_flow < capacity
                        or capacity is None and back_flow > 0):
                    new_path = dfs(n, t)

                    if new_path is not None:
                        return [s] + new_path

        return None

    origin_graph = graph[0]
    residual_graph = graph[1]
    const_visited = [False for _ in range(len(origin_graph))]
    visited = const_visited[:]
    path = dfs(source, sink)
    flow = 0

    while path:
        flow += augmented(origin_graph, residual_graph, path)
        visited = const_visited[:]
        path = dfs(source, sink)

    return flow


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n_v, n_e = next(reader)
    graph, residual_graph = build_graph(n_v, n_e, reader)
    source = 0
    sink = n_v - 1
    print(max_flow(source, sink, (graph, residual_graph)))


if __name__ == "__main__":
    main()
