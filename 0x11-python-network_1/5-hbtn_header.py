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

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("No X-Request-Id found in the response headers.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
