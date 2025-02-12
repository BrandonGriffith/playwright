import os
import time
import json
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from a .env file
load_dotenv()
BROWERS_EXECUTABLE_PATH = os.getenv("BROWERS_EXECUTABLE_PATH")
SITE_URL_ONE = os.getenv("SITE_URL_ONE")

# Start a Playwright session
with sync_playwright() as p:
    # Launch the browser with the specified executable path and in non-headless mode
    browser = p.chromium.launch(executable_path=BROWERS_EXECUTABLE_PATH, headless=False)
    context = browser.new_context()

    # Load cookies from a JSON file and add them to the browser context
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
        context.add_cookies(cookies)

    # Open a new page and navigate to the specified URL
    page = context.new_page()
    page.goto(SITE_URL_ONE)
    time.sleep(5)  # Wait for the page to load

    # Wait for the guide close button to appear and click it
    page.wait_for_selector("span.components-home-assets-__sign-guide_---guide-close---2VvmzE")
    page.click("span.components-home-assets-__sign-guide_---guide-close---2VvmzE")
    time.sleep(5)  # Wait for the action to complete

    # Click on the active day element
    page.evaluate("document.querySelector('div.components-home-assets-__sign-content-test_---actived-day---34r3rb').click()")
    time.sleep(5)  # Wait for the action to complete

    # Save the current cookies to a JSON file
    cookies = context.cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)

    # Close the browser
    browser.close()