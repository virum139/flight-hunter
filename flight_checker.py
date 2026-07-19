from playwright.sync_api import sync_playwright

print("Flight Hunter started")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://www.google.com/travel/flights",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    print("Google Flights opened")

    print("Page title:")
    print(page.title())

    text = page.locator("body").inner_text()

    print(text[:2000])

    page.screenshot(
        path="google_flights_test.png",
        full_page=True
    )

    browser.close()

print("Test completed")
