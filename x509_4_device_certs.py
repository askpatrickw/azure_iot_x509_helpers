"""
Create a Device ID and a Device Certificate for use with Azure IoT Hub

    Based on sample code from the cryptography library docs:
    https://cryptography.io/en/latest/x509/tutorial/#creating-a-self-signed-certificate
"""

import datetime
from pathlib import Path
import uuid

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography import x509
from cryptography.x509.oid import NameOID

from config import COMPANY_INFO, PASSPHRASE, PATH_TO_CERTS, VALID_DAYS

device_id = str(uuid.uuid4())
print(f"Device ID: {device_id}")

for key_name in PASSPHRASE.keys():
    pem_data = open(f"{PATH_TO_CERTS}{key_name}/key.pem", "rb").read()
    key = serialization.load_pem_private_key(pem_data, PASSPHRASE[key_name])

    issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, COMPANY_INFO['COUNTRY']),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, COMPANY_INFO['STATE']),
            x509.NameAttribute(NameOID.LOCALITY_NAME, COMPANY_INFO['CITY']),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, COMPANY_INFO['NAME']),
        ]
    )

    subject = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, f"{device_id}"),])

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(
            datetime.datetime.utcnow()
            + datetime.timedelta(days=VALID_DAYS)
        )
        .sign(key, hashes.SHA256())
    )
    path = Path(f"{PATH_TO_CERTS}{key_name}/devices")
    path.mkdir(parents=True, exist_ok=True)
    filename = f"{path}/{device_id}.pem"
    with open(filename, "xb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))

    print(f"\t{key_name.capitalize()} Cert: {filename}")
