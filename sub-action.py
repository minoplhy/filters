import os
import sys

sys.path.append('/mass-name-change')
import build_make
os.makedirs('/gh-releases',exist_ok=True)

build_make.filepath_mass_changer('Allowlist' ,'/reprwiki/Private-build/Allowlist' ,'/gh-releases')
build_make.filepath_mass_changer('Veneto' ,'/reprwiki/Private-build/veneto' ,'/gh-releases')
build_make.filepath_mass_changer('ucate' ,'/reprwiki/Private-build/ucate' ,'/gh-releases')
