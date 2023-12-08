from string import ascii_lowercase, digits, punctuation
from unittest import main, TestCase
from main import caeser_encryption


class TestEncryption(TestCase):
    """  """
    def setUp(self):
        self.message = 'Apples are sweet and nutritious'
        

    def test_input_exists(self):
        self.assertIsNotNone(self.message)

    def test_input_type(self):
        self.assertIsInstance(self.message, str)

    # check if encryption() returns an output
    def test_encryption(self):
        self.assertIsNotNone(caeser_encryption(self.message))

    def test_lenIO(self):   # test the length of input & output 
        self.assertEqual(len(self.message), len(caeser_encryption(self.message)))
    
    def test_differentIO(self):
        self.assertNotIn(self.message, caeser_encryption(self.message))
    
    def test_output_type(self):     # test the data type of output, i.e. message
        self.assertIsInstance(caeser_encryption(self.message), str)
    
    def test_shifted_cipher(self):
        text = ascii_lowercase + punctuation + digits + ' '
        encrypt_msg = ''.join([text[text.find(char) + 1] if len(text) > (text.find(char) + 1) else text[0] for idx, char in enumerate(self.message)])
        print(encrypt_msg)
        self.assertEqual(encrypt_msg, caeser_encryption(self.message))



if __name__ == '__main__':
    main()