from playwright.sync_api import sync_playwright
import re
import time

print("Flight Hunter started")

destinations = [
    "DEL",
    "BOM",
    "BLR"
]

results = []

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    for destination in destinations:

        print("\n======================")
        print(f"Checking DAR → {destination}")
        print("======================")

        page.goto(
            "https://www.google.com/travel/flights",
            wait_until="domcontentloaded",
            timeout=60000
        )

        page.wait_for_timeout(5000)

        print("Google Flights opened")

        # Click first input
        inputs = page.locator("input")

        print("Inputs found:", inputs.count())

        time.sleep(2)

    browser.close()

print("Test completed")
