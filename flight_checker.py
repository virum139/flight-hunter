from playwright.sync_api import sync_playwright
import re
import time

print("Flight Hunter started")

destinations = [
    "DEL",
    "BOM",
    "BLR",
    "HYD",
    "MAA",
    "CCU",
    "AMD",
    "JAI",
    "PAT",
    "LKO",
    "COK",
    "PNQ",
    "GOI",
    "TRV",
    "GAU"
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


        # Origin
        inputs = page.locator("input")

        inputs.nth(0).click()
        inputs.nth(0).fill("DAR")

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")


        page.wait_for_timeout(3000)


        # Destination
        inputs.nth(2).click()
        inputs.nth(2).fill(destination)

        page.wait_for_timeout(2000)

        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")


        page.wait_for_timeout(3000)


        # Open date picker
        inputs.nth(4).click()

        page.wait_for_timeout(3000)


        # Select September 1
        try:
            page.get_by_text("September", exact=True).first.click()

            page.wait_for_timeout(1000)

            page.get_by_text("1", exact=True).first.click()

            page.wait_for_timeout(2000)

        except:

            print("Date selection failed")


        # Search
        buttons = page.get_by_text("Done", exact=True)

        if buttons.count():

            buttons.first.click()

        page.wait_for_timeout(10000)


        text = page.locator("body").inner_text()


        prices = re.findall(
            r'\$(\d{3,5})',
            text
        )


        prices = [
            int(x)
            for x in prices
            if 100 <= int(x) <= 5000
        ]


        if prices:

            price = min(prices)

            print(
                destination,
                "USD",
                price
            )

            results.append(
                (destination, price)
            )

        else:

            print(
                destination,
                "No fare found"
            )


    browser.close()



if results:

    results.sort(
        key=lambda x:x[1]
    )


    print("\n======================")
    print("CHEAPEST INDIA FARE")
    print("======================")


    print(
        "DAR →",
        results[0][0]
    )

    print(
        "USD",
        results[0][1]
    )


else:

    print("No results found")


print("Flight Hunter completed")
