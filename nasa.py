import requests
import os
import ctypes


url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
FILENAME = r"C:\Users\andreas\Documents\Projects\python-nasabackground\nasa_pic.jpg"


def download_pic():
    r = requests.get(url)

    if r.status_code != 200:
        print("Error")
        return

    picture_url = r.json()["url"]
    if "jpg" not in picture_url:
        print("No image found")
    else:
        pic = requests.get(picture_url, allow_redirects=True)
        filename = FILENAME
        open(filename, "wb").write(pic.content)
        print("Saved picture of the day")


if __name__ == "__main__":
    download_pic()
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, FILENAME, 3)
    # set_wallpaper(FILENAME)
    # os.system(cmd)
