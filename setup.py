import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import pprint

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def start_setup():
    """
    start_setup() -> dict

    Returns Twitter Friends Json file for certain account name
    Max number of friends data - 15

    """
    print('\nThis is a module for getting Friends Json file for certain account')
    print('')
    acct = input('Enter Twitter Account Name: ')
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '15'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    return js

def search(js):
    """
    dict -> None
    dict -> dict
    dict -> list
    dict -> str
    dict -> int
    dict -> float
    dict -> bool

    Makes console interfaced search platform
    for data from twitter json file

    Type 'E' to exit, 'B' to go back, 'R' to return current item and exit

    Returns none if exit ('E') or certain type for item if return ('R')
    """
    temp = 0
    erlist = ["\n!!! You can not go back further !!!", "\n!!! Type int number in correct range !!!", "\n!!! Not found try again !!!"]
    er = -1
    history = []
    inputik = "Hello there"
    cur_item = js
    print("\nThis is a module for observing a Json file")
    print("You can 'open catalogs' by typing the name of the dict key, or by typing an index of an item")
    print("To go back type 'B'\nTo exit type 'E'\nTo return and exit type'R'")
    while True:
        print('\nCatalogs or files:')
        if type(cur_item) == dict:
            for i in cur_item:
                print('-', i)
            if er != -1:
                print(erlist[er])
                er = -1
            inputik = input('\nSelect catalog (name, str): ')
            if inputik == "R":
                print("Returning current item...")
                return cur_item
            if inputik == "B":
                try:
                    cur_item = history[-1]
                    history.remove(history[-1])
                except:
                    er = 0
            elif inputik == "E":
                break
            else:
                try:
                    checkpoint = cur_item[inputik]
                    history.append(cur_item)
                    cur_item = checkpoint
                except:
                    er = 2
        elif type(cur_item) == list:
            temp = 0
            for i in cur_item:
                print("\nItem index:", temp, "\n")
                pprint.pprint(i)
                temp += 1
            if er != -1:
                print(erlist[er])
                er = -1
            print("\nNumber of items: ", temp)
            inputik = input('\nSelect item index (number, int, <!> start = 0 <!>): ')
            if inputik == "R":
                print("Returning current item...")
                return cur_item
            if inputik == "B":
                try:
                    cur_item = history[-1]
                    history.remove(history[-1])
                except:
                    er = 0
            elif inputik == "E":
                break
            else:
                try:
                    inputik = int(inputik)
                    checkpoint = cur_item[inputik]
                    history.append(cur_item)
                    cur_item = checkpoint
                except:
                    er = 1
        else:
            print("\nCurrent file:", cur_item)
            if er != -1:
                print(erlist[er])
                er = -1
            inputik = input("\nNo more catalogs to open\nTo exit type - E\nTo go back type - B\nTo return current item - R\nYour input: ")
            if inputik == "R":
                print("\nReturning current item...")
                return cur_item
            if inputik == "B":
                try:
                    cur_item = history[-1]
                    history.remove(history[-1])
                except:
                    er = 0
            if inputik == "E":
                break

    print("\nFinished succesfully")

if __name__ == "__main__":
    print("Returned - ", search(start_setup()))
