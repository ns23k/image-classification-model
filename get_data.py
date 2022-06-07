import os
from GoogleImageScrapper import GoogleImageScraper
from patch import webdriver_executable

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    fileobj=open("things.txt")
    lines = fileobj.readlines()
    search_keys = [line.strip() for line in lines]

    #Parameters
    number_of_images = 50
    headless = False
    min_resolution=(0,0)
    max_resolution=(9999,9999)

    #Main program
    for search_key in search_keys:
        image_scrapper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
        image_urls = image_scrapper.find_image_urls()
        image_scrapper.save_images(image_urls)
