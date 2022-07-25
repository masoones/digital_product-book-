from django.core.validators import RegexValidator


class PhoneNumberValidators(RegexValidator):
    regex = '^98(9[0-3,9]\d{8}[1-9]\d{9})$'
    massage = 'Phone Number must be VALID 12 digits like 98xxxxxxxxxx.'
    code = 'invalid_phone_number'


class SKUValidators(RegexValidator):
    regex = '^[a-zA-Z0-9\-\]{6,20}$'
    massage = 'SKU must be alphanumeric with 6 to 20 characters.'
    code = 'invalid_sku'


class UsernameValidators(RegexValidator):
    regex = '^[a-zA-Z][a-zA-Z0-9_\.]+$'
    message = 'Enter a valid username starting with a-z.''This value may contain only letters, numbers and underscore characters.'
    code = 'invalid_username'


class PostalCodeValidators(RegexValidator):
    regex = '^[0-9]{10}$'
    massage = 'Enter a valid Postal code. '
    code = 'invalid_postal_code'


class IDNumberValidators(RegexValidator):
    regex = '^[0-9]{10}$'
    massage = 'Enter a valid id number. '
    code = 'invalid_id_number'


class IBanNumberValidators(RegexValidator):
    regex = '^[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}$'
    massage = 'Enter a valid iban number. '
    code = 'invalid_iban_number'


class BankCardNumberValidators(RegexValidator):
    regex = '^[0-9]{16}$'
    massage = 'Enter a valid card number. '
    code = 'invalid_card_number'


validate_phone_number = PhoneNumberValidators
validate_sku = SKUValidators
validate_username = UsernameValidators
validate_postal_code = PostalCodeValidators
validate_id_number = IDNumberValidators
validate_iban_number = IBanNumberValidators
validate_caard_number = BankCardNumberValidators
