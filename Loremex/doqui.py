# Example data to write to the file
data = {
    'token': 'your_token_here',
    'expiry': '2024-12-31'
}

# Writing data to 'token.json'
with open('token.json', 'w') as token:
    json.dump(data, token)

print("Data successfully written to 'token.json'")
