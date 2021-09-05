eval rm -rf output __py* && pelican content -o output -s pelican* && ghp-import output && git push origin gh-pages
