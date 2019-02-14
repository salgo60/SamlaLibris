# SamlaLibris
Access LIBRIS and search for Svenska Kyrkor and extract items available from RAÄ Samla

 1) Search in LIBRIS is [ZSER:(Sveriges kyrkor)](http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200)

 1-1) Check if RAÄ SAMLA has references to Wikipedia/Wikidata

 1-2) export data

 2) Next step use OpenRefine to Match items in Wikidata

 2-1) Upload to Wikidata --> SAMLA books one object references fro WD chucrobject using

### How to 
* Python [get_libris_svenska_kyrkor.py](https://github.com/salgo60/SamlaLibris/blob/master/get_libris_svenska_kyrkor.py) --> [log](https://github.com/salgo60/SamlaLibris/blob/master/log/get_libris_svenska_kyrkor2019-02-13.log)
* produce [svenskakyrkor.csv](https://github.com/salgo60/SamlaLibris/blob/master/svenskakyrkor.csv) and [samlaWikidata.csv](https://github.com/salgo60/SamlaLibris/blob/master/samlaWikidata.csv)

### Wikidata (test)
* Wikidata objekt [Q61723424](https://www.wikidata.org/wiki/Q61723424) is RAÄ Samla [6880](http://samla.raa.se/xmlui/handle/raa/6880) - [What links here](https://www.wikidata.org/wiki/Special:WhatLinksHere/Q61723424)

### Links

* Question LIBRIS XL about searching [link](https://kundo.se/org/librisxl/d/soka-fram-alla-kopplade-till-samlaraa-i-libris-xl/) - no reply so far but looks like the data in LIBRIS has bad structure with no Identifiers for RAÄ --> its pattern matching in URLS and labels. Feels an odd approach to have such bad data when LIBRIS have invested in Linked Data building LIBRIS XL since [2012](https://librisbloggen.kb.se/2014/05/28/ny-katalog-nytt-format-pionjararbetet-med-libris-xl/)/[roadmap 2014](https://librisbloggen.kb.se/2014/06/08/uppdaterad-libris-roadmap-juni/). LIBRIS statement about [Open Data](http://kb.se/libris/Om-Libris/Introduktion-till-nya-Libris-och-XL/Lankade-data-och-arbetet-framat/)
* [UGC-hubben](https://www.raa.se/hitta-information/k-samsok/anvandargenererat-innehall-ugc-hubben/) (användargenererat innehåll)
* [Sveriges kyrkor](http://samla.raa.se/xmlui/handle/raa/7) - [Riksantikvarieämbetes Samla](https://www.raa.se/hitta-information/publikationer/om-samla/)
* [LIBRIS Xsearch](http://librishelp.libris.kb.se/help/xsearch_swe.jsp?open=tech)
* Phabricator Task [T215603](https://phabricator.wikimedia.org/T215603) *Connect WD Churches and church documentation at [RAÄ](http://samla.raa.se/xmlui/handle/raa/7)*
