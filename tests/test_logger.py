import unittest

from utils.logger.LoggerFactory import LoggerFactory
from utils.logger.Logger import Logger

from utils.constants import LOGGER_FILE_SUFFIX

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = LoggerFactory.make_logger(f'test{LOGGER_FILE_SUFFIX}')

        self.loggers = [self.logger]

    def tearDown(self) -> None:
        for logger in self.loggers:
            logger.delete()

            del logger

    def test_factory(self):
        logger = LoggerFactory.make_logger(f'test{LOGGER_FILE_SUFFIX}')
        self.assertEqual(logger, self.logger)

        logger2 = LoggerFactory.make_logger(f'test{LOGGER_FILE_SUFFIX}')
        self.assertEqual(logger, logger2)

        logger3 = LoggerFactory.make_logger(f'test2{LOGGER_FILE_SUFFIX}')
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
        logger = LoggerFactory.make_logger(f'test5{LOGGER_FILE_SUFFIX}')
        self.assertTrue(logger.file_exists())

        logger.delete()

        self.assertFalse(logger.file_exists())

    def test_log_file_suffix(self):
        with self.assertRaises(ValueError):
            Logger('test.log.txt')
        
        with self.assertRaises(ValueError):
            Logger('test.txt')

    def test_read_file_not_exists(self):
        logger = LoggerFactory.make_logger(f'test2{LOGGER_FILE_SUFFIX}')

        logger.delete()

        with self.assertRaises(FileNotFoundError):
            logger.read()

        self.loggers.append(logger)

        

