from torrt import toolbox
#import bs4

username=''
password=''

url='https://rutracker.org/forum/dl.php?t=6014364'
download_to='C:/files'
#print(get_download_link(url))

dw = toolbox.add_torrent_from_url(url, download_to)
print(dw)