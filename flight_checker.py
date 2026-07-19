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

    url = (
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    )

    with open(file_path, "rb") as photo:

        requests.post(
            url,
            files={
                "photo": photo
            },
            data={
                "chat_id": CHAT_ID,
                "caption": caption
            }
        )


print("Flight Hunter Started")


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )


    page = browser.new_page(
        viewport={
            "width":1920,
            "height":1080
        }
    )


    for code, name in routes:


        print("====================")
        print(
            f"Checking DAR → {code}"
        )


        url = (
            "https://www.google.com/travel/flights?"
            f"q=Flights%20from%20DAR%20to%20{code}"
            f"%20on%20{travel_date}"
        )


        print(url)


        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )


        page.wait_for_timeout(30000)


        filename = (
            f"{code}_{datetime.now().strftime('%Y%m%d_%H%M')}.png"
        )


        page.screenshot(
            path=filename,
            full_page=False
        )


        send_photo(
            filename,
            f"""
✈️ Flight Hunter

DAR → {name} ({code})

One way
Travel date:
01 September 2026

Checked:
{datetime.now().strftime('%d-%m-%Y %H:%M')}

Google Flights screenshot
"""
        )


        print(
            "Sent:",
            filename
        )


    browser.close()


print("Completed")
