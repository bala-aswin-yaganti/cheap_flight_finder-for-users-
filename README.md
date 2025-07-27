Cheap Flight Finder for Users

A Python application that monitors flight prices for specified routes and sends notifications via SMS and email when a cheap flight deal is found. The app fetches flight data through the Amadeus API, stores user requests in a Google Sheet, updates IATA codes, and alerts users of price drops.

Features

- Fetches and updates IATA airport codes from a JSON file.
- Retrieves user flight deal requests and contact info from a Google Sheet (via Sheety API).
- Searches for flights on Amadeus API for the next 7 days.
- Sends SMS notifications using Twilio.
- Sends email alerts using SMTP (Gmail).
- Supports multiple users with personalized deal criteria and contact info.
- Environment variables for sensitive credentials management.

Project Structure

- main.py - Entry point to update data and trigger flight searches & notifications.
- data_manager.py - Handles Google Sheet data retrieval and IATA code updates.
- flight_search.py - Connects to Amadeus API to find cheapest flights.
- notification_manager.py - Sends SMS and email notifications.
- iata_codes.json - Stores city-to-IATA airport code mapping.
- requirements.txt - Python dependencies.

Setup and Installation

1. Clone the repository

    git clone https://github.com/bala-aswin-yaganti/cheap_flight_finder-for-users.git
    cd cheap_flight_finder-for-users

2. Create and activate a virtual environment (optional but recommended)

    python3 -m venv env
   
    source env/bin/activate   # macOS/Linux
   
    env\Scripts\activate      # Windows

4. Install dependencies

    pip install -r requirements.txt

5. Create a .env file in the project root with the following variables:

    SHEETY_ENDPOINT=<Your Sheety API endpoint URL>
    AMADEUS_CLIENT_ID=<Your Amadeus SDK Client ID>
    AMADEUS_CLIENT_SECRET=<Your Amadeus SDK Client Secret>
    TWILIO_SID=<Your Twilio Account SID>
    TWILIO_AUTH=<Your Twilio Auth Token>
    TWILIO_PHONE=<Your Twilio phone number>
    TARGET_PHONE=<Target phone number for SMS in E.164 format, e.g. +919876543210>
    EMAIL=<Your email address used for sending emails>
    EMAIL_PWD=<Password or app-specific password for the email>

6. Ensure iata_codes.json includes city to IATA mappings (already provided).

Usage

Run the main script:

    python main.py

The program will:

- Update missing IATA codes in your Google Sheet.
- Fetch flight deal requests.
- Search for the cheapest flights on the next 7 days.
- Notify users by SMS and email if the flight price is below their target price.

Google Sheet Setup

The Google Sheet connected via Sheety should contain columns similar to:

| id | cityFrom | cityTo | iataFrom | iataTo | maxPrice | email         | phone         |
|----|----------|--------|----------|--------|----------|---------------|---------------|
| 1  | Paris    | Tokyo  | PAR      | TYO    | 15000    | user@example.com | 9876543210    |

- iataFrom and iataTo can be auto-updated by the app if left empty.
- maxPrice sets the maximum price threshold to trigger notifications.
- email and phone are used to send alerts.

Dependencies

- Amadeus Python SDK
- requests
- python-dotenv
- twilio
- smtplib (built-in)
- email (built-in)

Notes

- Make sure your Twilio phone number and target phone number are configured correctly.
- Gmail account used for email notifications must allow less secure apps or use app passwords.
- The app currently prefixes Indian phone numbers with +91 for SMS; modify as needed.
- Handle API rate limits and errors with retries or logging as desired.

License

This project is licensed under the MIT License.
