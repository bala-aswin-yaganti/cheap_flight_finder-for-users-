import os
from datetime import datetime, timedelta
from amadeus import Client, ResponseError
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        self.amadeus = Client(
            client_id=os.getenv("AMADEUS_CLIENT_ID"),
            client_secret=os.getenv("AMADEUS_CLIENT_SECRET"),
            hostname='production'  # ✅ Use production API for real prices
        )

    def search_flight(self, from_code, to_code):
        start_date = datetime.today()
        lowest_price = None
        best_flight = {}

        for i in range(7):  # Check next 7 days
            date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
            print(f"🛫 Checking flights on: {date}")

            try:
                response = self.amadeus.shopping.flight_offers_search.get(
                    originLocationCode=from_code,
                    destinationLocationCode=to_code,
                    departureDate=date,
                    adults=1,
                    max=1
                )
                if response.data:
                    price = float(response.data[0]['price']['total'])
                    currency = response.data[0]['price']['currency']
                    print(f"💸 Found: {price} {currency}")

                    if lowest_price is None or price < lowest_price:
                        lowest_price = price
                        best_flight = {
                            "price": price,
                            "currency": currency,
                            "dateFrom": date,
                            "cityFrom": from_code,
                            "cityTo": to_code
                        }

            except ResponseError as e:
                print(f"❌ Error on {date}: {e}")
                continue

        return best_flight if best_flight else None
