import unittest

from environmental.layers.ascii_art_layer import AsciiArtLayer


class TestAsciiArtLayer(unittest.TestCase):
    def setUp(self):
        self.ascii_art_layer = AsciiArtLayer()

    def test_run(self):
        individuals = [{'art': ''}, {'art': ''}]
        environment = 'environment'
        updated_individuals = self.ascii_art_layer.run(individuals, environment)
        for individual in updated_individuals:
            self.assertNotEqual(individual['art'], '')

    def test_fit_func(self):
        genes = 'genes'
        fitness = self.ascii_art_layer.fit_func(genes)
        self.assertEqual(fitness, self.ascii_art_layer.fitness)

    def test_run_edge_case(self):
        individuals = []
        environment = 'environment'
        updated_individuals = self.ascii_art_layer.run(individuals, environment)
        self.assertEqual(updated_individuals, [])

    def test_fit_func_edge_case(self):
        genes = ''
        fitness = self.ascii_art_layer.fit_func(genes)
        self.assertEqual(fitness, self.ascii_art_layer.fitness)

if __name__ == '__main__':
    unittest.main()
