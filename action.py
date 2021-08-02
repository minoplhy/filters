import sys
export PYTHONPATH=$PYTHONPATH:/filters-maker
  
import crawler
import maker_rpz
import maker_domains

input = '/repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/domains.txt'
excluded = '/repros/Resources/excluded.txt'
rpz_locat = '/repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/rpz.txt'

crawler.download_filters("https://dbl.oisd.nl/" ,input)
crawler.download_filters("https://hosts.netlify.app/Pro/rpz.txt" ,input)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/dns.txt" ,input)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/cname-tracker.txt" ,input)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/cname-original.txt" ,input)
crawler.download_filters("https://filters.kylz.nl/RPZ/stevenblack/f-s.txt" ,input)
crawler.download_filters("https://filters.kylz.nl/RPZ/someonewhocares/rpz.txt" ,input)
crawler.download_filters("https://urlhaus.abuse.ch/downloads/rpz/" ,input)
crawler.download_filters("https://github.com/easylist/easylist/raw/master/easylist/easylist_adservers.txt" ,input)
crawler.filtering(input)
crawler.filteringcon(input)
crawler.killingdup(input)
maker_rpz.RPZbuilding(excluded, input, rpz_locat)
maker_domains.domainsbuilding(excluded, input)
