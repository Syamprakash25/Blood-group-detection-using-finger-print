import requests

BASE_URL = "http://127.0.0.1:5000"

def test_signup(username, password):
    print(f"Attempting signup for {username}...")
    response = requests.post(f"{BASE_URL}/signup", data={
        "username": username,
        "password": password,
        "email": "test@example.com" # Sending email as form does
    }, allow_redirects=True)
    
    print(f"Status Code: {response.status_code}")
    print(f"Final URL: {response.url}")
    if "Login" in response.text or "/login" in response.url:
        print("Signup successful (redirected to login)")
    elif "Username already exists" in response.text:
        print("Signup failed: Username already exists")
    else:
        print("Signup failed: Unknown reason")
        # print(response.text)

if __name__ == "__main__":
    test_signup("testuser_123", "password123")
