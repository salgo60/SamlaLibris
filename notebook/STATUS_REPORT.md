
# External Link Health Study – RAA

_Last updated: **2025-12-01**_

## Scope and method

This report measures HTTP availability of external links used in Wikipedia.
Findings reflect **technical accessibility**, not content validity.

---

## Summary

* **Total external links:** 300
* **Broken links:** 42 (14.0%)
* **Legacy DSpace links:** 3
* **Dominant failure mode:** removal of DSpace XMLUI endpoints

---

## Broken links by Wikipedia (Top 15)

| wiki   | links_total   | broken_links   | legacy_dspace   | broken_pct   |
|--------|---------------|----------------|-----------------|--------------|

---

## Broken links by content language (Top 15)

|                                   |   links |   broken |   broken_pct |
|:----------------------------------|--------:|---------:|-------------:|
| ('da', 'dansk')                   |      22 |       22 |       100    |
| ('nn', 'norsk nynorsk')           |      16 |       16 |       100    |
| ('sv', 'svenska')                 |      58 |        3 |         5.17 |
| ('cdo', '閩東語 / Mìng-dĕ̤ng-ngṳ̄') |       1 |        1 |       100    |
| ('af', 'Afrikaans')               |       7 |        0 |         0    |
| ('an', 'aragonés')                |       5 |        0 |         0    |
| ('ast', 'asturianu')              |       2 |        0 |         0    |
| ('de', 'Deutsch')                 |      25 |        0 |         0    |
| ('en', 'English')                 |      82 |        0 |         0    |
| ('es', 'español')                 |      32 |        0 |         0    |
| ('eu', 'euskara')                 |       1 |        0 |         0    |
| ('fi', 'suomi')                   |       6 |        0 |         0    |
| ('nl', 'Nederlands')              |       1 |        0 |         0    |
| ('no', 'norsk')                   |      40 |        0 |         0    |
| ('pl', 'polski')                  |       2 |        0 |         0    |

---

## Link rot over time (year heuristic)

|   year |   links |   broken |   legacy |   broken_pct |
|-------:|--------:|---------:|---------:|-------------:|
|   1936 |       2 |        0 |        0 |            0 |
|   1939 |       1 |        0 |        0 |            0 |
|   1956 |       1 |        0 |        0 |            0 |
|   1973 |       1 |        0 |        0 |            0 |
|   1974 |       1 |        0 |        0 |            0 |
|   1976 |       1 |        0 |        0 |            0 |
|   1978 |       2 |        0 |        0 |            0 |
|   1979 |       9 |        0 |        0 |            0 |
|   1981 |       1 |        1 |        1 |          100 |
|   2000 |       8 |        0 |        0 |            0 |
|   2003 |       1 |        1 |        0 |          100 |
|   2009 |       1 |        0 |        0 |            0 |
|   2014 |       1 |        0 |        0 |            0 |
|   2016 |       1 |        0 |        0 |            0 |
|   2018 |       1 |        1 |        0 |          100 |
|   2027 |       1 |        0 |        0 |            0 |
|   2069 |       1 |        0 |        0 |            0 |
|   2073 |       1 |        0 |        0 |            0 |
|   2074 |       1 |        0 |        0 |            0 |
|   2088 |       1 |        0 |        0 |            0 |

---

## Domains showing blocking or throttling

| domain   | checks   | ok   | timeouts   | conn_errors   | mean_latency   | problem_ratio   |
|----------|----------|------|------------|---------------|----------------|-----------------|

---

## Sample links needing manual repair

| Wikipedia-sida   | Extern länk                                                                 | repair_reason              | migration_hint                                                  |
|:-----------------|:----------------------------------------------------------------------------|:---------------------------|:----------------------------------------------------------------|
| Sune Lindqvist   | http://samla.raa.se/xmlui/bitstream/handle/raa/799/1926_307.pdf?sequence=1  | RAA DSpace XMLUI migration | https://samla.raa.se/discover?query=1926_307.pdf%3Fsequence%3D1 |
| Vendeltiden      | http://samla.raa.se/xmlui/bitstream/handle/raa/2429/1981_008.pdf?sequence=1 | RAA DSpace XMLUI migration | https://samla.raa.se/discover?query=1981_008.pdf%3Fsequence%3D1 |

Full list: `results/links_needing_manual_repair.csv`
