from playwright.sync_api import sync_playwright

print("Flight Hunter started")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        "https://www.skyscanner.net",
        wait_until="networkidle",
        timeout=60000
    )

    print("Page loaded")

    print("Title:")
    print(page.title())

    text = page.locator("body").inner_text()

    print(text[:2000])

    page.screenshot(
        path="skyscanner_test.png",
        full_page=True
    )

    browser.close()

print("Test completed")
