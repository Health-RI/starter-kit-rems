from json import dumps
from authlib.jose import jwk
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

public_key_file = "public-key.json"
private_key_file = "private-key.json"

if __name__ == "__main__":

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend(),
    )
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    public_jwk = jwk.dumps(public_key, kty="RSA")
    private_jwk = jwk.dumps(pem, kty="RSA")

    with open(public_key_file, "w") as f:
        f.write(dumps(public_jwk, indent=4))
        print(f"wrote {public_key_file}")
    with open(private_key_file, "w") as f:
        f.write(dumps(private_jwk, indent=4))
        print(f"wrote {private_key_file}")
