from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request as request
import requests
from bs4 import BeautifulSoup
import time
from clint.textui import progress
import argparse
import os

browserHeader = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

folder = ""

def downloadVideo( EpisodeName, EpisodeURL):
	print("Opening " + EpisodeURL)
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1920x1080")

	driver = webdriver.Chrome(chrome_options=chrome_options)
	# driver = webdriver.Chrome()
	driver.get(EpisodeURL)
	print(EpisodeURL + " successfully opened!!!")
	cover = driver.find_elements_by_class_name("cover")
	cover[0].click()
	driver.switch_to_window(driver.window_handles[1])
	driver.close()
	driver.switch_to_window(driver.window_handles[0])
	time.sleep(5)
	iframe = driver.find_element_by_css_selector("iframe")
	RapidVideoURL = iframe.get_attribute("src")+"&q=1080p"
	print(RapidVideoURL)
	driver.close()

	req = request.Request(RapidVideoURL,headers=browserHeader)
	response = request.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	video = soup.findAll('source')
	VideoURL = video[0]['src']

	r = requests.get(VideoURL, stream=True)
	path =  EpisodeName + '.mp4'
	f = open(path, 'wb')
	total_length = int(r.headers.get('content-length'))
	print("Downloading "+EpisodeName.split('/')[-1]+"...")
	for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
	    if chunk:
	        f.write(chunk)
	        f.flush()
	print("Download successful!!\n")

def getLinks(args):
	# Starting html path of the manga
    site = args.site
    name = args.name
    # Starting html path of the manga
    start = args.start
    # Starting html path of the manga
    stop = args.stop
    # Folder to store the generated images
    folder = args.folder

    ## Make the folder if it is not already made
    if(not os.path.isdir(folder)):
        os.makedirs(folder)
   
    site_base = '/'.join(site.split('/')[:3])
    print("Getting Episode Listing...")

    req = request.Request(site, headers=browserHeader)
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    allRows = soup.select(".server.active")[0].find_all('a')
    episodeListing = []
    for row in allRows:
        episodeListing.append([folder + '/' + name + " " + row['data-base'],site_base+row['href']])
    
    #Make looping array
    downloadEpisodeListing = episodeListing[start:stop]
    if stop == -1:
        downloadEpisodeListing = episodeListing[start:]
    return (downloadEpisodeListing)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=True, type=str,
                        help='Name of Anime')
    parser.add_argument('--site', required=True, type=str,
                        help='URL of the first episode in series')
    parser.add_argument('--start', type=int, default=0,
                        help='Episode to start downloading from')
    parser.add_argument('--stop', type=int, default=-1,
                        help='Episode to stop downloading')
    parser.add_argument('--folder', type=str, default='Anime',
                        help='Output folder')
    args = parser.parse_args()

    allEpisodes = getLinks(args)
    print("Episode Listing Received\n")
    for episodeName, episodeLink in allEpisodes:
    	downloadVideo(episodeName, episodeLink)

if __name__ == '__main__':
    main()


