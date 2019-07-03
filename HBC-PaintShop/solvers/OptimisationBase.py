from model import ColorType


class OptimisationBase:
    """
    Class OptimisationBase represents base class for any paint shop optimiser.
    """

    @classmethod
    def satisfy_customers(cls, colors_count, solution, customers_list):
        """
        Check if passed solution satisfy all customers.
        """

        for customer in customers_list:
            if not cls.satisfy_customer(colors_count, solution, customer):
                return False
        return True

    @classmethod
    def satisfy_customer(cls, colors_count, solution, customer):
        """
        Check if passed solution satisfy a given customer.
        """

        matt_matching_count = 0
        liked_color_count = 0

        for color_number in range(1, colors_count + 1):
            iter_solution_color = solution.color_at(color_number)
            iter_customer_color = customer.color_at(color_number)

            if iter_customer_color == iter_solution_color:
                liked_color_count += 1
                if iter_customer_color == ColorType.MATT:
                    matt_matching_count += 1

        # Constraints given in problem statement
        #   liked_color_count > 0       ... (At lease like one color)
        #   matt_matching_count <= 1    ... (At most one Matt color)
        return liked_color_count > 0 and matt_matching_count <= 1
