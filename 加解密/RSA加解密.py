import re
import base64
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

message = "hello client, this is a message"

'''
# Server的秘钥对的生成
private_pem = rsa.exportKey().decode('utf-8')
private_pem = str(private_pem).replace(r"\n",'\n')
print(private_pem)

with open("server-private.pem", "w") as f:
    f.write(str(private_pem))

public_pem = rsa.publickey().exportKey().decode('utf-8')
private_pem = str(public_pem).replace(r"\n",'\n')
print(private_pem)
with open("server-public.pem", "w") as f:
    f.write(str(public_pem))


# Client的秘钥对的生成
private_pem = rsa.exportKey()
with open("client-private.pem", "w") as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open("client-public.pem", "w") as f:
    f.write(public_pem)


# rsa加密
with open(r"C:\Users\WilliamL71Oi\Desktop\server-public.pem") as f:
    key = f.read()
    print(type(key))
    rsakey = RSA.importKey(key)
    print(type(rsakey))
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    print(cipher_text)
    print(cipher_text.decode('utf-8'))


# rsa解密
with open("server-private.pem") as f:
    encrypt_text = 'FWi4VtPsZDhR74WqBCSFf5K1L/ixsOp5nJeSXgBDTU5ikQjEJLYo/ing3mRaW51SB+2ZPSifWLphz+UgZJvh7zyuhRPAsVuBNb+MWniZH0Pxz2VfgjQdhO3AamKRaQ+W5JFdpaRpaN9dL8KKgdWgLVRLSdQUwVsqqVMZUO5P0VM='
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    print(text.decode('utf-8'))
'''

# 数字签名
# Server使用自己的私钥对内容进行签名
with open("server-private.pem") as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    signer = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    digest.update(message.encode('utf-8'))
    sign = signer.sign(digest)
    signature = base64.b64encode(sign)
    print(signature)

# 签名验签
# Client使用Server的公钥对内容进行验签

with open("server-public.pem") as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(message)
    is_verify = verifier.verify(digest, base64.b64decode(signature))
    print(is_verify)




