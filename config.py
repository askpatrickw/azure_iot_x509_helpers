"""
This file contains all the personsalization settings for these scripts.

REMEMBER: Save Passphrases, and store them in a secret and safe place.
"""

# Required to run scripts 1 and 2
COMPANY_INFO = {
    "NAME": "FAKE COMPANY, LLC",
    "COUNTRY": "US",
    "STATE": "WA",
    "CITY": "SEATTLE",
}

# Required to run scripts 1 and 2
PASSPHRASE = {
    "primary": b"primarypassphrase",
    "secondary": b"secondarypassphrase"
}

# Required to run script 3
# Validation Data is only input once you have uploaded your certs to IoT Central
AZURE_IOT_VERIFICATION_CODE = {
    "primary": "11111111",
    "secondary": "22222222"
}

# Certificates are valid for
VALID_DAYS = 10

# You can leave this alone
PATH_TO_CERTS = "./certs/"

