last_modified_time=$(stat requirements.txt | sed -n '6p' | awk '{print $2,$3}')

last_modified_timestamp=$(date -d "$last_modified" +"%s")

now_timestamp=$(date +%s)

# seconds
modified_threshold=3600

if [ $(($now_timestamp-$last_modified_timestamp)) -ge $modified_threshold ]; then
  echo 'good job !'
fi
