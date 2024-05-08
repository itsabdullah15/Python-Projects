import re
from constant import ORIGINAL_PRICE_XPATH, DISCOUNT_PRICE_XPATH, PRODUCT_PRICE_XPATH, \
    ASIN_REGEX, PRODUCT_NAME_REGEX

async def ASIN(page, url):
    try:
        product_code = re.search(ASIN_REGEX, url).group(1)
        return product_code
    except AttributeError:
        print("ASIN not found in URL:", url)
        return None

async def product_name(page, url):
    try:
        match = re.search(PRODUCT_NAME_REGEX, url)
        if match:
            product_id = match.group(1)
            return product_id
        else:
            return None
    except Exception as e:
        print("Error extracting product name:", e)
        return None

async def original_price(page):
    try:
        price_element = await page.query_selector(ORIGINAL_PRICE_XPATH)
        if price_element:
            original_price = await price_element.text_content()
            return original_price
        else:
            return None
    except Exception as e:
        print("Error extracting original price:", e)
        return None

async def discounted_price(page):
    try:
        discount_price_element = await page.query_selector(DISCOUNT_PRICE_XPATH)
        if discount_price_element:
            discount_price = await discount_price_element.text_content()
            return discount_price
        else:
            return None
    except Exception as e:
        print("Error extracting discounted price:", e)
        return None

async def product_rating(page):
    try:
        product_rating_element = await page.query_selector(PRODUCT_PRICE_XPATH)
        if product_rating_element:
            product_rating = await product_rating_element.text_content()
            return product_rating
        else:
            return None
    except Exception as e:
        print("Error extracting product rating:", e)
        return None
