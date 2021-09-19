pelican content -o output -s publishconf.py -v && ghp-import -m "-" --no-jekyll -b master output -c archiko.my.id && git push origin master
