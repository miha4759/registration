from classes.Registration import Registration

if __name__ == '__main__':
    phone = input('Input phone(like 7XXXXXXXXXX): ')

    registration = Registration(phone)

    print(registration.try_register_phone())

exit()
