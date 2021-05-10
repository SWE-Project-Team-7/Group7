def input_validation_zip(zipcode):
    try:
        int(zipcode)
        return str("This is a valid zipcode.")
    except ValueError:
            return str("This is not a valid zipcode!")


def input_validation_phone(phoneNum):
    try:
        int(phoneNum)
        return str("This is a valid phone number.")
    except ValueError:
        return str("This is not a valid phone number!")