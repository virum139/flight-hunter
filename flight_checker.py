from playwright.sync_api import sync_playwright
import re
import time
import urllib.parse

print("Flight Hunter started")

origin = "DAR"

# Indian destinations to check
destinations = [
    "DEL",
    "BOM",
    "JAI",
    "AMD",
    "PAT",
    "BLR",
    "HYD",
    "MAA"
]

results = []


def create_google_flights_url(destination):

    query = f"Flights from {origin} to {destination}"

    url = (
        "https://www.google.com/travel/flights?"
        f"q={urllib.parse.quote(query)}"
    )

    return url


with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    for destination in destinations:

        print("\n======================")
        print(f"Checking {destination}")
        print("======================")

        url = create_google_flights_url(destination)

        print(url)

        try:

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(10000)

            text = page.locator("body").inner_text()

            # Find realistic flight prices
            prices = re.findall(
                r'\$(\d{3,5})',
                text
            )

            prices = [
                int(price)
                for price in prices
                if int(price) >= 100
            ]

            if prices:

                cheapest = min(prices)

                print(
                    f"{destination}: USD {cheapest}"
                )

                results.append(
                    {
                        "city": destination,
                        "price": cheapest
                    }
                )

            else:

                print(
                    f"{destination}: No price found"
                )


        except Exception as e:

            print(
                f"{destination}: Error {e}"
            )


        time.sleep(3)


    browser.close()


if results:

    results.sort(
        key=lambda x: x["price"]
    )

    print("\n======================")
    print("CHEAPEST INDIA FARE")
    print("======================")

    print(
        "Route: DAR → "
        + results[0]["city"]
    )

    print(
        "Price: USD "
        + str(results[0]["price"])
    )

    print("\nAll results:")

    for result in results:

        print(
            result["city"],
            "USD",
            result["price"]
        )

else:

    print("No flights found")


print("\nFlight check completed")
