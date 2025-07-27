# Cheap Flight Finder for Users

A Python application that monitors flight prices for specified routes and sends notifications via SMS and email when a cheap flight deal is found. The app fetches flight data through the Amadeus API, stores user requests in a Google Sheet, updates IATA codes, and alerts users of price drops.

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup and Installation](#setup-and-installation)
    - [Virtual Environment Setup](#virtual-environment-setup)
    - [Install Dependencies](#install-dependencies)
4. [Usage](#usage)
5. [Google Sheet Setup](#google-sheet-setup)
6. [Dependencies](#dependencies)
7. [Notes](#notes)
8. [License](#license)

## Features

- Fetches and updates IATA airport codes from a JSON file.
- Retrieves user flight deal requests and contact info from a Google Sheet (via Sheety API).
- Searches for flights on Amadeus API for the next 7 days.
- Sends SMS notifications using Twilio.
- Sends email alerts using SMTP (Gmail).
- Supports multiple users with personalized deal criteria and contact info.
- Environment variables for sensitive credentials management.

## Project Structure

    .
    ├── main.py 
    ├── data_manager.py 
    ├── flight_search.py 
    ├── notification_manager.py 
    ├── iata_codes.json
    └── requirements.txt

.main.py                 # Entry point to update data and trigger flight searches & notifications.
.data_manager.py         # Handles Google Sheet data retrieval and IATA code updates.
.flight_search.py        # Connects to Amadeus API to find cheapest flights.
.notification_manager.py # Sends SMS and email notifications.
.iata_codes.json         # Stores city-to-IATA airport code mapping.
.requirements.txt        # Python dependencies.
    

## Setup and Installation

### 1. Clone the Repository

git clone https://github.com/bala-aswin-yaganti/cheap_flight_finder-for-users.git
cd cheap_flight_finder-for-users

### 2. Create and Activate a Virtual Environment (Recommended)

#### For macOS/Linux


### 2. Create and Activate a Virtual Environment (Recommended)

#### For macOS/Linux

    python3 -m venv env
    source env/bin/activate

#### For Windows
    
    python -m venv env
    env\Scripts\activate


### 3. Install Dependencies

    pip install -r requirements.txt


### 4. Create a `.env` File in the Project Root

Sample `.env` file (replace placeholders with actual values):

    Sheety API endpoint URL for your Google Sheet
    
    SHEETY_ENDPOINT=https://api.sheety.co/your_project/your_sheet
    Amadeus API credentials (Client ID and Client Secret)
    
    AMADEUS_CLIENT_ID=your_amadeus_client_id_here
    AMADEUS_CLIENT_SECRET=your_amadeus_client_secret_here
    Twilio credentials for sending SMS
    
    TWILIO_SID=your_twilio_account_sid_here
    TWILIO_AUTH=your_twilio_auth_token_here
    TWILIO_PHONE=+1234567890
    Target phone number to receive SMS notifications (in E.164 format)
    
    TARGET_PHONE=+919876543210
    Email credentials for sending email notifications
    
    EMAIL=your_email@example.com
    EMAIL_PWD=your_email_password_or_app_specific_password


> **Note:** Keep your `.env` file private; never commit it to a public repository.

### 5. Ensure `iata_codes.json` Includes City to IATA Mappings (already provided).

## Usage

Run the main script:

    python main.py


The program will:

- Update missing IATA codes in your Google Sheet.
- Fetch flight deal requests.
- Search for the cheapest flights in the next 7 days.
- Notify users by SMS and email if the flight price is below their target price.

## Google Sheet Setup

The Google Sheet connected via Sheety should contain columns like:

| id | cityFrom | cityTo | iataFrom | iataTo | maxPrice | email             | phone       |
|----|----------|--------|----------|--------|----------|-------------------|-------------|
| 1  | Paris    | Tokyo  | PAR      | TYO    | 15000    | user@example.com  | 9876543210  |

- `iataFrom` and `iataTo` can be auto-updated by the app if left empty.
- `maxPrice` sets the maximum price threshold to trigger notifications.
- `email` and `phone` are used for alerts.

## Dependencies

- Amadeus Python SDK
- requests
- python-dotenv
- twilio
- smtplib (built-in)
- email (built-in)

## Notes

- Make sure your Twilio phone number and target phone number are configured correctly.
- The Gmail account used for notifications may require an app password or allow less secure apps.
- The app currently prefixes Indian phone numbers with +91 for SMS; adjust as needed.
- Be aware of API rate limits; add retries or logging as desired.

## License

This project is licensed under the MIT License.

---

If you want any additional sections or tweaks, feel free to ask!
