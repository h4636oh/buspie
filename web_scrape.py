# XPATHS
# EACH CARD DIV: //div[@class="IHKeM"]
# BUS NAME: //div[@class="IHKeM"]//div[@class="+iUf5"]
# BUS TYPE: //div[@class="IHKeM"]//div[@class="G88l9"]
# DEPATURE TIME: //div[@class="IHKeM"]//div[@class="wYtCy"]//div[@class="_4rWgi"]
# DEPATURE DATE: //div[@class="IHKeM"]//div[@class="wYtCy"]//div[@class="C3vrs"]
# ARRIVAL TIME: //div[@class="IHKeM"]//div[@class="EjC2U"]//div[@class="_4rWgi"]
# ARRIVAL DATE: //div[@class="IHKeM"]//div[@class="EjC2U"]//div[@class="_4rWgi"]
# DURATION: //div[@class="IHKeM"]//div[@class="_1D2hF"]
# FINAL PRICE: //div[@class='IHKeM']//span[@class="A2eT9 F+C81"]
# INITIAL PRICE: //div[@class='IHKeM']//span[@class="i6vdL ifd4l"]
# RATING: //div[@class="IHKeM"]//div[@class="eoyaT"]/div
# SEATS AVAILABLE: //div[@class="IHKeM"]//div[@class="UxGbP"][1] // returns a text needs to be split by space and gets index 0 item

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json

from generate_url import generate_paytm_bus_url

def get_bus_data(url: str):
    """
    Scrapes bus details from the Paytm bus search page.
    
    :param url: Paytm bus search URL
    :return: List of bus details in JSON format
    """
    options = Options()
    options.add_argument("--headless")
    service = Service("chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    buses = []
    cards = driver.find_elements(By.XPATH, "//div[@class='IHKeM']")

    for card in cards:
        try:
            bus_name = card.find_element(By.XPATH, ".//div[@class='+iUf5']").text
            bus_type = card.find_element(By.XPATH, ".//div[@class='G88l9']").text
            departure_time = card.find_element(By.XPATH, ".//div[@class='wYtCy']//div[@class='_4rWgi']").text
            departure_date = card.find_element(By.XPATH, ".//div[@class='wYtCy']//div[@class='C3vrs']").text
            arrival_time = card.find_element(By.XPATH, ".//div[@class='EjC2U']//div[@class='_4rWgi']").text
            arrival_date = card.find_element(By.XPATH, ".//div[@class='EjC2U']//div[@class='_4rWgi']").text
            duration = card.find_element(By.XPATH, ".//div[@class='_1D2hF']").text
            final_price = card.find_element(By.XPATH, ".//span[@class='A2eT9 F+C81']").text
            initial_price = card.find_element(By.XPATH, ".//span[@class='i6vdL ifd4l']").text
            rating = card.find_element(By.XPATH, ".//div[@class='eoyaT']/div").text
            seats_available = card.find_element(By.XPATH, ".//div[@class='UxGbP'][1]").text.split()[0]

            bus_info = {
                "bus_name": bus_name,
                "bus_type": bus_type,
                "departure_time": departure_time,
                "departure_date": departure_date,
                "arrival_time": arrival_time,
                "arrival_date": arrival_date,
                "duration": duration,
                "final_price": final_price,
                "initial_price": initial_price,
                "rating": rating,
                "seats_available": seats_available
            }
            buses.append(bus_info)
        except Exception as e:
            print(f"Error extracting data for a bus: {e}")
    
    driver.quit()
    return json.dumps(buses, indent=4)

url = generate_paytm_bus_url("delhi", "mumbai", "2025-02-10")
print(get_bus_data(url))