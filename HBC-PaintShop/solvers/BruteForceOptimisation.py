import math

from model import Solution
from solvers.OptimisationBase import OptimisationBase


class BruteForceOptimisation(OptimisationBase):
    """
    BruteForceOptimisation class represents Brute Force approach by searching all the solution space
    from most cheapest option [('G', 'G', 'G', 'G', 'G') for color_count = 5] to the most expensive one
    [('M', 'M', 'M', 'M', 'M') for color_count = 5] as we are trying to minimise.
    """


    @classmethod
    def optimize(cls, colors_count, customers_list):
        # equivalent to ('G', 'G', 'G', 'G', 'G') for color_count = 5
        min_search_space_value = 0
        # equivalent to ('M', 'M', 'M', 'M', 'M') for color_count = 5
        max_search_space = int(math.pow(2, colors_count) - 1)

        for solution_data_point in range(min_search_space_value, max_search_space + 1):
            solution = Solution.create(colors_count, solution_data_point)
            if cls.satisfy_customers(colors_count, solution, customers_list):
                return solution.to_string()

        return 'No solution found'
