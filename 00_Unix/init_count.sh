sed  's/[^a-zA-Z]\+/\n/g' | uconv -x upper | sort | uniq -i > $$words
grep -oi '^[^aeiouÄÁÀÂÅĄĀǍÆẮĂⱯẢⱭĒÊÉẾÈĚĖĘËÏĮȊȊÎİÍÌĪꞮƐƏÒÖŐÓỘŌÔØƱŮŰŲÛÜÚŪÙǓŬ]\+' < $$words| sort | uniq > $$init.consonants
rm $$words
