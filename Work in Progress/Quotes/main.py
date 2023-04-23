# """Gives the user quotes on a subject the user requests. Allows the user to
# ask for instructions, look at a log of the quotes, and quit."""

# import time


# def clear_terminal():
#     """Clears the terminal of all text."""

#     print("\033c", end="")


# def print_instructions():
#     """Print out all of the instructions to the user."""

#     clear_terminal()
#     print("--- Instructions ---")

#     print("Press enter to get the next quote after receiving one")
#     print("Enter 'ls' to see a list of the quotes given with special information")
#     print("Enter '?' to see these instructions")
#     print("Enter 'q' to quit")

#     input("Press enter when you are ready")


# def main():
#     """
#     Run the main event loop of telling the user different quotes based on their choice of a
#     subject and allowing them to ask for instructions, look at a log of the quotes, and quit.
#     """

#     quote_log: list[str] = []
#     quote_subject = input("Enter the subject you would like to receive quotes on: ")
#     print_instructions()

#     while True:
#         clear_terminal()
#         quote = "place holder"
#         date_said = "place holder"
#         timestamp = time.time()
#         timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
#         quote_log.append(
#             f"Quote: {quote} || Said On: {date_said} || Quote Generated On: {timestamp}"
#         )
#         user_input = input(f"{quote} ")
#         if user_input == "q":
#             break
#         if user_input == "?":
#             print_instructions()
#         elif user_input == "ls":
#             clear_terminal()
#             for quote in quote_log:
#                 print(quote)
#                 print("-" * 100)

#             print()
#             input("Press enter to continue")


# if __name__ == "__main__":
#     main()
import requests

subject = "success"
test = f"https://quotes.rest/quote/search?minlength=100&maxlength=500&query={subject}"
response = requests.get(url=test, timeout=5)

if response.ok:
    data = response.json()
    if data["contents"]["quotes"]:
        quote = data["contents"]["quotes"][0]["quote"]
        author = data["contents"]["quotes"][0]["author"]
        print(f"{quote}\n- {author}")
    else:
        print(f"No quotes found on {subject}")
else:
    print(f"Error: {response.status_code}")
