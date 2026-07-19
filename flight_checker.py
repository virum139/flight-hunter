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

    inputs = page.locator("input")

    print("Total inputs:", inputs.count())

    for i in range(inputs.count()):

        element = inputs.nth(i)

        print("----------------")
        print("INPUT", i)

        print(
            "Placeholder:",
            element.get_attribute("placeholder")
        )

        print(
            "Value:",
            element.input_value()
        )

        print(
            "Type:",
            element.get_attribute("type")
        )


    browser.close()

print("Inspection completed")
