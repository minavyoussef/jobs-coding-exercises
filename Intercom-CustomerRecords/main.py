import logging
import os
from datetime import datetime

from Services.DependencyInjection.InjectorKernal import init_injector
from app.LocationApp import LocationApp
from app.LocationAppParameters import LocationAppParameters
from main_args import setup_args_parser


def init_logger():
    log_dir = './logs/'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(level=logging.INFO,
                        filename=f"{log_dir}{datetime.now().strftime('exec_log_%Y%m%d_%H%M%S.%f.log')}",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


if __name__ == '__main__':
    init_logger()

    logging.info('Intercom Customer Location Service V1.0 - Application Started')

    # Parse command line argument.
    parser = setup_args_parser()
    args = parser.parse_args()
    logging.info(f'Passed command-lined args: {args}')

    # Initialize DependencyInjection
    init_injector()

    # Parse command-line argument.
    location_app_parameters = LocationAppParameters.from_args(args)

    # Invoke location app.
    location_app = LocationApp(location_app_parameters)
    location_app.run()

    logging.info('Intercom Customer Location Service V1.0 - Application Finished')
