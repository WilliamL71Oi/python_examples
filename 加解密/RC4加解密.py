from Crypto.Cipher import ARC4 as rc4cipher
import base64

def rc4_algorithm(encrypt_or_decrypt, data, key1):
    if encrypt_or_decrypt == "encrypt":
        key = bytes(key1, encoding='utf-8')
        enc = rc4cipher.new(key)
        res = enc.encrypt(data.encode('utf-8'))
        res=base64.b64encode(res)
        res = str(res,'utf8')
        return res
    elif encrypt_or_decrypt == "decrypt":
        data = base64.b64decode(data)
        key = bytes(key1, encoding='utf-8')
        enc = rc4cipher.new(key)
        res = enc.decrypt(data)
        res = str(res,'utf8')
        return res


if __name__ == "__main__":
    data = '测试'
    key = 'l2ru8181z'
    print(rc4_algorithm('encrypt',data,key))
    res ='dLzb09qr'
    print(rc4_algorithm('decrypt', res, key))
