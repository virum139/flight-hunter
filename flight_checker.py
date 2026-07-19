from playwright.sync_api import sync_playwright
import re

print("Flight Hunter started")

url = "https://www.google.com/travel/flights/search?tfs=CBwQAhojEgoyMDI2LTA5LTAxagwIAhIIL20vMDJjZHRyBwgBEgNERUxAAUgBcAGCAQsI____________AZgBAg"

print("Opening Google Flights:")
print(url)

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Allow Google Flights results to load
    page.wait_for_timeout(10000)

    print("Page title:")
    print(page.title())

    # Read page text
    text = page.locator("body").inner_text()

    print("Searching prices...")

    # Find USD prices
    prices = re.findall(r'\$(\d+)', text)

    prices = [int(p) for p in prices]

    if prices:
        cheapest = min(prices)

        print("----------------------")
        print("CHEAPEST FARE FOUND")
        print("----------------------")
        print(f"USD {cheapest}")

    else:
        print("No prices found")

    # Save screenshot for checking
    page.screenshot(
        path="google_flights_result.png",
        full_page=True
    )

    browser.close()

print("Flight check completed")
