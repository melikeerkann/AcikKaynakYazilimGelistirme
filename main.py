import requests

def get_api_list():
    url = "https://api.github.com/repos/public-apis/public-apis/contents/APIs.json"
    response = requests.get(url)

    if response.status_code == 200:
        api_list = response.json()
        return api_list
    else:
        return None

def print_api_list(api_list):
    if api_list:
        for api in api_list:
            print(api["name"])
    else:
        print("API listesi alınamadı.")

if __name__ == "__main__":
    api_list = get_api_list()
    print_api_list(api_list)
