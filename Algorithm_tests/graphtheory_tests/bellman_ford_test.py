# Import folder where sorting algorithms
import sys
import unittest

# For importing from different folders
# OBS: This is supposed to be done with automated testing, hence relative to folder we want to import from
sys.path.append("Algorithms/graphtheory/bellman-ford")

# If run from local:
# sys.path.append('../../Algorithms/graphtheory/bellman-ford')

from bellman_ford import bellman_ford


class test_BellmanFord(unittest.TestCase):
    def test_negativecycle(self):
        # Because of negative cycles, we shall denote the shortest path for these
        # as -infinity.
        G = {1: {2: 5, 3: 20}, 2: {4: 10}, 3: {5: 10}, 4: {}, 5: {6: 5}, 6: {3: -20}}

        correct_shortest_dist = {
            1: 0,
            2: 5,
            3: -float("inf"),
            4: 15,
            5: -float("inf"),
            6: -float("inf"),
        }
        shortest_dist, _ = bellman_ford(G, 1)

        self.assertEqual(shortest_dist, correct_shortest_dist)

    def test_shortestdist(self):
        G = {1: {2: 100, 3: 5}, 2: {4: 20}, 3: {2: 10}, 4: {}}

        start_node = 1
        shortest_dist, _ = bellman_ford(G, start_node)

        # Test distance to starting node should be 0
        self.assertEqual(shortest_dist[start_node], 0)

        # Test shortest distances from graph
        self.assertEqual(shortest_dist[2], 15)
        self.assertEqual(shortest_dist[3], 5)
        self.assertEqual(shortest_dist[4], 35)

    def test_run_emptygraph(self):
        G = {}
        start_node = 1

        # Cant run an empty graph without returning error
        with self.assertRaises(ValueError):
            shortest_dist, _ = bellman_ford(G, start_node)


if __name__ == "__main__":
    print("Running bellman ford tests:")
    unittest.main()
