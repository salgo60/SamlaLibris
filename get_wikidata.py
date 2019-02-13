import logging
from urllib.parse import urlparse
import pywikibot as pywikibot

logger = logging.getLogger(__name__)


def get_WD(wikipedia_url):
    """ get WD object from swedish wikipedia URL

    user account/pwd is defined i  user-config.py like below user xxxx pwd yyy
        usernames['xxxx']['yyy'] = u'ExampleBot'
    """
    try:
        wikipedia_page_url = urlparse(wikipedia_url)
        wikipedia_page = wikipedia_page_url.path.split("/")[2]

        site = pywikibot.Site('sv', 'wikipedia')
        page = pywikibot.Page(site, wikipedia_page)
        wikidata = pywikibot.ItemPage.fromPage(page)

        logger.info("\t\twikidata %s wikipedia %s", wikidata.id, wikipedia_url)
        return wikidata.id
    except:
        logger.exception("Exception wikipedia %s", wikipedia_url)
        pass
    finally:
        pass
    return
