from utils.logger.LoggerFactory import LoggerFactory

def main ():
    logger = LoggerFactory.make_logger('test.log.txt')
    logger.log('Hello, World!')
    print(logger.read())
    logger.clear()
    print(logger.read())

if __name__ == '__main__':
    main()