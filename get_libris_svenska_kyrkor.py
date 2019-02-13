"""Function to get LIBRIS records for Svenska Kyrkor with SAMLA ref

    1) Search in LIBRIS is ZSER:(Sveriges kyrkor)
    2) Check if SAMLA
    3) export data
    4) Use OpenRefine to Match items in WIkidata and upload

"""
import datetime
import csv
from typing import List
import logging
from get_libris import LibrisItem
import get_libris
import get_UGC

__version__ = "1.0.0"


def main():
    libris_svenska_kyrkan: List[LibrisItem] = []  # Contains LIBRIS items
    nrWikipediaRef = 0  # Number references to Wikipeda

    # Create logger
    today = str(datetime.date.today())
    LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
    logging.basicConfig(filename="log/get_libris_svenska_kyrkor" + today + ".log",
                    level=logging.INFO,
                    format=LOG_FORMAT)

    logger = logging.getLogger()

    # Add terminal logging
    logging.getLogger().addHandler(logging.StreamHandler())
    logger.info("Version %s",__version__)

    logger.info("Start query LIBRIS")
    get_libris.get_LIBRIS_svenska_kyrka(libris_svenska_kyrkan)

    csv_filename = "svenskakyrkor.csv"
    with open(csv_filename, 'w', encoding='UTF-8') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, )
        i = 0
        for i in range(len(libris_svenska_kyrkan)):
            wr.writerow([libris_svenska_kyrkan[i].librisID,
                        libris_svenska_kyrkan[i].title,
                        libris_svenska_kyrkan[i].yearPublished,
                        libris_svenska_kyrkan[i].ISBN,
                        libris_svenska_kyrkan[i].publisher,
                        libris_svenska_kyrkan[i].creator,
                        libris_svenska_kyrkan[i].samlaID,
                        libris_svenska_kyrkan[i].relation
                         ])


        logger.info("CSV file %s created with LIBRIS/Samla = %s", csv_filename, i + 1)

        get_UGC.check_UGC(libris_svenska_kyrkan)

        get_UGC.getRelationTypes()  # to get a better understanding of the Data in UGC


if __name__== "__main__":
  main()