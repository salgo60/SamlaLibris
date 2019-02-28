# SamlaLibris
* Wikidata Phabricator Task [T215603](https://phabricator.wikimedia.org/T215603) *Connect WD Churches and church documentation at [RAÄ](http://samla.raa.se/xmlui/handle/raa/7)*
* [Video](https://www.youtube.com/watch?v=6szCrwKdji0) in Swedish describes this linked solution where I extract 200 books from LIBRIS and combines them with RAÄ and Wikidata. A small reaction on this tweet from LIBRIS XL that I feel has no Linked Data vision displayed in what is delivered <-> [LIBRISXL tweet](https://twitter.com/LibrisNytt/status/1096353627097255936) "UX-design – att forma en användarupplevelse"
* [Map with the churches](https://goo.gl/Ftkd3F) that are documented in a RAÄ Book ([also links LIBRIS/LIBRIS XL](http://tinyurl.com/y4puqyxb))

![Wikidata search](https://github.com/salgo60/SamlaLibris/blob/master/www/SamlaLIBRIS_small.png)


# POC Linked Books - what can be done in a day
<img src="http://yuml.me/diagram/scruffy/class/[LIBRIS Svenska kyrkor]++book-1..&gt;[RAÄ Samla]++book-1..&gt;[RAÄ Samla]"/>
<img src="http://yuml.me/diagram/scruffy/class/[UGC]-..&gt;book[RAÄ Samla]"/>
<img src="http://yuml.me/diagram/scruffy/class/[UGC]-..&gt;Churches[Wikidata]"/>

Access LIBRIS and search for Svenska Kyrkor and extract items available from RAÄ Samla

 1) Search in LIBRIS is [ZSER:(Sveriges kyrkor)](http://libris.kb.se/xsearch?query=ZSER:(Sveriges%20kyrkor)&format=json&n=200)

 1-1) Check if RAÄ SAMLA has references to Wikipedia/Wikidata using [UGC](https://www.raa.se/hitta-information/k-samsok/anvandargenererat-innehall-ugc-hubben/)

 1-2) export data

 2) **Next step** use [Open Refine](https://www.wikidata.org/wiki/Wikidata:Tools/OpenRefine) to Match items in Wikidata to find Objects for authors etc.. and upload to Wikidata

 2-1) Upload to Wikidata --> SAMLA books will be one object with references from the WD church object and same as with the authors of the books

# Usage
Python [get_libris_svenska_kyrkor.py](https://github.com/salgo60/SamlaLibris/blob/master/get_libris_svenska_kyrkor.py) --> [log](https://github.com/salgo60/SamlaLibris/tree/master/log)
* Output
 * [svenskakyrkor.csv](https://github.com/salgo60/SamlaLibris/blob/master/svenskakyrkor.csv)
   * contains LIBRIS information looks like the JSON doesnt contain page information see [unanswered question](https://kundo.se/org/librisxl/d/soka-fram-alla-kopplade-till-samlaraa-i-libris-xl/#c3195511)
 * [samlaWikidata.csv](https://github.com/salgo60/SamlaLibris/blob/master/samlaWikidata.csv)
   * contains UGC relations Samla <-> Wikidata

# Wikidata
* every book is an object in WD 
  * example Wikidata objekt [Q61723424](https://www.wikidata.org/wiki/Q61723424) is RAÄ Samla [6880](http://samla.raa.se/xmlui/handle/raa/6880) - see also [What links here](https://www.wikidata.org/wiki/Special:WhatLinksHere/Q61723424)
  * every book has one or more Main Topic [P921](https://www.wikidata.org/wiki/Property_talk:P921) that is the churches they describe
* every church gets a described by [P1343](https://www.wikidata.org/wiki/Property_talk:P1343) linking back to the book
## Wikidata queries
* [Map with churches described by RAÄ](https://goo.gl/UYCMXB)
* Linked data Graph of book [Riddarholmskyrkan](http://tinyurl.com/yyeoszcw) same as 
  * RAÄ Samla [kulturarvsdata.se/raa/samla/6873](http://kulturarvsdata.se/raa/samla/html/6873)
  * LIBRIS [19512784](http://libris.kb.se/bib/19512784)
* [Map - chuches near me documented by RAÄ](https://goo.gl/S62aAy)
* [Start with a book about the Riddarholm church](http://tinyurl.com/y334xnvy) [tweet](https://twitter.com/salgo60/status/1101089732564566018)

![Book about the Riddarholm church](https://github.com/salgo60/SamlaLibris/blob/master/www/Book.png)

## Errors
* Wikidata/Sälgö
  * Wikidata 
    * Task Wikidata Phabricator Task [T215603](https://phabricator.wikimedia.org/T215603) and [workboard](https://phabricator.wikimedia.org/tag/wmse-riksarkivet-tora/)
    * [Category:P1260_Error](https://www.wikidata.org/wiki/Category:P1260_Error)
  * Github
    * [salgo60/SamlaLibris/issues](https://github.com/salgo60/SamlaLibris/issues)
    * [Projectboard RAÄ/Samla](https://github.com/salgo60/SamlaLibris/projects/1)
* RAÄ/UGC
   * No formal error reporting is used at RAÄ UGC so I sent a tweet to Abbe that I have a WD category with odd things [Category:P1260_Error](https://www.wikidata.org/wiki/Category:P1260_Error) - I guess either I update WD or they do redirect feels like some [Link rot](https://en.wikipedia.org/wiki/Link_rot)
* LIBRIS XL 
  * has a [discussion group](https://kundo.se/org/librisxl/posts/) that is answered but lack a change process that you can follow
    * you get no error id
    * there is no public backlog
    * you get no notification when something is in production you have to ask every 6 months in the discussion group example [status federated search](https://kundo.se/org/librisxl/d/federated-sparql-fragor-hur-gor-man-och-vad-behovs/#c3199001)
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
## Facebook anouncements about the map
* [Släktforskning Semantisk Web](https://www.facebook.com/groups/345973895882090/permalink/552177558595055/)
* [Epitafier](https://www.facebook.com/groups/448439408603556/permalink/2096873797093434/)
* [Sveriges Släktforskarförbund](https://www.facebook.com/sverigesslaktforskarforbund/posts/1255156874623091?comment_id=1255734687898643)
