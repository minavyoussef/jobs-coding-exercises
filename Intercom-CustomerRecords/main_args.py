import argparse
import logging


def boolean_parser(value):
    """
    Parse boolean coommand-line argument
    """
    _boolean_mapper = {
        True: ['true', 't', '1'],
        False: ['false', 'f', '0']
    }
    for key, values in _boolean_mapper.items():
        if value in values:
            return key
    return False


def setup_args_parser():
    """
    Setup command-line argument that the application expects.

    :return: ArgumentParser instance
    :rtype: ArgumentParser
    """
    parser = argparse.ArgumentParser(description='Intercom Customer Location Service V1.0')
    parser.add_argument('--input_file', dest='input_file', type=str, required=True, help='Input file')
    parser.add_argument('--latitude', dest='latitude', type=float, required=True, help='Reference latitude')
    parser.add_argument('--longitude', dest='longitude', type=float, required=True, help='Reference longitude')
    parser.add_argument('--search_radius', dest='search_radius', type=float, required=True, help='Searching radius in kilometre')
    parser.add_argument('--stop_on_failure', dest='stop_on_failure', type=boolean_parser, default=False, required=False,
                        help='Stop execution of the whole file and raise exception if file is wrong')
    # TODO: Support passing unit distance as cmd-arg.

    parser.add_argument('--multithread-enable', dest='multithread_enable', type=boolean_parser, default=False, required=False,
                        help='Enable multi-threading execution (default disabled)')

    logging.info('Setting up args parser ' + repr(parser))

    return parser
