import asyncio
import aiohttp
import re
import random
import pandas as pd
from playwright.async_api import async_playwright
import re
from constant import FILE_PATH
from get_data import ASIN,product_name, original_price, discounted_price, product_rating
import csv


df = pd.read_csv(FILE_PATH) #Reading CSV FILE USING PANDAS
extracted_urls = df['URL'] # Extract URLs from the DataFrame



async def open_urls(extracted_urls):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        async with aiohttp.ClientSession() as session:
            tasks = [process_url(url, browser, session) for url in extracted_urls]
            await asyncio.gather(*tasks)


async def process_url(url, browser, session):
    page = await browser.new_page()
    await page.set_viewport_size({"width": 1920, "height": 1080})
    await page.goto(url)
    await asyncio.sleep(random.uniform(2, 5))
    try:
        await extract_product_info(page, url, session)
    except Exception as e:
        print(f"Error processing {url}: {e}")
    finally:
        await page.close()

async def extract_product_info(page, url, session):
    Amazon_Standard_Identification_Number = await ASIN(page, url)
    PRODUCT_NAME = await product_name(page, url)
    ORIGINAL_PRICE = await original_price(page)
    DISCOUNTED_PRICE = await discounted_price(page)
    PRODUCT_RATING = await product_rating(page)

    print(f'The ASIN is {Amazon_Standard_Identification_Number}')
    print(f'The PRODUCT NAME is {PRODUCT_NAME}')
    print(f'The ORIGINAL PRICE is {ORIGINAL_PRICE}')
    print(f'The DISCOUNTED PRICE is {DISCOUNTED_PRICE}')
    print(f'The PRODUCT RATING is {PRODUCT_RATING}')


     # Write data to CSV file
    with open('Output.csv', 'a', newline='') as csvfile:
        fieldnames = ['URL','ASIN', 'PRODUCT_NAME', 'ORIGINAL_PRICE', 'DISCOUNTED_PRICE', 'PRODUCT_RATING']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

         # Write headers if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'URL': url,
            'ASIN': Amazon_Standard_Identification_Number,
            'PRODUCT_NAME': PRODUCT_NAME,
            'ORIGINAL_PRICE': ORIGINAL_PRICE,
            'DISCOUNTED_PRICE': DISCOUNTED_PRICE,
            'PRODUCT_RATING': PRODUCT_RATING
        })

asyncio.run(open_urls(extracted_urls))
