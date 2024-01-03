/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send GET request and display debugging info
response=$(curl -s -w "\n%{http_code}" "$1")
statusCode=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

echo "HTTP status code: $statusCode"
echo "Response body:"
