import requests

BASE_URL = "http://127.0.0.1:5000"

def test_signup_flow():
    s = requests.Session()
    
    # 1. Successful Signup
    print("1. Testing successful signup...")
    resp = s.post(f"{BASE_URL}/signup", data={
        "username": "unique_user",
        "email": "unique@example.com",
        "password": "password"
    })
    if "Login" in resp.text or "/login" in resp.url:
        print("PASS: Signup successful")
    else:
        print("FAIL: Signup failed")

    # 2. Duplicate Username
    print("\n2. Testing duplicate username...")
    resp = s.post(f"{BASE_URL}/signup", data={
        "username": "unique_user",
        "email": "other@example.com",
        "password": "password"
    })
    if "Username or Email already exists" in resp.text:
        print("PASS: Duplicate username caught")
    else:
        print("FAIL: Duplicate username allowed")

    # 3. Duplicate Email
    print("\n3. Testing duplicate email...")
    resp = s.post(f"{BASE_URL}/signup", data={
        "username": "other_user",
        "email": "unique@example.com",
        "password": "password"
    })
    if "Username or Email already exists" in resp.text:
        print("PASS: Duplicate email caught")
    else:
        print(f"FAIL: Duplicate email allowed. Status: {resp.status_code}")
        # print("Response text snippet:", resp.text[:500])

if __name__ == "__main__":
    test_signup_flow()
