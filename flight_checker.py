from playwright.sync_api import sync_playwright
from urllib.parse import quote

print("Flight Hunter started")

origin = "DAR"
destination = "DEL"
date = "2026-09-01"

# Google Flights one-way search URL
url = "https://www.google.com/travel/flights/search?tfs=CBwQAhojEgoyMDI2LTA5LTAxagwIAhIIL20vMDJjZHRyBwgBEgNERUxAAUgBcAGCAQsI____________AZgBAg"

print(url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    print("Title:")
    print(page.title())

    import re

text = page.locator("body").inner_text()

prices = re.findall(r'\$(\d+)', text)

prices = [int(p) for p in prices]

if prices:
    cheapest = min(prices)
    print("Cheapest fare found:")
    print("$" + str(cheapest))
else:
    print("No prices found")

    browser.close()

print("Completed")
