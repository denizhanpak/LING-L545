#[usage: sh consonant_count.sh (corpus)]

sed  's/[^a-zA-Z]\+/\n/g' < $1 | uconv -x upper | sort | uniq -i > $$words
grep -oi '[^aeiouÄÁÀÂÅĄĀǍÆẮĂⱯẢⱭĒÊÉẾÈĚĖĘËÏĮȊȊÎİÍÌĪꞮƐƏÒŐÖÓỘŌÔØƱŮŰŲÛÜÚŪÙǓŬ]\+$' < $$words| sort | uniq -c > wiki_cons.end
grep -oi '^[^aeiouÄÁÀÂÅĄĀǍÆẮĂⱯẢⱭĒÊÉẾÈĚĖĘËÏĮȊȊÎİÍÌĪꞮƐƏÒÖŐÓỘŌÔØƱŮŰŲÛÜÚŪÙǓŬ]\+' < $$words| sort | uniq -c > wiki_cons.begin
rm $$words

echo "Number of Initial Consonants"
wc -w wiki_cons.begin

echo "Number of Terminal Consonants"
wc -w wiki_cons.end
