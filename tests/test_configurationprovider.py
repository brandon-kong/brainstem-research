import unittest

from providers.ConfigurationProvider import ConfigurationProvider

from utils.logger.LoggerFactory import LoggerFactory
from utils.Printer import Printer

from utils.constants import LOGGER_FILE_SUFFIX

logger = LoggerFactory.make_logger(LOGGER_FILE_SUFFIX, f'test{LOGGER_FILE_SUFFIX}')


class TestConfigurationProvider(unittest.TestCase):
    def setUp(self):
        self.config_provider = ConfigurationProvider()

    def test_add_configuration_stores_data_correctly(self):
        self.config_provider.add_configuration('test', 'test')
        self.assertEqual(self.config_provider.get_configuration('test'), 'test')

    def test_add_configuration_stores_data_correctly_with_nested_key(self):
        self.config_provider.add_configuration('test1/test2', 'test')
        self.assertEqual(self.config_provider.get_configuration('test1/test2'), 'test')

    def test_add_configuration_stores_data_correctly_with_multiple_nested_keys(self):
        self.config_provider.add_configuration('test1/test3', 'test')
        self.assertEqual(self.config_provider.get_configuration('test1/test3'), 'test')

    def test_add_configuration_overrides_existing_data(self):
        self.config_provider.add_configuration('test', 'test')
        self.config_provider.add_configuration('test', 'test1')
        self.assertEqual(self.config_provider.get_configuration('test'), 'test1')

    def test_add_configuration_raises_error_for_invalid_key(self):
        with self.assertRaises(ValueError) as context:
            self.config_provider.add_configuration('test/test2', 'test2')

    def test_load_configuration_stores_data_correctly(self):
        configuration = {'test': 'test'}
        valid_keys = {'test': str}
        self.config_provider.load_configuration(configuration, valid_keys)
        self.assertEqual(self.config_provider.get_configuration('test'), 'test')

    def test_load_configuration_error_for_invalid_key(self):
        configuration = {'invalid': 'test'}
        valid_keys = {'test': str}

        self.config_provider.load_configuration(configuration, valid_keys)
        self.assertNotIn('invalid', self.config_provider.keys())

    def test_load_configuration_error_for_invalid_type(self):
        configuration = {'test': 123}
        valid_keys = {'test': str}

        self.config_provider.load_configuration(configuration, valid_keys)

        self.assertIn('test', self.config_provider.keys())

    def test_get_configuration_returns_none_for_nonexistent_key(self):
        self.assertIsNone(self.config_provider.get_configuration('nonexistent'))
