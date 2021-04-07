from faker import Faker
fake_data=Faker()
name=fake_data.name()
print(name)
address=fake_data.address()
print (address)
