d=$(date +"%y.%m.%d")

filename="/home/opc/backups/minecraft.${d}.tar.gz"
echo "Trying to create backup file '${filename}'"

tar -cpvzf "${filename}" --exclude-tag=no_backup ~/minecraft/

find ~/backups -name '*.tar.gz' -mtime +7 -exec rm {} \;
