import pytest
import GuiFunctions as test

def test_input_validation_zip():
    assert test.input_validation_zip("12345") == str("This is a valid zipcode.")
    assert test.input_validation_zip("123A5") == str("This is not a valid zipcode!")

def test_input_validation_phone():
    assert test.input_validation_phone("1234567891") == str("This is a valid phone number.")
    assert test.input_validation_phone("123BB67891") == str("This is not a valid phone number!")