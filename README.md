# MangaDownloader

Download manga as batches from mangareader.net.

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
