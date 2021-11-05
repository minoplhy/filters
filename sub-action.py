import os
import sys

sys.path.append('/filters-maker')
import build_make
os.makedirs('/gh-releases',exist_ok=True)

build_make.filepath_mass_changer('Allowlist' ,'/reprwiki/Private-build/Allowlist' ,'/gh-releases','txt')
build_make.filepath_mass_changer('Veneto' ,'/reprwiki/Private-build/veneto' ,'/gh-releases','txt')
build_make.filepath_mass_changer('ucate' ,'/reprwiki/Private-build/ucate' ,'/gh-releases','txt')

build_make.filepath_mass_changer('Allowlist' ,'/reprwiki/Private-build/Allowlist' ,'/gh-releases','conf')
build_make.filepath_mass_changer('Veneto' ,'/reprwiki/Private-build/veneto' ,'/gh-releases','conf')
build_make.filepath_mass_changer('ucate' ,'/reprwiki/Private-build/ucate' ,'/gh-releases','conf')
