import os

from model import Customer, ColorType
from solvers.OptimisationBase import OptimisationBase


class Solver:
    """
    Solver class reporesents facade for controlling input parameter to the optimiser
    """

    @classmethod
    def optimize(cls, input_file, optimiser):
        cls.validate_params(input_file, optimiser)

        # Parse input file.
        colors_numbers, customers_list = cls.parse(input_file)

        # Solve using passed optimiser.
        return optimiser.optimize(colors_numbers, customers_list)

    @classmethod
    def validate_params(cls, input_file, optimiser):
        if not os.path.isfile(input_file):
            raise Exception('input file does not exists and/or invalid')
        if not isinstance(optimiser, OptimisationBase):
            raise Exception('Invalid optimiser')

    @classmethod
    def parse(cls, input_file):
        customers_list = []

        with open(input_file) as fp:
            # Parse number of colors.
            colors_count = int(fp.readline())

            # Parse customer per line.
            line = fp.readline().strip()
            while line:
                customer = Customer(colors_count)

                tokens = line.split(' ')
                for i in range(0, len(tokens), 2):
                    color_number = int(tokens[i])
                    color_type = ColorType.GLOSSY if tokens[i + 1] == 'G' else ColorType.MATT

                    customer.put_color_choice(color_number, color_type)

                customers_list.append(customer)
                line = fp.readline().strip()

        return colors_count, customers_list
