sed 's/[^a-zA-Z]\+/\n/g' | grep -v '^$' > $$words
tail -n +2 < $$words > $$nextwords
paste $$words $$nextwords | sort | uniq -c | sort -nr

rm $$words 
rm $$nextwords
