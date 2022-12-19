#import random
import requests

def primary():
  #   print("Keep it logically awesome.")

# Make a GET request to the quote API
  response = requests.get("https://api.quotable.io/random")

# Check the status code of the response
  if response.status_code == 200:
    # If the request is successful, parse the JSON response
    quote = response.json()
    print(quote['content'])
    print("- " + quote['author'])
  else:
    # If the request is not successful, print an error message
    print("An error occurred:", response.status_code)

if __name__== "__main__":
  primary()
