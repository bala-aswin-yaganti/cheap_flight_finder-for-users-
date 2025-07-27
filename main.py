from dotenv import load_dotenv
load_dotenv()

import os
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notifier = NotificationManager()

# Update TARGET_PHONE_NUMBER in .env from sheet
target_phone_number = data_manager.get_latest_phone_number()

if target_phone_number:
    # Ensure it's a 10-digit number and add +91 prefix
    formatted_number = f"+91{str(target_phone_number)[-10:]}"
    print(f"✅ Using phone number from sheet: {formatted_number}")
    os.environ["TARGET_PHONE_NUMBER"] = formatted_number
else:
    print("❌ No phone number found.")

# Step 1: Update IATA codes if missing
data_manager.update_iata_codes()

# Step 2: Get flight deal requests from Google Sheet
deals = data_manager.get_destinations()

# Step 3: Check flights and notify if price below target
for deal in deals:
    from_code = (deal.get("iataFrom") or "").strip()
    to_code = (deal.get("iataTo") or "").strip()
    target_price = float(deal.get("maxPrice") or 0)
    user_email = (deal.get("email") or "").strip()

    if not from_code or not to_code or target_price == 0 or not user_email:
        print("Skipping incomplete deal:", deal)
        continue

    flight = flight_search.search_flight(from_code, to_code)

    if flight and flight["price"] < target_price:
        msg = (
            f"Low price alert! Only ₹{flight['price']} to fly from "
            f"{flight['cityFrom']} to {flight['cityTo']} on {flight['dateFrom']}."
        )
        print("Sending notification:", msg)
        notifier.send_sms(msg)
        notifier.send_email("Flight Deal Alert", msg, user_email)
    else:
        print("❌ Not a good deal.")
