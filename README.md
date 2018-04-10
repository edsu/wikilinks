# wikilinks

`wikilinks` is a Python command line utility and module that allow you to easily
extract external links from Wikipedia that point at a particular website.  It
can be useful and interesting to see how Wikipedians have cited the content made
available on another website. These links say something about the websites
placement in Wikipedia, as well as the topics of interest in the website.

The `wikilinks` code was originally part of a much larger project called
[Linkypedia] that was used to visualize the use of cultural heritage materials
on Wikipedia.  Linkypedia has since been shut down but perhaps this little piece
of functionality could still be of use to you.

While [Wikipedia's API] allows you list external links from a given page, it
doesn't (to my knowledge) have an API call to retrieve pages that link to a
particular website. However they do provide the [External links search] page
that lets you perform this lookup in your browser. `wikilinks` simply scrapes
those results, for all language Wikipedias.

## Install

    pip install wikilinks

## Use

Find links in English Wikipedia that point at the mith.umd.edu website and print
them out as tab separated URLs:

    % wikilinks --lang en http://mith.umd.edu
    https://en.wikipedia.org/wiki/User:Mastersplinter/Making_the_History_of_1989 http://mith.umd.edu/
    https://en.wikipedia.org/wiki/University_of_Maryland_Libraries http://mith.umd.edu/ https://en.wikipedia.org/wiki/User:Walker222
    http://mith.umd.edu https://en.wikipedia.org/wiki/Maryland_Institute_for_Technology_in_the_Humanities
    http://mith.umd.edu/ https://en.wikipedia.org/wiki/User:Edsu http://mith.umd.edu
    https://en.wikipedia.org/wiki/University_of_Maryland_College_of_Information_Studies http://mith.umd.edu/ https://en.wikipedia.org/wiki/Antonia%27s_Line
    http://mith.umd.edu//WomensStudies/FilmReviews/antonias-line-mcalister https://en.wikipedia.org/wiki/Rio_Nutrias
    http://mith.umd.edu//eada/gateway/diario/diary.html https://en.wikipedia.org/wiki/Rio_Nutria_(Zuni_River_tributary)
    http://mith.umd.edu//eada/gateway/diario/diary.html https://en.wikipedia.org/wiki/Nutrioso,_Arizona
    http://mith.umd.edu//eada/gateway/diario/diary.html https://en.wikipedia.org/wiki/Marilee_Lindemann	http://mith.umd.edu/2008/01/
    https://en.wikipedia.org/wiki/User:Keilana/Women_scientist_resources http://mith.umd.edu/WomensStudies/Bibliographies/ScienceBiblio/science-pt2
    https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Maria_Ford http://mith.umd.edu/WomensStudies/FilmReviews/S/some-nudity-burdette.html
    https://en.wikipedia.org/wiki/Wikipedia:Articles_for_deletion/Log/2015_January_14 http://mith.umd.edu/WomensStudies/FilmReviews/S/some-nudity-burdette.html
    https://en.wikipedia.org/wiki/Talk:Colors_of_the_Wind http://mith.umd.edu/WomensStudies/FilmReviews/pocahontas-strong ...

## Use as a Library

This example will fetch each Wikipedia article link to the `mith.umd.edu`
website as a `(source, target)` tuple:

```python
from wikilinks import wikilinks

for link in wikilinks("http://mith.umd.edu"):
    print(link)
```

Which would output something like:

```
('https://ca.wikipedia.org/wiki/Amerigo_Vespucci', 'http://mith.umd.edu//eada/html/display.php?docs=vespucci_letters.xml')
('https://de.wikipedia.org/wiki/Lisa_Monaco', 'http://mith.umd.edu/WomensStudies/GenderIssues/Violence+Women/ResponsetoRape/introduction')
('https://de.wikipedia.org/wiki/Buenaventura_River', 'http://mith.umd.edu/eada/gateway/diario/')
('https://de.wikipedia.org/wiki/Sarah_Kemble_Knight', 'http://mith.umd.edu/eada/html/display.php?docs=knight_journal.xml')
('https://de.wikipedia.org/wiki/Klapperschlangen', 'http://mith.umd.edu/eada/html/display.php?docs=smith_map.xml')
('https://de.wikipedia.org/wiki/Theater_(Bauwerk)', 'http://mith.umd.edu/theatrefinder/')
('https://en.wikipedia.org/wiki/User:Mastersplinter/Making_the_History_of_1989', 'http://mith.umd.edu/')
...
```

By default `wikilinks` will search all language Wikipedias. If you are only
interested in links from particular language Wikipedias you can use the `langs`
parameter:

```python
for link in wikilinks("http://mith.umd.edu", langs=["de", "fr"]):
    print(link)
```

[Wikipedia's API]: https://en.wikipedia.org/w/api.php
[External links search]: https://en.wikipedia.org/wiki/Special:LinkSearch
[Linkypedia]: https://github.com/edsu/linkypedia
