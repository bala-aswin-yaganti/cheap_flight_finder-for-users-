import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    def __init__(self, iata_file="iata_codes.json"):
        with open(iata_file, "r") as file:
            self.iata_codes = json.load(file)

    def get_sheet_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()

        try:
            data = response.json()
            return data["formResponses1"]

        except ValueError:
            print("❌ Could not parse JSON from response. Check the URL or API.")
            print(f"Response text was: {response.text}")
            return []
        except KeyError:
            print("❌ 'formResponses1' key not found in response JSON. Full JSON:")
            print(data)
            return []


    def update_iata_codes(self):
        data = self.get_sheet_data()
        for row in data:
            updated_data = {}

            from_city = row["cityFrom"].strip()
            to_city = row["cityTo"].strip()

            if not row.get("iataFrom") and from_city in self.iata_codes:
                updated_data["iataFrom"] = self.iata_codes[from_city]

            if not row.get("iataTo") and to_city in self.iata_codes:
                updated_data["iataTo"] = self.iata_codes[to_city]

            if updated_data:
                body = {"formResponses1": updated_data}
                response = requests.put(f"{SHEETY_ENDPOINT}/{row['id']}", json=body)
                response.raise_for_status()


    def get_destinations(self):
        return self.get_sheet_data()

    def get_latest_phone_number(self):
        data = self.get_sheet_data()
        if not data:
            return None

        # Assuming the latest response is the last entry
        latest_entry = data[-1]

        # Replace "phoneNumber" with your actual column name in the Sheet
        return latest_entry.get("phone")


