import json

import requests


def main():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    api_key = "aZ28VGAAOqeFzkx3Df9KcwDkuXFw5624VSZCngxT"
    params = {"Mozilla/5.0": "(X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
              "api_key": api_key,
              "earth_date": "2021-06-30"  # невідомо чому але це остання дата до якої працюе цей алгоритм:-
              # 2021-06-30 (від себе без офіційної лексики дата тут працюе ...йово)
              }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # print(response.status_code)
        with open('nasa_photo.json', 'w', encoding='utf-8') as file_json:
            json.dump(response.json(), file_json, ensure_ascii=False, indent=4)

    with open('nasa_photo.json', 'r', encoding='utf-8') as file_json:
        photo = json.load(file_json)
        # print(photo)
        # photo = response.json()["photos"]
        # print(f"Finde{len(photo)} photos")
        # print(photo[99]['img_src'])
        for photos in photo['photos']:
            all_photos = [photos['img_src']]
            print(all_photos)


main()
