from BrowserHandler import BrowserHandler
from ProductHandler import product
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Handle OS and browser
    browser_handler = BrowserHandler()
    browser_properties = browser_handler.get_properties()
    logging.debug(f'Browser properties: {browser_properties}')
    # get product
    prod = product()
    # get price
    price = prod.create_soup()
    logging.debug(f'The price of our product in runtime is {price}')