from requests import get
from pprint import PrettyPrinter

apiKey = "62204b7b-e3cc-4d2b-98b2-c50c36a58a04"
baseUrl = "https://free.currconv.com/"
printer = PrettyPrinter()


def getCurrencies():
    endpoint = f"api/v7/currencies?apiKey={apiKey}"
    url = baseUrl + endpoint
    data = get(url).json()["results"]
    data = list(data.items())
    data.sort()
    return data


def printCurrencies(currencies):
    for name, currency in currencies:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchangeRate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={apiKey}"
    url = baseUrl + endpoint
    data = get(url).json()
    if len(data) == 0:
        print("Invalid Currencies")
        return
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    rate = exchangeRate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid Input")
        return
    convertedAmount = rate * amount
    print(f"{amount} {currency1} is equal to {convertedAmount} {currency2}")
    return convertedAmount


def main():
    currencies = getCurrencies()
    while True:
        try:
            command = int(
                input(
                    "Enter Command [1. See Currencies 2. See Exchange Rates 3. Convert]: "
                )
            )
        except Exception:
            print("Invalid Command")
            main()
        if command == 1:
            printCurrencies(currencies)
        elif command == 2:
            currency1 = input("Enter Base Currency: ").upper()
            amount = input(f"Enter Amount In {currency1}: ")
            currency2 = input("Enter Currency To Convert To: ").upper()
            convert(currency1, currency2, amount)
        elif command == 3:
            currency1 = input("Enter A Base Currency: ").upper()
            currency2 = input("Enter Currency To Convert To: ").upper()
            exchangeRate(currency1, currency2)
        else:
            print("Invalid Command")


main()
