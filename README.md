# Session-Bruter
Instagram Session ID Brute-forcer

## Desctiption

Simple Instagram Session ID Brute-Forcer. You can even specify specific accounts to brute force them. 

![2022-10-08 11_47_23-Session Bruter py - Scripts under maintance - Visual Studio Code](https://user-images.githubusercontent.com/58238467/194702579-ee1abe9b-190f-4644-aed8-b25bee0f8a5f.png)

### The Instagram Session ID contains 3 strings seperated by a colon (:)
- String 1 contains `instagram user id `
- String 2 contains `14 random characters [A-Za-z0-9]`
- String 3 contains `random number between 0-30`


#### an example is going to be:
561\*\*\*\*\*54`:`UZWvH*****I0v4`:`28

With URL encoding:

561\*\*\*\*\*54`%3A`UZWvH\*\*\*\*\*I0v4`%3A`28

The program either generate random user-id, string and a number or you can add the targeted user-id's in a text file and the program will use them and generates only string and a number for them 
## How to start?
1. Clone the repository using `git clone` or copy the code if you prefer
2. Download the wanted libraries in the `requirements.txt`
3. Open the terminal or the command prompt and navigate to the folder you downloaded the repo
4. Make sure you have python 3 installed and run this command `python "Session Bruter.py"`
5. Follow the instructions on the terminal

> You must have proxies. Free proxies are useless in this situation so paid ones are highly recommended.

> The program supports HTTP/S, SOCKS4 and SOCKS5.

> All hits will be either sent on telegram or saved in Hits.txt

![2022-10-08 11_54_00-Session Bruter](https://user-images.githubusercontent.com/58238467/194703560-55c0a170-9647-44e2-af9b-d7557144d27f.png)

