from typing import Dict, Callable

from utils.Printer import Printer
from utils.logger.LoggerFactory import LoggerFactory

type Options = Dict[str, Callable[[], None]]

class Menu:
    def __init__(self, options: Options):
        self.options = options

        self.printer = Printer()
        self.logger = LoggerFactory.make_logger('menu.log')

    def run(self):
        while True:
            self.printer.print('Please select an option from the menu below:\n')
            for option, action in self.options.items():
                self.printer.print(f'{option}. {action.__name__}\n')
            choice = input()
            action = self.options.get(choice)
            if action:
                action()
            else:
                self.printer.error('Invalid option')
