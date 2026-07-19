from playwright.sync_api import sync_playwright
import time

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

    # Origin
    page.locator("input").nth(0).click()
    page.locator("input").nth(0).fill("DAR")
    page.wait_for_timeout(2000)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

    page.wait_for_timeout(2000)

    # Destination
    page.locator("input").nth(2).click()
    page.locator("input").nth(2).fill("DEL")
    page.wait_for_timeout(2000)
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

    page.wait_for_timeout(3000)

    print("Opening date picker")

    # Click departure field
    page.locator("input").nth(4).click()

    page.wait_for_timeout(3000)

    print("Page text around date:")
    text = page.locator("body").inner_text()

    print(text[:2000])

    page.screenshot(
        path="date_picker_test.png",
        full_page=True
    )

    browser.close()

print("Date test completed")
