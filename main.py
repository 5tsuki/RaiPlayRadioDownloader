import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Download audio files from RaiPlayRadio')
parser.add_argument("-l", "--link", type=str, required=True, dest='link', help="Define playlist link")
parser.add_argument("-v", "--verbose", required=False, help="Increase output verbosity", action="store_true")
args = parser.parse_args()

link = args.link

if __name__ == "__main__":
    page = requests.get(link)
    soup = BeautifulSoup(page.content, features="html.parser")
    elencoPlaylist = soup.find_all('li', attrs={'role':'playlist-item'})
    for i, elemento in enumerate(elencoPlaylist):
        currentLink = elemento.get('data-mediapolis')
        if (args.verbose):
            print(f"Download #{i+1}, @: {currentLink}")
        audioFile = requests.get(currentLink)
        open(f'{i+1}.mp3', 'wb').write(audioFile.content)
    print("Download Completato")
