sed  's/[^a-zA-Z]\+/\n/g' | uconv -x upper | sort | uniq -i > $$words
grep -oi '[^aeiouÄÁÀÂÅĄĀǍÆẮĂⱯẢⱭĒÊÉẾÈĚĖĘËÏĮȊȊÎİÍÌĪꞮƐƏÒŐÖÓỘŌÔØƱŮŰŲÛÜÚŪÙǓŬ]\+$' < $$words| sort | uniq > $$ending.consonants
rm $$words
