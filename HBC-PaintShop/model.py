class ColorType:
    UNKNOWN = 'X'
    GLOSSY = 'G'
    MATT = 'M'


class Customer:
    """
    Customer class represents customer's color choice.
    """

    def __init__(self, colors_count):
        # Dictionary key: color_number, value: color_type (G|M|X)
        self._choice_dict = {}
        for color_number in range(1, colors_count + 1):
            self.put_color_choice(color_number, ColorType.UNKNOWN)

    def put_color_choice(self, color_number, color_type):
        self._choice_dict[color_number] = color_type

    def color_at(self, color_number):
        return self._choice_dict[color_number]


class Solution:
    """
    Solution class represents a given solution instance.
    """

    def __init__(self):
        self._colors_values_dict = {}

    def color_at(self, color_number):
        return self._colors_values_dict[color_number]

    def update_color_type(self, color_number, color_type):
        self._colors_values_dict[color_number] = color_type

    @classmethod
    def create(cls, colors_count, color_data_point):
        solution = Solution()

        mask = 0
        while colors_count > 0:
            if color_data_point & (1 << mask) > 0:
                solution._colors_values_dict[colors_count] = ColorType.MATT
            else:
                solution._colors_values_dict[colors_count] = ColorType.GLOSSY
            colors_count -= 1
            mask += 1

        return solution

    @classmethod
    def create_minimum(cls, colors_count):
        solution = Solution()
        for color_number in range(1, colors_count + 1):
            solution._colors_values_dict[color_number] = ColorType.GLOSSY
        return solution

    def to_string(self):
        colors = []
        for i in range(1, len(self._colors_values_dict) + 1):
            colors.append(self._colors_values_dict[i])
        return ' '.join(colors)
