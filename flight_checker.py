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

    print("Changing origin...")

    # Origin field
    origin = page.locator("input").nth(0)
    origin.click()
    origin.fill("DAR")

    page.wait_for_timeout(3000)

    # Select suggestion
    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")

    page.wait_for_timeout(3000)


    print("Changing destination...")

    # Destination field
    destination = page.locator("input").nth(2)

    destination.click()
    destination.fill("DEL")

    page.wait_for_timeout(3000)

    page.keyboard.press("ArrowDown")
    page.keyboard.press("Enter")


    page.wait_for_timeout(3000)


    print("Taking screenshot")

    page.screenshot(
        path="flight_form_test.png",
        full_page=True
    )


    print("Current URL:")
    print(page.url)


    browser.close()


print("Test completed")
