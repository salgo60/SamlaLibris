from dataclasses import dataclass
import urllib.request, json
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

@dataclass
class LibrisItem:
    librisID: str
    title: str
    yearPublished: str = ""
    ISBN: str = ""
    publisher: str = ""
    creator: str = ""
    samlaID: str = ""
    relation: str = ""
#     page: str = ""


searchURLs = {'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200',
              'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200&start=201',
              'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200&start=401',
              'http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200&start=601'}

# Python has bad support for overload --> a dirty solution below

def get_isbn(item):
    return item.get('isbn','')

def get_creator(item):
    return item.get('creator','')

def get_publisher(item):
    return item.get('publisher', '')

def get_year_published(item):
    return item.get('date', '')

def get_relation(item):
    return item.get('relation', '')

def in_samla(item):
    """check url for pattern, LIBRIS miss something published by and mediatype?!?!?"""
    for libris_url in item["free"]:
        if str(libris_url).lower().find("raa/samla"):
            return True
    return False


def samla_id(item):
    """extract RAÄ samla id from URL"""
    for libris_url in item["free"]:
        try:
            samlaurl = urlparse(libris_url)
            if "raa/samla/html" in samlaurl.path:
                return (samlaurl.path).lower().replace('/raa/samla/html/', '')
        except:
            logger.warning("libris_url : %s", item)
    return


def get_libris_identifier(item):
    return item["identifier"].replace("http://libris.kb.se/bib/", "")


def clean_libris_title(item):
    ''' returns the LIBRIS title
            - strip media type [Elektronisk resurs]
            :rtype: str'''

    cleanTitle = str(item["title"]).replace(" [Elektronisk resurs]", "")
    return cleanTitle

def get_libris_page(item):
    ''' returns the LIBRIS page info in... feels its not in JSOn see question
        https://kundo.se/org/librisxl/d/soka-fram-alla-kopplade-till-samlaraa-i-libris-xl/#c3195511
             :rtype: str'''
    clean_page = ""
    logger.info("Not implemented - ")
    return clean_page


def get_LIBRIS_svenska_kyrka(libris_svenska_kyrkan):
    ''' loops LIBRIS search URLs to get data related to RAÄ Samla
    '''

    for search in searchURLs:
        logger.info("Search: %s", search)
        with urllib.request.urlopen(search) as url:
            data = json.loads(url.read().decode())
            for item in data["xsearch"]["list"]:
                try:
                    if 'free' not in item:
                        raise ValueError("No Free resource")
                    # print  (str(item["free"][0]))
                    if in_samla(item):
                        libris_svenska_kyrkan.append(
                            LibrisItem(librisID = get_libris_identifier(item),
                                       title = clean_libris_title(item),
                                       yearPublished = get_year_published(item),
                                       ISBN = get_isbn(item),
                                       publisher = get_publisher(item),
                                       creator = get_creator(item),
                                       samlaID = samla_id(item),
                                       relation =get_relation(item)
                        ))

                except ValueError:
                    logger.info("No 'Free' in LIBRIS item : %s", item)
                    pass
                finally:
                    pass

    return libris_svenska_kyrkan


