import unittest

from utils.logger.LoggerFactory import LoggerFactory
from utils.logger.Logger import Logger

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = LoggerFactory.make_logger('test.log.txt')
        self.logger.create_file()

        self.loggers = [self.logger]

    def tearDown(self) -> None:
        for logger in self.loggers:
            logger.delete()

    def test_factory(self):
        logger = LoggerFactory.make_logger('test.log.txt')
        self.assertEqual(logger, self.logger)

        logger2 = LoggerFactory.make_logger('test.log.txt')
        self.assertEqual(logger, logger2)

        logger3 = LoggerFactory.make_logger('test2.log.txt')
        self.assertEqual(logger, logger2)
        self.assertNotEqual(logger2, logger3)
        
        self.loggers.append(logger)
        self.loggers.append(logger2)
        self.loggers.append(logger3)
        
    def test_log(self):
        self.logger.log('test')
        self.assertIsNotNone(self.logger.read())

    def test_read(self):
        self.logger.log('test')
        self.assertIsNotNone(self.logger.read())

    def test_clear(self):
        self.logger.log('test')
        self.logger.clear()
        self.assertEqual(self.logger.read(), '')

    def test_delete(self):
        self.logger.log('test')
        self.logger.delete()
        self.assertFalse(self.logger.file_exists())

    def test_file_exists(self):
        self.assertTrue(self.logger.file_exists())

        self.logger.delete()
        self.assertFalse(self.logger.file_exists())

    def test_log_file_suffix(self):
        with self.assertRaises(ValueError):
            Logger('test.log')
        
        with self.assertRaises(ValueError):
            Logger('test.txt')

    def test_read_file_not_exists(self):
        logger = LoggerFactory.make_logger('test2.log.txt')

        logger.delete()

        with self.assertRaises(FileNotFoundError):
            logger.read()

        self.loggers.append(logger)

        

