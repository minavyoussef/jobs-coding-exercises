import unittest

from solvers.BruteForceOptimisation import BruteForceOptimisation
from solvers.EliminationOptimisation import EliminationOptimisation

from solvers.Solver import Solver

optimizer = EliminationOptimisation()

"""
Testing Brute Force Optimisation Method
"""


class TestBruteForceOptimisation(unittest.TestCase):
    def test_input_sample_1(self):
        solution = Solver.optimize('./QA/input_sample_1.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'G G G G M')

    def test_input_sample_2(self):
        solution = Solver.optimize('./QA/input_sample_2.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'No solution found')

    def test_input_sample_3(self):
        solution = Solver.optimize('./QA/input_sample_3.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'M M')

    def test_input_sample_4(self):
        solution = Solver.optimize('./QA/input_sample_4.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'G M G M G')

    def test_input_tc_1(self):
        solution = Solver.optimize('./QA/input_tc_1.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'G')

    def test_input_tc_2(self):
        solution = Solver.optimize('./QA/input_tc_2.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'M')

    def test_input_tc_3(self):
        solution = Solver.optimize('./QA/input_tc_3.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'M G G G G G G G G G')

    def test_input_tc_4(self):
        solution = Solver.optimize('./QA/input_tc_4.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'M M M M M M M M M M')

    def test_input_tc_5(self):
        solution = Solver.optimize('./QA/input_tc_5.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'G M G M G')

    def test_input_tc_6(self):
        solution = Solver.optimize('./QA/input_tc_6.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'G G')

    def test_input_tc_7(self):
        solution = Solver.optimize('./QA/input_tc_7.txt', BruteForceOptimisation())
        self.assertEqual(solution, 'M M')

"""
Testing Elimination Optimisation Method
"""


class TestEliminationOptimisation(unittest.TestCase):
    def test_input_sample_1(self):
        solution = Solver.optimize('./QA/input_sample_1.txt', EliminationOptimisation())
        self.assertEqual(solution, 'G G G G M')

    def test_input_sample_2(self):
        solution = Solver.optimize('./QA/input_sample_2.txt', EliminationOptimisation())
        self.assertEqual(solution, 'No solution found')

    def test_input_sample_3(self):
        solution = Solver.optimize('./QA/input_sample_3.txt', EliminationOptimisation())
        self.assertEqual(solution, 'M M')

    def test_input_sample_4(self):
        solution = Solver.optimize('./QA/input_sample_4.txt', EliminationOptimisation())
        self.assertEqual(solution, 'G M G M G')

    def test_input_tc_1(self):
        solution = Solver.optimize('./QA/input_tc_1.txt', EliminationOptimisation())
        self.assertEqual(solution, 'G')

    def test_input_tc_2(self):
        solution = Solver.optimize('./QA/input_tc_2.txt', EliminationOptimisation())
        self.assertEqual(solution, 'M')

    def test_input_tc_3(self):
        solution = Solver.optimize('./QA/input_tc_3.txt', EliminationOptimisation())
        self.assertEqual(solution, 'M G G G G G G G G G')

    def test_input_tc_4(self):
        solution = Solver.optimize('./QA/input_tc_4.txt', EliminationOptimisation())
        self.assertEqual(solution, 'M M M M M M M M M M')

    def test_input_tc_5(self):
        solution = Solver.optimize('./QA/input_tc_5.txt', EliminationOptimisation())
        self.assertEqual(solution, 'G M G M G')

    def test_input_tc_6(self):
        solution = Solver.optimize('./QA/input_tc_6.txt', EliminationOptimisation())
        self.assertEqual(solution, 'G G')

    def test_input_tc_7(self):
        solution = Solver.optimize('./QA/input_tc_7.txt', EliminationOptimisation())
        self.assertEqual(solution, 'M M')

if __name__ == '__main__':
    unittest.main()
