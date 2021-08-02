import sys
sys.path.append('/filters-maker')

import crawler
import maker_rpz
import maker_domains

incoming = '/repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/domains.txt'
excluded = '/repros/Resources/excluded.txt'
rpz_locat = '/repros/$INPUT_DESTINATION_FOLDER/$INPUT_DESTINATION_VERSION/rpz.txt'

crawler.download_filters("https://dbl.oisd.nl/" ,incoming)
crawler.download_filters("https://hosts.netlify.app/Pro/rpz.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/dns.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/cname-tracker.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/cname-original.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/stevenblack/f-s.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/someonewhocares/rpz.txt" ,incoming)
crawler.download_filters("https://urlhaus.abuse.ch/downloads/rpz/" ,incoming)
crawler.download_filters("https://github.com/easylist/easylist/raw/master/easylist/easylist_adservers.txt" ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
maker_rpz.RPZbuilding(excluded, incoming, rpz_locat)
maker_domains.domainsbuilding(excluded, incoming)
