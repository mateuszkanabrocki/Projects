#!/bin/bash

# more:
# option to break the script with no charts - try
# make txt data files with sticking bit - you can change it only through the script

source check_last_exe.sh
# last_saved_tasks
# last_saved_weight
# last_saved_disk1
# last_saved_disk2


save_date_weight () {
vi check_last_exe.sh <<EndOfCommands
/last_saved_weight="
!!echo 'last_saved_weight="`date --iso-8601`"'

:x
EndOfCommands
}


save_date_tasks () {
vi check_last_exe.sh <<EndOfCommands
/last_saved_tasks="
!!echo 'last_saved_tasks="`date --iso-8601 --date="1 day ago"`"'

:x
EndOfCommands
}


save_date_disk1 () {
vi check_last_exe.sh <<EndOfCommands
/last_saved_disk1="
!!echo 'last_saved_disk1="`date --iso-8601`"'
:x
EndOfCommands
}


save_date_disk2 () {
vi check_last_exe.sh <<EndOfCommands
/last_saved_disk2="
!!echo 'last_saved_disk2="`date --iso-8601`"'

:x
EndOfCommands
}


save_new_data () {
new_data="$1 $2"
file=$3
vi $file <<EndOfCommands
Go!!echo "$new_data"

:x
EndOfCommands
}


main () {
echo -e "Hello.\nHow you doin?"

# check if script has already been executed today and we have the data from the user


today="`date --iso-8601`"
if [ "$today" != "$last_saved_weight" ]; then  # it's the first execution today
	echo -e "What was your weight today?"
	read given_weight
	file="weight_stat.txt"
	save_new_data $today $given_weight $file 2> /dev/null
	# modify last execution date - hardcoded in the script
    save_date_weight 2> /dev/null
	# run the chart
	python3.7 weight_chart.py
	clear
fi


yesterday="`date --iso-8601 --date="1 day ago"`"
# check if script has already been executed today and we have the data from the user
if [ "$yesterday" != "$last_saved_tasks" ]; then  # it's the first execution today
	echo -e "How many tasks did you do yesterday?"
	read given_tasks
	file="tasks_stat.txt"
	save_new_data $yesterday $given_tasks $file 2> /dev/null
	# modify last execution date - hardcoded in the script
    save_date_tasks 2> /dev/null
	# run the chart
	./tasks_chart.py
	clear
fi


today="`date --iso-8601`"
# check if script has already been executed today and we have the data from the user
if [ "$today" != "$last_saved_disk1" ]; then  # it's the first execution today
	echo -e "Do you want to display storage usage charts? (y/n)"
	read answer
	disk_used1=`df -h | grep /dev/sdb2 | sed "s/ \+/ /g" | cut -d " " -f 5 | cut -b 1-2`
	file="disk1_stat.txt"
	save_new_data $today $disk_used1 $file 2> /dev/null
	# modify last execution date - hardcoded in the script
    save_date_disk1 2> /dev/null

	disk_used2=`df -h | grep /dev/sdb1 | sed "s/ \+/ /g" | cut -d " " -f 5 | cut -b 1`
	file="disk2_stat.txt"
	save_new_data $today $disk_used2 $file 2> /dev/null
	# modify last execution date - hardcoded in the script
    save_date_disk2 2> /dev/null

	# run the chart
	echo "$answer"
	if [ "$answer" == "y" ]; then
	./disk1_chart.py
	./disk2_chart.py
	fi
	clear
fi
}

main
