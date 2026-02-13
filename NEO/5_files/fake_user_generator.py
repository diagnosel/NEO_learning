from faker import Faker

fake = Faker("uk_UA")

def generate_fake_data():

    return {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone_number": fake.phone_number(),
            "password": fake.password()
        }
    


