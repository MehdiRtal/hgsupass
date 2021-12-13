import hashlib

def suPassword(chall):
    premd5 = bytearray(8)
    for i in range(8):
        if ord(chall[i]) <= 0x47:
            premd5[i]=ord(chall[i])<<1
        else:
            premd5[i]=ord(chall[i])>>1
    
    md5hash = hashlib.md5()
    md5hash.update(premd5)
    print("MD5:",md5hash.hexdigest())
    prepass = bytearray(md5hash.digest())

    challpass = bytearray(8)
    for i in range(8):
        temp2=(prepass[i]>>1)*0xB60B60B7
        temp2=temp2>>(5+32)
        temp1=temp2<<3
        temp1=temp1-(temp2<<1)
        temp3=(temp1<<4)
        temp3=temp3-temp1
        temp0=prepass[i]-temp3+0x21
        temp0=temp0&0xFF
        if temp0 == 0x3F:
            challpass[i]=0x3E
        else:
            challpass[i]=temp0
    print("Password:",challpass.decode())

print("Huawei HG8245 SU Challenge Verification Generator")
print("Challenge:")
challenge = input()

if len(challenge)==8:
    suPassword(challenge)
else:
    print("Challenge must have 8 chars")
