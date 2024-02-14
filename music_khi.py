import os
import os.path
import re
import xml.etree.ElementTree as et
from   urllib.request import urlopen as urlopen
import bs4

def descape(s:str):

    return re.sub(pattern='%([0-9]{2})',repl=lambda m: eval(f'\'\\x{m.group(1)}\''),string=s)

def urltail(url:str):

    return url.split('/')[-1]

def get_album(url:str,
              dir:str):
    
    doc            = bs4.BeautifulSoup(urlopen(url).read().decode(),features='html.parser')
    page_content   = doc         .find(id='rightColumn').find(id='pageContent')
    album_title    = page_content.find('h2').find(text=True,recursive=False)
    album_dir      = os.path.join(dir,album_title)
    os.makedirs(album_dir,exist_ok=True)
    for i,album_picture_link in enumerate(div.find('a')['href'] for div in page_content.find_all(attrs={'class':'albumImage'})):

        album_picture_name = os.path.join(album_dir, descape(urltail(album_picture_link)))
        if os.path.exists(album_picture_name): continue
        with open(album_picture_name, 'wb') as f:

            f.write(urlopen(album_picture_link).read())
    
    for song in page_content.find(id='songlist').find_all('tr'):

        if 'id' in song.attrs and song['id'] in {'songlist_header',
                                                 'songlist_footer',}: continue
        song_iter = lambda _iter=iter(song.find_all('td')): next(_iter)
        song_iter()
        cd_number    = song_iter().text
        track_number = song_iter().text
        track        = song_iter().find('a')
        track_name   = track.text
        track_link   = track['href']
        song_page    = bs4.BeautifulSoup(urlopen('https://downloads.khinsider.com'+track_link,features='html.parser').read().decode())
        song_content = song_page.find(id='rightColumn').find(id='pageContent')
        song_link    = song_content.find(attrs={'class':'songDownloadLink'}).parent['href']
        song_name    = os.path.join(album_dir,descape(urltail(song_link)))
        if os.path.exists(song_name): continue
        with open(song_name, 'wb') as f: 
            
            f.write(urlopen(song_link).read())

if __name__ == '__main__':

    import sys

    get_album(url=sys.argv[1],
              dir=sys.argv[2])