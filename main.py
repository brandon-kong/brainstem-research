from utils.Logger import Logger

def main ():
    logger = Logger()
    logger.log('Hello, World!')
    print(logger.read())
    logger.clear()
    print(logger.read())

if __name__ == '__main__':
    main()