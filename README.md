# AnimeMangaDownloader

Download manga as batches from mangareader.net.

## MangaDownloader
### Usage:

1. Find the url of the manga you want to download from http://mangareader.net. You can use their normal Search or Advanced Search option
2. Download or clone the repository
3. Open terminal at the repository folder
4. Enter the following command: python MangaDownloader.py --site [url] --start [(Chapter to start downloading in integer)-1] --stop [Chapter to stop downloading in integer] --folder [Path To Destination Folder]
5. All parameters in above command except --site are optional
6. The manga chapters will be downloaded as .cbz files to destination folder. You can view these files using YACReader or any CBZ Viewer.
     

### Libraries Used:
1. urllib.parse
2. urllib.request
3. os
4. BeautifulSoup
5. argparse
6. sys
7. shutil
8. zipfile
          
All of the above libraries are mostly present already when Python 3.6 installed. Compatible with Python 3.6. Not checked with other versions.

## AnimeDownloader
### Usage:

1. Find the url of the first episode of the anime you want to download from https://www4.9anime.is/.
2. Download or clone the repository
3. Open terminal at the repository folder
4. Enter the following command: python MangaDownloader.py --name [Name of Anime] --site [url] --start [(Chapter to start downloading in integer)-1] --stop [Chapter to stop downloading in integer] --folder [Path To Destination Folder]
5. All parameters in above command except --name and --site are optional
6. The anime episodes will be downloaded to destination folder.
     

### Libraries Used:
1. selenium
2. urllib.request
3. os
4. BeautifulSoup
5. argparse
6. requests
7. time
8. zipfile
9. clint
          
All of the above libraries are mostly present already when Python 3.6 installed. Others can be downloaded with pip install. chromedriver have to be downloaded and set for selenium to work.
 ##### In Mac
 ```bash
 brew tap caskroom/cask
 brew cask install chromedriver
 ```
 
 ##### In Ubuntu
 ```bash
 wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
 unzip chromedriver_linux64.zip
 sudo mv chromedriver /usr/bin/chromedriver
 sudo chown root:root /usr/bin/chromedriver
 sudo chmod +x /usr/bin/chromedriver
 ```
 
 ##### In Windows
 1. Download from https://chromedriver.storage.googleapis.com/2.30/chromedriver_win32.zip
 2. Extract it.
 3. Copy chromedriver.exe to C:\Windows\
 
Compatible with Python 3.6. Not checked with other versions.
