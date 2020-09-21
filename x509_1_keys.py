"""
Generate a Primary and Secondary Private Key
"""
from pathlib import Path
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from config import PASSPHRASE, PATH_TO_CERTS


for key_name in PASSPHRASE.keys():
    path = Path(f"{PATH_TO_CERTS}{key_name}")
    path.mkdir(parents=True, exist_ok=True)
    filename = f"{path}/key.pem"
    _key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    with open(filename, "xb") as f:
        f.write(
            _key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.BestAvailableEncryption(
                    PASSPHRASE[key_name]
                ),
            )
        )
    print(f"{key_name.capitalize()} Key: {filename}")
