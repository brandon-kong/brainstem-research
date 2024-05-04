from utils.logger.LoggerFactory import LoggerFactory
from utils.Menu import Menu
from utils.Printer import Printer

def main ():
    # Instantiate singletons and providers
    printer = Printer()
    logger = LoggerFactory.make_logger('logs/logger.log')

    # Log the start of the program
    logger.log('Starting program...')

    # Print a message
    printer.info('\nWelcome to the Brainstem Research Toolkit!\n')
    printer.print('This program will help you analyze and visualize data from the brainstem.\n')

    options = {
        'Perform K-Means Clustering': lambda: printer.print('Print'),
        'Perform PCA': lambda: printer.print('Print'),
        'Perform t-SNE': lambda: printer.print('Print'),
        'Exit': lambda: {
            printer.error('Exiting program...'),
            logger.log('Program ended.'),
            exit()
        }
    }
    # Print the menu
    menu = Menu(options)

    # Run the menu
    menu.run()

    # Log the end of the program
    logger.log('Program ended.')
    


if __name__ == '__main__':
    main()