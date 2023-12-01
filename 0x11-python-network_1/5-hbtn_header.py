#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
        else:
            print("X-Request-Id header not found in the response.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error making the request: {e}")
        sys.exit(1)
