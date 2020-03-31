# please run this shell in project root dir

last_modified_time=$(stat requirements.txt | sed -n '6p' | awk '{print $2,$3}')

last_modified_timestamp=$(date -d "$last_modified_time" +"%s")

now_timestamp=$(date +%s)

# seconds
modified_threshold=3600

if [ $((now_timestamp - last_modified_timestamp)) -ge $modified_threshold ]; then
  echo 'create new requirements.txt ...'
  pip freeze >requirements.txt
fi

git add .

git commit -m "$1"

git push origin master
