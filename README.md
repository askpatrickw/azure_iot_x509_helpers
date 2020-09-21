# azure_iot_x509_helpers

X509 Helpers to create self-signed certs for use with Azure IoT.

Also generates Device IDs in GUID format and primary and secondary certificate
for each device.

> The .gitignore for this repro does not track .pem files.
> Don't commit your keys and certs to public repos.
> Don't commit your passphrases either (in config.py)

## Setup Requirements

`pip install cryptography`

NOTE: At the time of publishing was using Python 3.8.5 and cryptography 3.1.

Based on sample code from the cryptography library docs:
https://cryptography.io/en/latest/x509/tutorial/#creating-a-self-signed-certificate

## Usage

Where you see "run the file", you can right click in VSCode or from the cli `python script_name.py`

1. Edit `config.py` and enter your company information and your passphrases.
2. Run `x509_1_keys.py`
3. Run `x509_2_certs.py`
4. Go to your IoT Central application /admin/device-connection/ and create or edit an enrollment group.
5. Import the primary certicate, copy the validation Code into `config.py`. Keep this page open in your web browser. IF you close it, the validation code will change. 
6. Run `x509_3_validation_certs.py` go back to your IoT Central application /admin/device-connection/ and upload the validation certificate. Your primary cert should now be valid with a greem check mark.
7. Repeat steps 5 & 6 for your secondary certificate on the enrollment group.
8. SAVE the enrollment group.
9. Use `x509_4_device_certs.py` to generate device ids with a primary and secondary certificates for each device.

For more information on connecting to Azure IoT Central: https://docs.microsoft.com/en-us/azure/iot-central/core/concepts-get-connected
