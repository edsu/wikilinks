# wikilinks

wikilinks is a simple Python module for extracting links from Wikipedia to a
particular website. While [Wikipedia's API] allows you list external links from
a given page, it doesn't have an API call to retrieve pages that link to a
particular website URL. They do however provide the [External links search] page
that lets you perform this lookup. wikilinks simply scrapes those results, for
all language wikipedias.

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

Which would result in the following 

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

[External links search]: https://en.wikipedia.org/wiki/Special:LinkSearch
