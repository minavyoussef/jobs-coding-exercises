from model import ColorType, Solution
from solvers.OptimisationBase import OptimisationBase


class EliminationOptimisation(OptimisationBase):
    """
    EliminationOptimisation class represents an elimination approach in finding solution
    this is achieved by starting with the cheapest paint combination ('G', 'G', 'G', 'G') for n = 4
    and then for every customer requirement we restrict the combination till we can't optimise further.
    """

    @classmethod
    def optimize(cls, colors_count, customers_list):
        solution = Solution.create_minimum(colors_count)

        while cls.can_optimize(colors_count, solution):
            for customer in customers_list:
                if not cls.satisfy_customer(colors_count, solution, customer):
                    cls.update_solution(colors_count, solution, customer)

            if cls.satisfy_customers(colors_count, solution, customers_list):
                return solution.to_string()

        return 'No solution found'

    @classmethod
    def update_solution(cls, colors_count, solution, customer):
        for color_number in range(1, colors_count + 1):
            if customer.color_at(color_number) == ColorType.MATT:
                solution.update_color_type(color_number, ColorType.MATT)

    @classmethod
    def can_optimize(cls, colors_count, solution):
        for color_number in range(1, colors_count + 1):
            if solution.color_at(color_number) != ColorType.MATT:
                return True
        return False
