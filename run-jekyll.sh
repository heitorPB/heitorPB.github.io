echo "getting rid of old files at _site"
rm -rf _site/*
echo -e "Gonne!\n\n"

echo -e "If you want to create output with drafts run:"
echo -e "sh $0 --drafts\n\n"
echo -e "If you want verbose output run:"
echo -e "sh $0 --verbose\n\n"

echo -e "Running a jekyll server $1 at 127.0.0.1:4000\n\n"
bundle exec jekyll serve --lsi $1

echo -e "\n\n"
echo "Oh, you are evil! you killed jekyll server! :O"

echo -e "\n\nIf you want to upload to github, build the files instead of \
serving them!!"
