import requests
"""Note: this use the ExchangeRate-API to get the exchange rate data"""

# Define a function to convert currencies
def currency_converter(amount, from_currency, to_currency):
    # Set the API endpoint for currency conversion
    api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    # Send a GET request to the API endpoint
    response = requests.get(api_endpoint)
    # Get the JSON data from the response
    data = response.json()
    # Extract the exchange rate for the target currency
    exchange_rate = data["rates"][to_currency]
    # Calculate the converted amount
    converted_amount = amount * exchange_rate
    # Return the converted amount
    return converted_amount

# Prompt the user to enter the amount, source currency, and target currency
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency code: ").upper()
to_currency = input("Enter the target currency code ").upper()

# Convert the currency and print the result
result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")