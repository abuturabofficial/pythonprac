import requests
# import json


def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ConnectionError):
        print("Couldn't complete the API call! Try again.")
        return

    content = response.json()
    # Print pretty data using JSON module
    # print(json.dumps(content, indent=4))
    for artwork in content["data"]:
        print(f"* {artwork["title"]}")


main()
