import unittest

from utils.logger.LoggerFactory import LoggerFactory
from utils.logger.Logger import Logger

from utils.constants import LOGGER_FILE_SUFFIX

class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, f'test{LOGGER_FILE_SUFFIX}')
        self.loggers = [self.logger]

    def tearDown(self) -> None:
        for logger in self.loggers:
            logger.delete()

            del logger

    def test_make_logger_creates_same_logger_for_same_name(self):
        logger1 = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, f'test{LOGGER_FILE_SUFFIX}')
        logger2 = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, f'test{LOGGER_FILE_SUFFIX}')
        self.assertEqual(logger1, logger2)

    def test_make_logger_creates_different_logger_for_different_name(self):
        logger1 = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, f'test{LOGGER_FILE_SUFFIX}')
        logger2 = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, f'test2{LOGGER_FILE_SUFFIX}')
        self.assertNotEqual(logger1, logger2)

        # Add the logger to the list of loggers to delete
        self.loggers.append(logger2)

    def test_log_writes_message_to_log(self):
        message = 'test'
        self.logger.log(message)
        log_content = self.logger.read().rstrip()
        # Check if the log content contains the message
        self.assertIn(message, log_content)

    def test_read_returns_log_contents(self):
        message = 'test'
        self.logger.log(message)
        log_content = self.logger.read().rstrip()

        # Check if the log content contains the message
        self.assertIn(message, log_content)

    def test_clear_empties_log(self):
        self.logger.log('test')
        self.assertNotEqual(self.logger.read(), '')
        self.logger.clear()
        self.assertEqual(self.logger.read(), '')

        

