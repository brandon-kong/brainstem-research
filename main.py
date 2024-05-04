from utils.logger.LoggerFactory import LoggerFactory

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

    printer.print('Please select an option from the menu below:\n')


    # Log the end of the program
    logger.log('Program ended.')
    


if __name__ == '__main__':
    main()