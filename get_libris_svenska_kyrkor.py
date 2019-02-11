"""Function to get LIBRIS records for Svenska Kyrkor with SAMLA ref

    1) Search in LIBRIS is ZSER:(Sveriges kyrkor)
    2) Check if SAMLA
    3) export data
    4) Use OpenRefine to Match items in WIkidata and upload

"""
import datetime
import urllib.request,json
import csv
from typing import List
import logging

from dataclasses import dataclass

@dataclass
class libris_item:
    librisID: str
    title: str
    samlaID: str = ""



searchURLs={'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200',
        'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200&start=201',
        'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200&start=401',
        'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200&start=601'}


def in_samla(item):
    for libris_url in item["free"]:
        if (str(libris_url).lower(),str(libris_url).find("raa")):
            return True
    return False

def samla_id(item):
    for libris_url in item["free"]:
       if (str(libris_url).lower(), str(libris_url).find("raa/samla/html")):
            return str(libris_url).replace('http://kulturarvsdata.se/raa/samla/html/','')
    return

libris_svenska_kyrkan: List[libris_item] = []

#Create logger
today = str(datetime.date.today())
LOG_FORMAT: str = " %(asctime)s - %(message)s"
logging.basicConfig(filename="log/get_libris_svenska_kyrkor" + today +".log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT)

logger = logging.getLogger()
logger.info("Start ")


def get_LIBRISidentifier(item):
    return item["identifier"].replace("http://libris.kb.se/bib/","")


def clean_title(item):
    cleanTitle = str(item["title"]).replace(" [Elektronisk resurs]","")
    return cleanTitle



for search in searchURLs:
    print ("Search ",search)
    logger.info("Search: %s", search)
    with urllib.request.urlopen(search) as url:
        data = json.loads(url.read().decode())
        for item in data["xsearch"]["list"]:
            try:
                if 'free' not in item:
                    raise ValueError("No Free resource")
                #print  (str(item["free"][0]))
                if in_samla(item):
                    libris_svenska_kyrkan.append(
                        libris_item(get_LIBRISidentifier(item),
                        clean_title(item),
                        samla_id(item)))

            except ValueError:
                logger.warning("ValueError: %s", item)
                pass
            finally:
                pass

with open("svenskakyrkor.csv", 'w',encoding='UTF-8') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,)
    i = 0
    for i in  range(len(libris_svenska_kyrkan)):
        wr.writerow([libris_svenska_kyrkan[i].librisID,
                     libris_svenska_kyrkan[i].samlaID,
                     libris_svenska_kyrkan[i].title])
    print ("LIBRIS item found with SAMLA = ",i+1)
    logger.info("LIBRIS item found with SAMLA = %s", i+1)