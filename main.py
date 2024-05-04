from providers.ConfigurationProvider import ConfigurationProvider

from utils.logger.LoggerFactory import LoggerFactory
from utils.Menu import Menu
from utils.Printer import Printer
from utils.FileUtility import FileUtility
from utils.InputUtility import InputUtility

from utils.constants import CONFIG_FILE, LOG_FILE

printer = Printer()
logger = LoggerFactory.make_logger(LOG_FILE)

def exit_program():
    printer.error('Exiting program...')
    logger.log('Program ended.')

    exit()

def main ():
    # Instantiate singletons and providers
    config = ConfigurationProvider()

    # Log the start of the program
    logger.log('Starting program...')

    # Print a message
    printer.info('\nWelcome to the Brainstem Research Toolkit!')
    printer.print('This program will help you analyze and visualize data from the brainstem.\n')

    printer.loading('Loading configuration...')

    # Read the config file
    config_file = FileUtility.read_json(CONFIG_FILE)

    if config_file is None:
        # Prompt the user to create a new configuration file
        printer.warning('Configuration file not found.')
        
        if not InputUtility.get_yes_no_input('Would you like to create a new configuration file?'):
            exit_program()

        # Create a new configuration file

    else:
        # Load the configuration

        try:
            config.load_configuration(config_file)
            printer.success(f'Configuration loaded successfully: {config.length()} config(s) loaded.\n')

        except Exception as e:
            printer.error(f'Error loading configuration: {e}\n')
            exit_program()



    options = {
        'Perform K-Means Clustering': lambda: printer.print('Print'),
        'Perform PCA': lambda: printer.print('Print'),
        'Perform t-SNE': lambda: printer.print('Print'),
        'Exit': exit_program
    }
    # Print the menu
    menu = Menu(options)

    # Run the menu
    menu.run()

    # Log the end of the program
    exit_program()
    


if __name__ == '__main__':
    main()