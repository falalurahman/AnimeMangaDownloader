# Make sure all these libraries are installed before proceeding
import urllib.parse as parse
import urllib.request as request
import os
from bs4 import BeautifulSoup
import argparse
import sys
import shutil
import zipfile

browserHeader = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}



def download(args):
    # Starting html path of the manga
    site = args.site
    # Starting html path of the manga
    start = args.start
    # Starting html path of the manga
    stop = args.stop
    # Folder to store the generated images
    folder = args.folder
    tempFolder = 'TempManga'

    ## Make the folder if it is not already made
    if(not os.path.isdir(folder)):
        os.makedirs(folder)
    
    #Delete Temp FolderIf Exists
    if(os.path.isdir(tempFolder)):
    	shutil.rmtree(tempFolder)
    #Create Folder Fee_Receipts
    os.makedirs(tempFolder)
    site_base = '/'.join(site.split('/'))
    print("Getting Chapter Listing...")

    req = request.Request(site_base, headers=browserHeader)
    response = request.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    allRows = soup.find(id="listing").find_all('td')
    del allRows[1::2]
    chapterListing = []
    for row in allRows:
        chapterListing.append([row.get_text().strip().replace(":", "-"),'/'+'/'.join(row.find('a').get('href').split('/')[2:])])

    #Make looping array
    downloadChapterListing = chapterListing[start:stop]
    if stop == -1:
        downloadChapterListing = chapterListing[start:]
    
    for chapterName, chapterLink in downloadChapterListing:
        chapterBaseLink = site_base + chapterLink

        req = request.Request(chapterBaseLink, headers=browserHeader)
        response = request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        allOptions = soup.find(id="pageMenu").find_all('option')
        allPages = []
        for option in allOptions:
            allPages.append('/'+'/'.join(option['value'].split('/')[2:]))
        
        pageNumber = 1
        for page in allPages:
            pageLink = site_base + page

            req = request.Request(pageLink, headers=browserHeader)
            response = request.urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

            imageUrl = soup.find(id='img').get('src')

            req = request.Request(imageUrl, headers=browserHeader)
            imagePage = request.urlopen(req)
            content = imagePage.read()
            filename = tempFolder + '/' + str(pageNumber) + '.jpeg'
            fileOpen = open(filename,'wb')
            fileOpen.write(content)
            fileOpen.close()

            pageNumber += 1


        images = os.listdir(tempFolder)
        outputFile = folder + "/" + chapterName + ".cbz"
        cbzFile = zipfile.ZipFile(outputFile, 'w')
        for img in images:
                cbzFile.write(tempFolder + '/' + img)
        cbzFile.close()

        #Delete Temp FolderIf Exists
        if(os.path.isdir(tempFolder)):
            shutil.rmtree(tempFolder)
        #Create Folder Fee_Receipts
        os.makedirs(tempFolder)
        print("Created " + outputFile)


    #Delete Temp FolderIf Exists
    if(os.path.isdir(tempFolder)):
        shutil.rmtree(tempFolder)


# In[ ]:

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site', required=True, type=str,
                        help='URL of the first image in series')
    parser.add_argument('--start', type=int, default=0,
                        help='Chapter to start downloading from')
    parser.add_argument('--stop', type=int, default=-1,
                        help='Chapter to stop')
    parser.add_argument('--folder', type=str, default='Manga',
                        help='output folder')
    args = parser.parse_args()

    download(args)

# In[ ]:

if __name__ == '__main__':
    main()
