import random
simple = ['home1','wood123','cat7','dog43']
hard = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

men = input('Do you want your password long or short?')
if men == 'short':
    print(random.choice(simple))
else:
    password = ""
    for i in range(25):
        password += random.choice(hard)
    print(password)

    

