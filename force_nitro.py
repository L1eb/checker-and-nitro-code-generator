import random
import requests

char = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9" 
char_sep = char.split(" ")
def gen_password(pass_len):
    password = "" 
    random_nbr = 0
    i = 0
    while i < pass_len: 
        random_nbr = random.randint(0, len(char_sep) - 1) 
        password = password + char_sep[random_nbr]
        i += 1 
    return password
    
continue_prog = True 
for i in range(100):
    true = '  [+]'
    false = '  [X]'
    final_password = gen_password(16)
    link = 'https://discord.gift/'
    redeem = "redeem"
    tel = final_password + '/' + redeem
    url = 'https://discordapp.com/api/v6/entitlements/gift-codes/reedem'
    z = requests.get('https://discordapp.com/api/v6/entitlements/gift-codes/', params=tel)

    if z.status_code == 200:
        print(z.url.replace('?','')+ true)
    elif z.status_code > 400:
        print(z.url.replace('?','')+ false)
        e = link + final_password + false
        

        



    choice = input()
