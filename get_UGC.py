import urllib.request, json
import logging
import csv
from dataclasses import dataclass

from get_wikidata import get_WD
from typing import List
logger = logging.getLogger(__name__)

relTypes = []  # Understand what refs are in the data


@dataclass
class SamlaWikidata:
        samlaID: str = ""
        WikiData: str = ""

samla_wikidata_list: List[SamlaWikidata] = []
counter_no_svWikipedia = 0  # added counter for bug UGC-46

def check_wd_reference(samla_id):
    global counter_no_svWikipedia
    ugc_kulturarvsdataid = 'http://ugc.kulturarvsdata.se/UGC-hub/api?' \
                           'x-api=ex2147ap36&method=retrieve&scope=all&maxCount=0&format=json' \
                           '&objectUri=http://kulturarvsdata.se/raa/samla/' \
                           + samla_id
    logging.info("Samla: %s", "http://kulturarvsdata.se/raa/samla/html/" + samla_id)
    logging.info("\tUGC: %s", ugc_kulturarvsdataid)

    with urllib.request.urlopen(ugc_kulturarvsdataid) as url:
        data = json.loads(url.read().decode())
        if 'relations' in data["response"]:
            for item in data["response"]["relations"]:
                relatedUri = item.get("relatedUri", "")
                try:
                    if "sv.wikipedia" in relatedUri:
                        samla_wikidata_list.append(SamlaWikidata(
                                                        samlaID=samla_id,
                                                        WikiData=get_WD(relatedUri)))
                    else:
                        logger.info("\t\trelatedUri not sv.Wikipedia: %s", relatedUri)
                        counter_no_svWikipedia += 1  # is a bug reported when related Uri is referencing itself
                except:
                    logging.exception("Problem %s", relatedUri)
                finally:
                    pass
                try:
                    """ To get some understanding of supported relation types. Feels documetation is missing """
                    if item["relationType"] not in relTypes:
                        relTypes.append(item["relationType"])
                finally:
                    pass
        else:
            logging.info("samlaID %s miss relation", samla_id)

    return


def check_UGC(libris_svenska_kyrkan):
    for i in range(len(libris_svenska_kyrkan)):
        check_wd_reference(libris_svenska_kyrkan[i].samlaID)

    csv_filename = "samlaWikidata.csv"
    with open(csv_filename, 'w', encoding='UTF-8') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, )
        i = 0
        for i in range(len(samla_wikidata_list)):
            wr.writerow([samla_wikidata_list[i].samlaID,
                         samla_wikidata_list[i].WikiData,
                         ])

        logger.info("CSV file %s created with Wikidata/Samla = %s", csv_filename, i + 1)

    logger.info("Number non svWikipedia references UGC-46 = %s", counter_no_svWikipedia)

    return


def getRelationTypes():
    logging.info("Relation types found in UGC:")
    for i in range(len(relTypes)):
        logging.info("\t\t%s", relTypes[i])
    return
