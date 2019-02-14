# SamlaLibris
Access LIBRIS and search for Svenska Kyrkor and extract items available from RAÄ Samla

 1) Search in LIBRIS is [ZSER:(Sveriges kyrkor)](http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200)

 1-1) Check if RAÄ SAMLA has references to Wikipedia/Wikidata

 1-2) export data

 2) **Next step** use [Open Refine](https://www.wikidata.org/wiki/Wikidata:Tools/OpenRefine) to Match items in Wikidata to find Objects for authors etc.. and upload to Wikidata

 2-1) Upload to Wikidata --> SAMLA books will be one object with references from the WD church object

# Usage
Python [get_libris_svenska_kyrkor.py](https://github.com/salgo60/SamlaLibris/blob/master/get_libris_svenska_kyrkor.py) --> [log](https://github.com/salgo60/SamlaLibris/blob/master/log/get_libris_svenska_kyrkor2019-02-13.log)
* Output
 * [svenskakyrkor.csv](https://github.com/salgo60/SamlaLibris/blob/master/svenskakyrkor.csv)
   * contains LIBRIS information looks like the JSON doesnt contain page information see [unanswered question](https://kundo.se/org/librisxl/d/soka-fram-alla-kopplade-till-samlaraa-i-libris-xl/#c3195511)
 * [samlaWikidata.csv](https://github.com/salgo60/SamlaLibris/blob/master/samlaWikidata.csv)

# Wikidata (test)
* Wikidata objekt [Q61723424](https://www.wikidata.org/wiki/Q61723424) is RAÄ Samla [6880](http://samla.raa.se/xmlui/handle/raa/6880) - see also [What links here](https://www.wikidata.org/wiki/Special:WhatLinksHere/Q61723424)

# Links

* Question LIBRIS XL about searching [link](https://kundo.se/org/librisxl/d/soka-fram-alla-kopplade-till-samlaraa-i-libris-xl/)
 * LIBRIS XL product owner [Anna Berggren](https://www.youtube.com/watch?v=N26nglSxhDk) reply 20190214
    * JSON API is just available for LIBRIS and **not** LIBRIS XL
    * Riksantikvarieämbetet is a text string **rdfs:Literal** and not the correct linked data way **owl:sameAs** for more info about [ProvisionActivity](http://id.loc.gov/ontologies/bibframe.html#p_provisionActivityStatement) see [LIBRIS Data Model](https://libris.kb.se/wk2q9mn3z0g096kd)
    * its confirmed that pattern matching in URLS and labels is what we have today(2019-feb) and use old school LIBRIS API
      * Feels an odd approach to have such bad data when LIBRIS have invested in Linked Data building LIBRIS XL since [2012](https://librisbloggen.kb.se/2014/05/28/ny-katalog-nytt-format-pionjararbetet-med-libris-xl/)/[roadmap 2014](https://librisbloggen.kb.se/2014/06/08/uppdaterad-libris-roadmap-juni/). LIBRIS statement about [Open Data](http://kb.se/libris/Om-Libris/Introduktion-till-nya-Libris-och-XL/Lankade-data-och-arbetet-framat/)
* [UGC-hubben](https://www.raa.se/hitta-information/k-samsok/anvandargenererat-innehall-ugc-hubben/) (användargenererat innehåll)
* [Sveriges kyrkor](http://samla.raa.se/xmlui/handle/raa/7) - [Riksantikvarieämbetes Samla](https://www.raa.se/hitta-information/publikationer/om-samla/)
* [LIBRIS Xsearch](http://librishelp.libris.kb.se/help/xsearch_swe.jsp?open=tech)
* Wikidata Phabricator Task [T215603](https://phabricator.wikimedia.org/T215603) *Connect WD Churches and church documentation at [RAÄ](http://samla.raa.se/xmlui/handle/raa/7)*
