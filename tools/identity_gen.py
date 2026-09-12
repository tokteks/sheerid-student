import random, json, os
from datetime import datetime, timedelta
import time

FIRST_NAMES_M = ["James","Michael","Robert","John","David","William","Richard","Joseph","Thomas","Christopher","Daniel","Matthew","Anthony","Mark","Donald","Steven","Paul","Andrew","Joshua","Kenneth","Kevin","Brian","George","Timothy","Ronald","Edward","Jason","Jeffrey","Ryan","Jacob","Gary","Nicholas","Eric","Jonathan","Stephen","Larry","Justin","Scott","Brandon","Benjamin","Samuel","Raymond","Gregory","Frank","Alexander","Patrick","Jack","Dennis","Jerry","Tyler"]
FIRST_NAMES_F = ["Mary","Patricia","Jennifer","Linda","Barbara","Elizabeth","Susan","Jessica","Sarah","Karen","Lisa","Nancy","Betty","Margaret","Sandra","Ashley","Kimberly","Emily","Donna","Michelle","Carol","Amanda","Dorothy","Melissa","Deborah","Stephanie","Rebecca","Sharon","Laura","Cynthia","Kathleen","Amy","Angela","Shirley","Anna","Brenda","Pamela","Emma","Nicole","Helen","Samantha","Katherine","Christine","Debra","Rachel","Carolyn","Janet","Catherine","Maria","Olivia"]
LAST_NAMES = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts"]
STREETS = ["Oak St","Maple Ave","Elm St","Main St","Pine Rd","Cedar Ln","Birch Dr","Walnut Ave","Cherry St","Spruce Ct","Willow Way","Ash Blvd","Hickory Ln","Poplar Dr","Sycamore St","Beech Ave","Magnolia Ct","Dogwood Dr","Hemlock Way","Alder St","Aspen Cir","Fir Ln"]
CITIES_ZIPS = [("Phoenix","85001","AZ"),("Tucson","85701","AZ"),("Mesa","85201","AZ"),("Chandler","85224","AZ"),("Gilbert","85233","AZ"),("Glendale","85301","AZ"),("Scottsdale","85250","AZ"),("Tempe","85280","AZ"),("Dallas","75201","TX"),("Houston","77001","TX"),("Austin","73301","TX"),("San Antonio","78201","TX"),("Orlando","32801","FL"),("Miami","33101","FL"),("Tampa","33601","FL"),("Denver","80201","CO"),("Portland","97201","OR"),("Seattle","98101","WA"),("Las Vegas","89101","NV"),("Atlanta","30301","GA")]

class IdentityGenerator:
    def generate(self, gender=None):
        if gender is None:
            gender = random.choice(["M","F"])
        first = random.choice(FIRST_NAMES_M if gender=="M" else FIRST_NAMES_F)
        last = random.choice(LAST_NAMES)
        today = datetime.now()
        age = random.randint(17, 26)
        bday = today - timedelta(days=age*365 + random.randint(0, 364))
        birth_str = bday.strftime("%Y-%m-%d")
        city, zipcode, state = random.choice(CITIES_ZIPS)
        street = random.choice(STREETS)
        street_num = random.randint(100, 9999)
        area = random.choice(["602","480","520","623","928","214","512","407","303","702"])
        phone = f"{area}-{random.randint(200,999)}-{random.randint(1000,9999)}"
        email_local = f"{first.lower()}.{last.lower()}{random.randint(10,99)}"
        return {
            "first_name": first, "last_name": last, "full_name": f"{first} {last}",
            "gender": gender, "birth_date": birth_str, "email_local": email_local,
            "address": f"{street_num} {street}", "city": city, "state": state,
            "zip": zipcode, "phone": phone,
        }

    def to_text_block(self, i):
        return f"""=== IDENTITY #{i} ===
Name: {i['full_name']} ({i['gender']})
DOB: {i['birth_date']}
Address: {i['address']}, {i['city']}, {i['state']} {i['zip']}
Phone: {i['phone']}
Email local: {i['email_local']}
"""

if __name__ == "__main__":
    g = IdentityGenerator()
    for i in range(2):
        print(g.to_text_block(g.generate()))