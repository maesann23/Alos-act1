import uuid
from bs4 import BeautifulSoup
import urllib3
import random
from faker import Faker
import json


def phone_generator():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]


fake = Faker(locale="en_US")


def generate_pet_owner(owner_id):

    name = fake.name()
    email = fake.email()
    address = fake.address()
    phone = phone_generator()
    return {"id": owner_id, "name": name, "email": email, "address": address, phone: phone}


urls = ["https://www.petamberalert.com/lost-pet-list/?action=search&pet_type=Dog&pet_gender=&pet_breed=&pet_zipcode=&pet_miles=25&search_lost_pet=Search", "https://www.petamberalert.com/lost-pet-list/?pg=25&action=search&pet_type=Dog&pet_miles=25",
        "https://www.petamberalert.com/lost-pet-list/?action=search&pet_type=Cat&pet_gender=&pet_breed=&pet_zipcode=&pet_miles=50&search_lost_pet=Search", "https://www.petamberalert.com/lost-pet-list/?pg=25&action=search&pet_type=Cat&pet_miles=25"]
index = 0
owners = []
pets = []

for url in urls:
    http_pool = urllib3.connection_from_url(url)
    page = http_pool.urlopen('GET', url).data.decode('utf-8')

    soup = BeautifulSoup(page)
    table_content = soup.select("#table_lost_pets tr")

    for item in table_content:
        owner_id = str(uuid.uuid4())
        colums = item.select("td")
        owners.append(generate_pet_owner(owner_id))
        pets.append({"id": index, "lost_date": colums[0].get_text(), "image_src": colums[1].select_one("img")["src"].replace("../..", "https://www.petamberalert.com"), "pet_name": colums[2].select_one(
            "a").get_text(), "breed": colums[3].get_text(), "zip_code": colums[4].get_text(), "posted_date": colums[5].get_text(), "ownerId": owner_id})
        index += 1


with open('db.json', 'w') as outfile:
    outfile.write(json.dumps({"owners": owners, "pets": pets}))
