# wikilinks

wikilinks is a Python module that provides a signle function for extracting
external links from Wikipedia that point at a particular website. This can be
useful to discover how Wikipedian's have used the content on a website. It was
originally part of a much larger project called [linkypedia] that was used to
visualize the use of cultural heritage materials on Wikipedia.

While [Wikipedia's API] allows you list external links from a given page, it
doesn't (to my knowledge) have an API call to retrieve pages that link to a
particular website. However they do provide the [External links search] page
that lets you perform this lookup in your browser. wikilinks simply scrapes
those results, for all language wikipedias.

## Install

    pip install wikilinks

## Use

This example will go and get all the links from wikipedia to the mith.umd.edu
website as a tuple of `(source, target)`:

```python
from wikilinks import wikilinks

for link in wikilinks("http://www.loc.gov"):
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

If you know you are only interested in let's say the German and French
Wikipedias you can limit the search:

    ```
    for link in wikilinks("http://mith.umd.edu", langs=["de", "fr"]):
        print(link)
    ```

[Wikipedia's API]: https://en.wikipedia.org/w/api.php
[External links search]: https://en.wikipedia.org/wiki/Special:LinkSearch
[Linkypedia]: https://github.com/edsu/linkypedia
