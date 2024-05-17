from providers.ConfigurationProvider import ConfigurationProvider

from utils.logger.LoggerFactory import LoggerFactory
from utils.Menu import Menu
from utils.Printer import Printer
from utils.FileUtility import FileUtility
from utils.InputUtility import InputUtility
from utils.DataFrameLoader import DataFrameLoader

from utils.constants import CONFIG_FILE, LOGGER_FILE_SUFFIX, LOG_FILE, CONFIG_KEYS

logger = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, LOG_FILE)


def exit_program():
    Printer.error('Exiting program...')
    logger.log('Program ended.')

    exit()


def main():
    # Instantiate singletons and providers
    config = ConfigurationProvider()

    # Log the start of the program
    logger.log('Starting program...')

    # Print a message
    Printer.info('\nWelcome to the Brainstem Research Toolkit!')
    Printer.print('This program will help you analyze and visualize data from the brainstem.\n')

    Printer.loading('Loading configuration...')

    # Read the config file
    config_file = FileUtility.read_json(CONFIG_FILE)

    if config_file is None:
        # Prompt the user to create a new configuration file
        Printer.warning('Configuration file not found.')

        if not InputUtility.get_yes_no_input('Would you like to create a new configuration file?'):
            exit_program()

        # Create a new configuration file

    else:
        # Load the configuration

        try:
            config.load_configuration(config_file, CONFIG_KEYS)
            Printer.success(f'Configuration loaded successfully: {config.length()} config(s) loaded.')

        except Exception as e:
            Printer.error(f'Error loading configuration: {e}')
            exit_program()

    # Load the data from the data directory

    Printer.loading('\nLoading data...')

    dataframes = DataFrameLoader.load_dataframes_in_directory('data')

    Printer.success(f'{len(dataframes)} dataframe(s) loaded successfully.')

    options = {
        'Perform K-Means Clustering': lambda: Menu({
            'Perform K-Means Clustering on all data': lambda: Printer.print('Print'),
            'Perform K-Means Clustering on a subset of data': lambda: Printer.print('Print'),
            'Perform K-Means Clustering on a subset of genes': lambda: Printer.print('Print'),
            'Perform K-Means Clustering on a subset of samples': lambda: Printer.print('Print'),
            'Perform K-Means Clustering on a subset of genes and samples': lambda: Printer.print('Print'),
            'Back': lambda: Printer.print('Print')
        }).run()
        ,

        'Perform PCA': lambda: Printer.print('Print'),
        'Perform t-SNE': lambda: Printer.print('Print'),
    }
    # Print the menu
    menu = Menu(options, include_exit=True, include_back=False)

    # Run the menu
    menu.run()

    # Log the end of the program
    exit_program()


if __name__ == '__main__':
    main()
