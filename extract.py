print('''

  ____  __  ___   _              _    ___      _    ____  __  __    _    ____  
 |  _ \ \ \/ / \ | |            / \  / _ \    / \  |  _ \|  \/  |  / \  |  _ \ 
 | |_) | \  /|  \| |  _____    / _ \| | | |  / _ \ | |_) | |\/| | / _ \ | |_) |
 |  _ <  /  \| |\  | |_____|  / ___ \ |_| | / ___ \|  _ <| |  | |/ ___ \|  __/ 
 |_| \_\/_/\_\_| \_|         /_/   \_\__\_\/_/   \_\_| \_\_|  |_/_/   \_\_|    
                                                                               
                                                                               
  ===========================================================================
  ==>> EXTRACT AD LINKS FROM AQAR MAP FOR FREE BY ABDULRAHMAN ABOULDAHAB <<==
  ===========================================================================

''')
from bs4 import BeautifulSoup
import urllib.request
#############################################################
k = input('Enter CITY [ ENGLISH ONLY ] : ')
url = 'https://aqarmap.com.eg/ar/for-sale/land-or-commercial/'+k+'/'
openurl     = urllib.request.urlopen(url)
readliness  = str(openurl.read(5000000))
soup        = BeautifulSoup(readliness,'html.parser')
for i in soup.findAll('div',{'class':'card-details-container'}):
    a = 'https://aqarmap.com.eg' + i.a.get('href')
    with open('RES.txt',mode='a+') as f:
        f.write(a+'\n')

print('='*20);print(' FINISHED ');print('='*20)
end = input(' >>> Press Enter To Close Script <<< ')
