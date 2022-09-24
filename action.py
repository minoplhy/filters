import sys
sys.path.append('/filters-maker')

import os
import crawler
import maker
import duplicat

incoming = "/reprwiki/Private-build/ucate/domains.txt"
excluded = "/repros/Resources/excluded.txt"
rpz_locat = "/reprwiki/Private-build/ucate/rpz.txt"
hosts_locat = "/reprwiki/Private-build/ucate/hosts.txt"
abp_locat = "/reprwiki/Private-build/ucate/adblock.txt"
unb_locat = "/reprwiki/Private-build/ucate/unbound.conf"
dnq_locat = "/reprwiki/Private-build/ucate/dnsmasq.conf"
Version = "UCATE"
os.makedirs('/reprwiki/Private-build/ucate',exist_ok=True)

UCATE_SOURCE = [
'https://badmojr.github.io/1Hosts/Pro/rpz.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-dns_rpz.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/stevenblack-f_rpz.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/someonewhocares_rpz.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/hostsVN-all_rpz.txt',
'https://github.com/minoplhy/filters/raw/main/Resources/blocked.txt',
'https://block.energized.pro/basic/formats/filter',
'https://hblock.molinero.dev/hosts_unbound.conf',
'https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-Base_rpz.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-Mobile_rpz.txt',
'https://github.com/yous/YousList/raw/master/youslist.txt',
'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt',
'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt',
'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt',
'https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2022.txt'
]

crawler.clear_old_files(incoming)
crawler.download_group_filters(UCATE_SOURCE ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
crawler.IP_URL_FILTERING(incoming)
crawler.excluded(excluded, incoming)
crawler.blankremover(incoming)
crawler.sort(incoming)
duplicat.add_file(incoming, "/reprwiki/Private-build/ruleset.txt")
UCATEline = maker.linecounter(incoming)
maker.RPZBlocklist(excluded, incoming, rpz_locat ,Version)
maker.HOSTBlocklist(excluded, incoming, hosts_locat ,Version)
maker.ABPBlocklist(excluded, incoming, abp_locat ,Version)
maker.UNBOUNDBlocklist(excluded, incoming, unb_locat ,Version)
maker.DNSMASQBlocklist(excluded, incoming, dnq_locat ,Version)
maker.DOMAINBlocklist(excluded, incoming ,Version)

incoming = "/reprwiki/Private-build/veneto/domains.txt"
excluded = "/repros/Resources/excluded.txt"
rpz_locat = "/reprwiki/Private-build/veneto/rpz.txt"
hosts_locat = "/reprwiki/Private-build/veneto/hosts.txt"
abp_locat = "/reprwiki/Private-build/veneto/adblock.txt"
unb_locat = "/reprwiki/Private-build/veneto/unbound.conf"
dnq_locat = "/reprwiki/Private-build/veneto/dnsmasq.conf"
Version = "VENETO"
os.makedirs('/reprwiki/Private-build/veneto',exist_ok=True)

VENETO_SOURCE = [
'https://blokada.org/mirror/v5/exodusprivacy/standard/hosts.txt',
'https://github.com/crazy-max/WindowsSpyBlocker/raw/master/data/hosts/spy.txt',
'https://energized.pro/extensions/xtreme/formats/rpz.txt',
'https://curben.gitlab.io/malware-filter/phishing-filter-agh.txt',
'https://curben.gitlab.io/malware-filter/pup-filter-agh.txt',
'https://phishing.army/download/phishing_army_blocklist_extended.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-Tracking_rpz.txt',
'https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-blocklist.txt',
'https://github.com/DandelionSprout/adfilt/raw/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareDomains.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-cname-tracker_rpz.txt',
'https://github.com/minoplhy/filters/releases/download/filters-build/Adguard-cname-original_rpz.txt',
'https://urlhaus.abuse.ch/downloads/rpz/',
'https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt',
'https://github.com/mitchellkrogza/Phishing.Database/raw/master/phishing-domains-ACTIVE.txt'
]

crawler.clear_old_files(incoming)
crawler.download_group_filters(VENETO_SOURCE ,incoming)
crawler.filtering(incoming)
crawler.filteringcon(incoming)
crawler.killingdup(incoming)
crawler.IP_URL_FILTERING(incoming)
crawler.excluded(excluded, incoming)
crawler.blankremover(incoming)
crawler.sort(incoming)
duplicat.check_n_kill_dupes("/reprwiki/Private-build/ruleset.txt", incoming)
duplicat.add_file(incoming, "/reprwiki/Private-build/ruleset.txt")
VENETOline = maker.linecounter(incoming)
maker.RPZBlocklist(excluded, incoming, rpz_locat ,Version)
maker.HOSTBlocklist(excluded, incoming, hosts_locat ,Version)
maker.ABPBlocklist(excluded, incoming, abp_locat ,Version)
maker.UNBOUNDBlocklist(excluded, incoming, unb_locat ,Version)
maker.DNSMASQBlocklist(excluded, incoming, dnq_locat ,Version)
maker.DOMAINBlocklist(excluded, incoming ,Version)
                      
excluded = "/repros/Resources/excluded.txt"
os.makedirs('/reprwiki/Private-build/Allowlist',exist_ok=True)
Version = "Allowlist"
rpz_locat = "/reprwiki/Private-build/Allowlist/rpz.txt"
abp_locat = "/reprwiki/Private-build/Allowlist/adblock.txt"
domains_locat = "/reprwiki/Private-build/Allowlist/domains.txt"
ALLOWLISTline = maker.linecounter(excluded)
maker.RPZAllowlist(excluded, rpz_locat ,Version)
maker.ABPAllowlist(excluded, abp_locat ,Version)
maker.DOMAINAllowlist(excluded ,domains_locat ,Version)
                      
import version
het = "/repros/version.md"
addition = "\n# Rule Counter \n ### UCATE : " + str(UCATEline) +"\n\n ### Veneto : " + str(VENETOline) + "\n\n ### Allowlist : " + str(ALLOWLISTline)
version.build(het, addition)
