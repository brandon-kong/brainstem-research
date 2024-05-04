from utils.logger.LoggerFactory import LoggerFactory

from utils.Printer import Printer

def main ():
    logger = LoggerFactory.make_logger('logger.log.txt')
    logger.log('Hello, World!')
    
    printer = Printer()
    printer.print('Hello, World!')

    printer.error('This is an error message')

    printer.warning('This is a warning message')

if __name__ == '__main__':
    main()