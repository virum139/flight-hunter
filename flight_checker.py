from playwright.sync_api import sync_playwright

print("Flight Hunter started")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://www.skyscanner.net")

    print("Opened Skyscanner")

    print("Page title:")
    print(page.title())

    browser.close()

print("Test completed")
