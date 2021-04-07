from faker import Faker
fake_data=Faker()
name=fake_data.name()
print(name)
address=fake_data.address()
print (address)
email=fake_data.safe_email()
print (email)

#profile

profile=fake_data.simple_profile()
for k,v in profile.items():
    print('{}: {} ' .format(k,v))

#jobs
    from faker import Faker
    faker = Faker()
    for _ in range(6):
        print(faker.job())

        # Location

        from faker import Faker
        faker = Faker('cz_CZ')
        for i in range(3):
            name = faker.name()
            address = faker.address()
            phone = faker.phone_number()

            print(f'{name}, {address}, {phone}')

            # random numbers

            from faker import Faker

            faker = Faker()

            print(f'Random int: {faker.random_int()}')
            print(f'Random int: {faker.random_int(0, 100)}')
            print(f'Random digit: {faker.random_digit()}')

            from faker import Faker

            faker = Faker()

            print(f'Email: {faker.email()}')
            print(f'Safe email: {faker.safe_email()}')
            print(f'Free email: {faker.free_email()}')
            print(f'Company email: {faker.company_email()}')

            print('------------------------------------')

            print(f'Host name: {faker.hostname()}')
            print(f'Domain name: {faker.domain_name()}')
            print(f'Domain word: {faker.domain_word()}')
            print(f'TLD: {faker.tld()}')

            print('------------------------------------')

            print(f'IPv4: {faker.ipv4()}')
            print(f'IPv6: {faker.ipv6()}')
            print(f'MAC address: {faker.mac_address()}')

            print('------------------------------------')

            print(f'Slug: {faker.slug()}')
            print(f'Image URL: {faker.image_url()}')