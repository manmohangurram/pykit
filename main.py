from currency_coverter import Conveter
from search import search_engines
from youtube_download import downloader
import os

def clear():
    os.system('clear')

def banner():
    print('\033[01m'+'\033[33m'+'\033[01m')
    print('******************************')
    print('*   ____        _    _ _     *')   
    print('*  |  _ \ _   _| | _(_) |_   *') 
    print('*  | |_) | | | | |/ / | __|  *')
    print('*  |  __/| |_| |   <| | |_   *') 
    print('*  |_|    \__, |_|\_\_|\__|  *')
    print('*          ___/              *')
    print('******************************')

if __name__ == "__main__":
    while True:
        clear()
        banner()
        print('1.Search\n2.Currency Converter\n3.Vedio/Audio Downloader\n4.Exit')
        choice = input('Select your choice : ')
        if choice=='1':
            clear()
            banner()
            search = input('What do you like to search : ')
            num = input('Enter No.of results (default = 10 ) : ') or "10"
            s = search_engines(search,num)
            print('1.Google\n2.Bing')
            choice = input('Selet prefered search engine : ')
            if choice == '1': s.google_search()
            else: s.bing_search()
        if choice=='2':
            clear()
            banner()
            print("1.Converter")
            print("2.Country Codes")
            choice = input("Select an Option:")
            if choice=='1':
                Conveter.get_data()
            else:
                Conveter.print_currency_codes()
        elif choice=='3':
            clear()
            banner()
            print("1.Vedio Downloader\n2.Audio Downloader")
            choice = input("Select an Option:")
            url = input('Enter Vedio URL : ')
            location = input('Enter prefered Location (default = /home/mohan/Download/) : ') or "Downloads"
            if choice=='1':
                resolution = input('Enter prefered Format (default = 720 ) : ') or "720"
                d = downloader(url,resolution,location)
                d.vedio_download()
            else:
                resolution = input('Enter prefered Format (default = mp3 ) : ') or "mp3"
                d = downloader(url,resolution,location)
                d.audio_download()
        else: break