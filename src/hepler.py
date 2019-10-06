import os


def has_data_on_file():
    dirPath = os.path.dirname(os.path.abspath(__file__))
    fileRead = open(f"{dirPath}/config/conf-01.txt", "r")
    data = fileRead.read()
    return data

def get_dec_data(data):
    def normalize(str):
        str = str.replace(' ', '')
        return " ".join(str[i:i+8] for i in range(0, len(str), 8))
    def dec(str):
        str = normalize(str)
        return ''.join(chr(int(binary, 2)) for binary in str.split(' '))

    dec_data = dec(str(data))
    return dec_data


def save_enc_data(token_obj):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    fileWrite = open(f"{dirPath}/config/conf-01.txt", "w")
    def enc(str):
        return ' '.join(bin(ord(char)).split('b')[1].rjust(8, '0') for char in str)
    token_obj = enc(str(token_obj))
    fileWrite.write(token_obj)
    fileWrite.close()