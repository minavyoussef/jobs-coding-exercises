import argparse

from solvers.BruteForceOptimisation import BruteForceOptimisation
from solvers.EliminationOptimisation import EliminationOptimisation

from solvers.Solver import Solver

optimizer = EliminationOptimisation()

if __name__ == '__main__':
    # Parse command line argument.
    parser = argparse.ArgumentParser(description='PaintShop Optimiser V1.0')
    parser.add_argument('input_file', type=str, help='Input file')
    parser.add_argument('--method', dest='method', type=str, help='Solution method [BruteForce | Elimination (default)]', default='Elimination')
    args = parser.parse_args()

    # Invoke solver.
    solvers_dict = {
        'bruteforce': BruteForceOptimisation(),
        'elimination': EliminationOptimisation()
    }
    arg_method = args.method.lower()
    if arg_method in solvers_dict.keys():
        solution = Solver.optimize(args.input_file, solvers_dict[arg_method])
        print(solution)
    else:
        raise Exception(f'Invalid solver method {arg_method}')
