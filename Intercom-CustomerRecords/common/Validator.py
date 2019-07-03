import os


class Validator:
    """
    Class Validator represents general validation methods.
    """

    @staticmethod
    def is_null_or_empty(param):
        if param is None:
            return True
        return isinstance(param, str) and param == ''

    @staticmethod
    def has(instance, member):
        if member not in instance:
            raise Exception(f'Expected {member} as member of {instance}')

    @staticmethod
    def is_type(instance, expected_type):
        if not isinstance(instance, expected_type):
            raise TypeError(f'Expected {expected_type} but got {type(instance)}')

    @staticmethod
    def file_exists(input_file):
        if Validator.is_null_or_empty(input_file):
            raise ValueError('Invalid passed input file')
        if not os.path.exists(input_file):
            raise FileNotFoundError(f'File {input_file} does not exists')
