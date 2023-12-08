from string import ascii_lowercase, digits, punctuation


def caeser_encryption(message):
    """ Caesar's cipher algorithm. """

    text = ascii_lowercase + punctuation + digits + ' '
    encrypt_msg = ''.join([text[text.find(char) + 1] if len(text) > (text.find(char) + 1) else text[0] for idx,  char in enumerate(message)])
    return encrypt_msg
