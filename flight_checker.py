from playwright.sync_api import sync_playwright
from urllib.parse import quote

print("Flight Hunter started")

origin = "DAR"
destination = "DEL"

departure_date = "2026-09-01"

google_flights_url = (
    "https://www.google.com/travel/flights?"
    f"q={quote(origin)}%20to%20{quote(destination)}%20"
    f"on%20{quote(departure_date)}"
)

print("Opening:")
print(google_flights_url)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        google_flights_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(10000)

    print("Page title:")
    print(page.title())

    text = page.locator("body").inner_text()

    print("---- PAGE TEXT ----")
    print(text[:3000])

    page.screenshot(
        path="google_flights_search.png",
        full_page=True
    )

    browser.close()

print("Search test completed")
