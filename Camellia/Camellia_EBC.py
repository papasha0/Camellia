from Camellia import Camellia_cls


class CamelliaECB:
    """
    Electronic codebook (ECB) Camellia operation mode.
    """
    def __init__(self, key):
        """
        Set the key to be used for en-/de-cryption.
        """
        self.camellia = Camellia_cls()
        self.camellia.set_key(key)

    def encrypt(self, plaintext):
        """
        Encrypt the given string using Camellia ECB.
        """
        if len(plaintext) % 16:
            raise RuntimeError("Camellia plaintext length must be a multiple of 16")
        ciphertext = b""
        while len(plaintext) >= 16:
            ciphertext += self.camellia.encrypt(plaintext[0:16])
            plaintext = plaintext[16:]
        return ciphertext

    def decrypt(self, ciphertext):
        """
        Decrypt the given string using Camellia ECB.
        """
        if len(ciphertext) % 16:
            raise RuntimeError("Camellia ciphertext length must be a multiple of 16")
        plaintext = b""
        while len(ciphertext) >= 16:
            plaintext += self.camellia.decrypt(ciphertext[0:16])
            ciphertext = ciphertext[16:]
        return plaintext


#def test_camellia_ecb():
#    __testkey = b"Now Testing Crypto-Functions...."
#    __testenc = b"Passing nonsense through crypt-API, will then do assertion check"
#    __testdec = b"\x71\xbf\x8a\xc5\x8f\x6c\x2d\xce\x9d\xdb\x85\x82\x5b\x25\xe3\x8d\xd8\x59\x86\x34\x28\x7b\x58\x06\xca\x42\x3d\xab\xb7\xee\x56\x6f\xd3\x90\xd6\x96\xd5\x94\x8c\x70\x38\x05\xf8\xdf\x92\xa4\x06\x2f\x32\x7f\xbd\xd7\x05\x41\x32\xaa\x60\xfd\x18\xf4\x42\x15\x15\x56"
#    assert CamelliaECB(__testkey).decrypt(__testenc) == __testdec
#    assert CamelliaECB(__testkey).encrypt(__testdec) == __testenc


#test_camellia_ecb()

