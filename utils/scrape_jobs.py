from playwright.async_api import async_playwright
import asyncio
import json
from bs4 import BeautifulSoup  # Import BeautifulSoup
from utils.config import scrape_config  # Import config from config.py


async def scrape_single_page(page, url, selector, wait_for_selector_timeout):
    await page.goto(url)
    page_content = {'url': url}
    try:
        if selector:
            try:
                # Attempt to wait for the selector
                await page.wait_for_selector(selector, timeout=wait_for_selector_timeout)
                elements = await page.query_selector_all(selector)
                if elements:  # If elements are found with the selector
                    page_content['content'] = [await element.text_content() for element in elements]
                else:  # If no elements are found, parse the body instead
                    raise Exception("Selector not found")
            except Exception as e:
                # If the selector is not found or any other exception occurs, parse the body instead
                content = await page.content()
                soup = BeautifulSoup(content, 'html.parser')
                # Check if soup.body is not None before calling get_text
                if soup.body:
                    body_text = soup.body.get_text(separator=' ', strip=True)
                    page_content['content'] = body_text
                else:
                    page_content['content'] = "Error: Body content not found"
        else:
            # If no selector is provided, directly parse the body
            await page.wait_for_timeout(wait_for_selector_timeout)
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            # Check if soup.body is not None before calling get_text
            if soup.body:
                body_text = soup.body.get_text(separator=' ', strip=True)
                page_content['content'] = body_text
            else:
                page_content['content'] = "Error: Body content not found"
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")
        page_content['content'] = "Error: Could not retrieve content"
    return page_content


async def scrape(config):
    urls = config['url'] if isinstance(config['url'], list) else [config['url']]
    selector = config.get('selector', None)
    wait_for_selector_timeout = config.get('wait_for_selector_timeout', 5000)
    output_to_file = config.get('output_to_file', False)
   

    scraped_data = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        )
        page = await context.new_page()

        for url in urls:
            content = await scrape_single_page(page, url, selector, wait_for_selector_timeout)
            scraped_data.append(content)
      

        await browser.close()

    if output_to_file:
        with open('output.json', 'w') as f:
            json.dump(scraped_data, f, indent=4)

    return scraped_data

def scrape_jobs():
 
    return asyncio.run(scrape(scrape_config))

if __name__ == "__main__":
    result = scrape_jobs()



