from playwright.sync_api import sync_playwright
from datetime import datetime
import os

print("Flight Hunter Screenshot Mode Started")

routes = [
    "DEL",
    "BOM",
    "BLR",
    "JAI",
    "PAT"
]

os.makedirs("screenshots", exist_ok=True)


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page(
        viewport={
            "width": 1440,
            "height": 1200
        }
    )


    for destination in routes:

        print("======================")
        print(f"Checking DAR → {destination}")
        print("======================")


        url = (
            "https://www.google.com/travel/flights?"
            f"q=Flights%20from%20DAR%20to%20{destination}"
        )


        print(url)


        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )


        # allow results to load
        page.wait_for_timeout(15000)


        filename = (
            f"screenshots/"
            f"DAR_{destination}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M')}.png"
        )


        page.screenshot(
            path=filename,
            full_page=True
        )


        print("Saved:", filename)


    browser.close()


print("Screenshot collection completed")
