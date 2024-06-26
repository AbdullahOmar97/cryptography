import unittest
from crypto_module.crypto import encrypt, decrypt

class TestCryptography(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(encrypt("abc", 1), "bcd")

    def test_encrypt_wrap(self):
        self.assertEqual(encrypt("xyz", 1), "yza")

    def test_encrypt_mixed_case(self):
        self.assertEqual(encrypt("aBc", 1), "bCd")

    def test_decrypt_basic(self):
        self.assertEqual(decrypt("bcd", 1), "abc")

    def test_decrypt_wrap(self):
        self.assertEqual(decrypt("yza", 1), "xyz")

    def test_decrypt_mixed_case(self):
        self.assertEqual(decrypt("bCd", 1), "aBc")

if __name__ == "__main__":
    unittest.main()
