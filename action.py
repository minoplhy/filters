import sys
sys.path.append('/filters-maker')

import os
import crawler
import maker_rpz
import maker_domains
import maker_hosts
import maker_abp

incoming = "/reprwiki/Private-build/ucate/domains.txt"
excluded = "/repros/Resources/excluded.txt"
rpz_locat = "/reprwiki/Private-build/ucate/rpz.txt"
hosts_locat = "/reprwiki/Private-build/ucate/hosts.txt"
abp_locat = "/reprwiki/Private-build/ucate/adblock.txt"
os.makedirs('/reprwiki/Private-build/ucate',exist_ok=True)

crawler.clear_old_files(incoming)
crawler.download_filters("https://badmojr.github.io/1Hosts/Pro/rpz.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/cname-tracker.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/adguard/cname-original.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/stevenblack/f-s.txt" ,incoming)
crawler.download_filters("https://filters.kylz.nl/RPZ/someonewhocares/rpz.txt" ,incoming)
crawler.download_filters("https://urlhaus.abuse.ch/downloads/rpz/" ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
crawler.excluded(excluded, incoming)
crawler.blankremover(incoming)
crawler.sort(incoming)
maker_rpz.RPZbuilding(excluded, incoming, rpz_locat)
maker_hosts.hostsbuilding(excluded, incoming, hosts_locat)
maker_abp.ABPbuilding(excluded, incoming, abp_locat)
maker_domains.domainsbuilding(excluded, incoming)

incoming = "/reprwiki/Private-build/veneto/domains.txt"
excluded = "/repros/Resources/excluded.txt"
rpz_locat = "/reprwiki/Private-build/veneto/rpz.txt"
hosts_locat = "/reprwiki/Private-build/veneto/hosts.txt"
abp_locat = "/reprwiki/Private-build/veneto/adblock.txt"
os.makedirs('/reprwiki/Private-build/veneto',exist_ok=True)

crawler.clear_old_files(incoming)
crawler.download_filters("https://blokada.org/mirror/v5/exodusprivacy/standard/hosts.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/raw/main/Resources/blocked.txt" ,incoming)
crawler.download_filters("https://github.com/crazy-max/WindowsSpyBlocker/raw/master/data/hosts/spy.txt" ,incoming)
crawler.download_filters("https://energized.pro/extensions/xtreme/formats/rpz.txt" ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
crawler.excluded(excluded, incoming)
crawler.blankremover(incoming)
crawler.sort(incoming)
maker_rpz.RPZbuilding(excluded, incoming, rpz_locat)
maker_hosts.hostsbuilding(excluded, incoming, hosts_locat)
maker_abp.ABPbuilding(excluded, incoming, abp_locat)
maker_domains.domainsbuilding(excluded, incoming)
