# russian_romanisation
*Script to transliterate text in Russian to Latin*

I wrote this because I wanted to read an old Russian encyclopedia that I found at home but since I don't know how to read Cyrillic characters this was pretty tough going. I hate having to rote memorise scripts so being able to compare the original text and its transliteration side by side seemed like a good approach. It turns out that there are in fact a bunch of ways of doing that so I wrote this script.

`russian_romanisation.csv` is adapted from the transliteration table in the Wikpedia article for "[Romanization of Russian](https://en.wikipedia.org/wiki/Romanization_of_Russian#Transliteration_table)". The code currently only swaps the Russian characters for the transliterated strings - it does not implement any of the rules specified in the Table Notes. I should probably go back and implement those at some point.

## Usage

```
➜  russian_romanisation git:(master) ✗ python transliterate.py -h
usage: transliterate.py [-h]
                        {gost_2002,bs_1958,gost_1971,scholarly_1,iso_1995,passport_2010,ala_lc,passport_2013,bgn_pcgn,iso_1968,gost_1971_2,passport_1997,scholarly_2,road_signs}
                        [inputfile]

Transliterate Russian using various romanisations

positional arguments:
  {gost_2002,bs_1958,gost_1971,scholarly_1,iso_1995,passport_2010,ala_lc,passport_2013,bgn_pcgn,iso_1968,gost_1971_2,passport_1997,scholarly_2,road_signs}
                        The romanisation to use.
  inputfile             The text to be translated. May be a file or piped
                        stdin.

optional arguments:
  -h, --help            show this help message and exit
```
