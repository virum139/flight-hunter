from playwright.sync_api import sync_playwright
import requests
import os
from datetime import datetime

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

routes = [
    ("DEL", "New Delhi"),
    ("BOM", "Mumbai")
]

travel_date = "2026-09-01"


def send_photo(file_path, caption):

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(file_path, "rb") as photo:

        response = requests.post(
            url,
            files={
                "photo": photo
            },
            data={
                "chat_id": CHAT_ID,
                "caption": caption
            }
        )

    print("--------------------------------")
    print("Telegram Status Code:", response.status_code)
    print("Telegram Response:")
    print(response.text)
    print("--------------------------------")

    if response.status_code == 200:
        print("Telegram notification sent successfully.")
    else:
        print("Telegram notification FAILED.")


print("===================================")
print("Flight Hunter Started")
print("===================================")

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page(
        viewport={
            "width": 1920,
            "height": 1080
        }
    )

    for code, name in routes:

        print()
        print("===================================")
        print(f"Checking DAR → {code}")
        print("===================================")

        url = (
            "https://www.google.com/travel/flights?"
            f"q=Flights%20from%20DAR%20to%20{code}"
            f"%20on%20{travel_date}"
        )

        print("Opening:")
        print(url)

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        print("Waiting for page to load...")

        page.wait_for_timeout(30000)

        filename = (
            f"{code}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )

        print("Taking screenshot...")

        page.screenshot(
            path=filename,
            full_page=False
        )

        print("Screenshot saved:", filename)

        caption = f"""✈️ Flight Hunter

DAR → {name} ({code})

One Way

Travel Date:
01 September 2026

Checked:
{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}

Google Flights Screenshot"""

        send_photo(
            filename,
            caption
        )

    browser.close()

print()
print("===================================")
print("Flight Hunter Completed")
print("===================================")
