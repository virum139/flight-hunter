from playwright.sync_api import sync_playwright
import re
import time
import urllib.parse

print("Flight Hunter started")

origin = "DAR"
date = "2026-09-01"

# Major Indian airports
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
    "GAU",
    "IXC",
    "IXB",
    "NAG",
    "BBI",
    "IXR"
]

results = []


def make_url(destination):

    query = (
        f"Flights from {origin} to {destination} "
        f"on {date}"
    )

    return (
        "https://www.google.com/travel/flights?"
        f"q={urllib.parse.quote(query)}"
    )


with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    for destination in destinations:

        print("\n======================")
        print(f"Checking {origin} → {destination}")
        print("======================")

        url = make_url(destination)

        print(url)

        try:

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            # Wait for Google Flights results
            page.wait_for_timeout(12000)

            text = page.locator("body").inner_text()

            # Extract realistic flight prices
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

                cheapest = min(prices)

                print(
                    f"{destination}: USD {cheapest}"
                )

                results.append(
                    (
                        destination,
                        cheapest
                    )
                )

            else:

                print(
                    f"{destination}: No fare found"
                )

        except Exception as e:

            print(
                f"{destination}: Error"
            )


        time.sleep(3)


    browser.close()



if results:

    results.sort(
        key=lambda x: x[1]
    )

    print("\n======================")
    print("CHEAPEST INDIA FARE")
    print("======================")

    print(
        f"DAR → {results[0][0]}"
    )

    print(
        f"USD {results[0][1]}"
    )

    print("\nAll fares:")

    for city, price in results:
        print(
            city,
            "USD",
            price
        )

else:

    print("No flights found")


print("\nFlight check completed")
