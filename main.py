import os
import time
import json
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
BROWERS_EXECUTABLE_PATH = os.getenv("BROWERS_EXECUTABLE_PATH")
SITE_URL_ONE = os.getenv("SITE_URL_ONE")


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=BROWERS_EXECUTABLE_PATH, headless=False)
    context = browser.new_context()

    # Load cookies
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
        context.add_cookies(cookies)

    page = context.new_page()
    page.goto(SITE_URL_ONE)
    time.sleep(5)
    page.wait_for_selector("span.components-home-assets-__sign-guide_---guide-close---2VvmzE")
    page.click("span.components-home-assets-__sign-guide_---guide-close---2VvmzE")
    time.sleep(5)
    page.evaluate("document.querySelector('div.components-home-assets-__sign-content-test_---actived-day---34r3rb').click()")
    time.sleep(5)

    # Save cookies
    cookies = context.cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)

    browser.close()