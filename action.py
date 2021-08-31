import sys
sys.path.append('/filters-maker')

import os
import crawler
import maker_rpz
import maker_hosts
import maker_abp
import maker_domains

incoming = "/reprwiki/Private-build/ucate/domains.txt"
excluded = "/repros/Resources/excluded.txt"
rpz_locat = "/reprwiki/Private-build/ucate/rpz.txt"
hosts_locat = "/reprwiki/Private-build/ucate/hosts.txt"
abp_locat = "/reprwiki/Private-build/ucate/adblock.txt"
Version = "UCATE"
os.makedirs('/reprwiki/Private-build/ucate',exist_ok=True)

crawler.clear_old_files(incoming)
crawler.download_filters("https://badmojr.github.io/1Hosts/Pro/rpz.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-cname-tracker_rpz.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-cname-original_rpz.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/releases/download/filters-build/stevenblack-f_rpz.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/releases/download/filters-build/someonewhocares_rpz.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/releases/download/filters-build/hostsVN-all_rpz.txt" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/releases/download/filters-build/hosts-database-full-alive_rpz.txt" ,incoming)
crawler.download_filters("https://urlhaus.abuse.ch/downloads/rpz/" ,incoming)
crawler.download_filters("https://github.com/minoplhy/filters/raw/main/Resources/blocked.txt" ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
crawler.excluded(excluded, incoming)
crawler.blankremover(incoming)
crawler.sort(incoming)
maker_rpz.RPZbuilding(excluded, incoming, rpz_locat ,Version)
maker_hosts.hostsbuilding(excluded, incoming, hosts_locat ,Version)
maker_abp.ABPbuilding(excluded, incoming, abp_locat ,Version)
maker_domains.domainsbuilding(excluded, incoming ,Version)

incoming = "/reprwiki/Private-build/veneto/domains.txt"
excluded = "/repros/Resources/excluded.txt"
rpz_locat = "/reprwiki/Private-build/veneto/rpz.txt"
hosts_locat = "/reprwiki/Private-build/veneto/hosts.txt"
abp_locat = "/reprwiki/Private-build/veneto/adblock.txt"
Version = "VENETO"
os.makedirs('/reprwiki/Private-build/veneto',exist_ok=True)

crawler.clear_old_files(incoming)
crawler.download_filters("https://blokada.org/mirror/v5/exodusprivacy/standard/hosts.txt" ,incoming)
crawler.download_filters("https://github.com/crazy-max/WindowsSpyBlocker/raw/master/data/hosts/spy.txt" ,incoming)
crawler.download_filters("https://energized.pro/extensions/xtreme/formats/rpz.txt" ,incoming)
crawler.download_filters("https://rpz.oisd.nl" ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
crawler.excluded(excluded, incoming)
crawler.blankremover(incoming)
crawler.sort(incoming)
maker_rpz.RPZbuilding(excluded, incoming, rpz_locat ,Version)
maker_hosts.hostsbuilding(excluded, incoming, hosts_locat ,Version)
maker_abp.ABPbuilding(excluded, incoming, abp_locat ,Version)
maker_domains.domainsbuilding(excluded, incoming ,Version)
                      
excluded = "/repros/Resources/excluded.txt"
os.makedirs('/reprwiki/Private-build/Allowlist',exist_ok=True)
Version = "Allowlist"
rpz_locat = "/reprwiki/Private-build/Allowlist/rpz.txt"
abp_locat = "/reprwiki/Private-build/Allowlist/adblock.txt"
domains_locat = "/reprwiki/Private-build/Allowlist/domains.txt"
maker_rpz.RPZallowlist(excluded, rpz_locat ,Version)
maker_abp.ABPallowlist(excluded, abp_locat ,Version)
maker_domains.DMallowlist(excluded ,domains_locat ,Version)
                      
import version
het = "/repros/version.md"
version.build(het)
