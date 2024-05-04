from utils.logger.LoggerFactory import LoggerFactory

from utils.Printer import Printer

def main ():
    logger = LoggerFactory.make_logger('logger.log.txt')
    logger.log('Starting program...')
    
    

if __name__ == '__main__':
    main()