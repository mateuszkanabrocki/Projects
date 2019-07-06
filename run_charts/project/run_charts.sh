#!/bin/bash


# write a script:
# script1: bash
# 	cron: each day after relooging if not possible at 9, 19, 17 18 o-clock
# 	in script: check today's date if already executed this day (variable storing last date of execution) -
#     do not execute else: save this variable to today's date and execute script2

# script2: bash
# 	check if there is weight in a text file for today
# 	if not prompts for the weight 
# 
# script3: python
# append to the file using vim (make a copy of the weight data file)
# 	finally go back to script2 -> go back to script1
	
# script1:
# 	execute run chart
	
# more:
# add tasks_data in the same script
# make txt data files with sticking bit - you can change it only through the script


save_exe_date () {
file=check_execution.sh
vi $file <<EndOfCommands
/last_saved_date="
!!echo 'last_saved_date="`date --iso-8601`"'

:x
EndOfCommands
}


modify_script () {
if [ $? -eq 0 ]; then  # if we've just saved new date - for today
    save_exe_date
    # edit stored value of last_saved_date in check_execution.sh
fi
}


# check if script has already been executed today and we have the data
bash check_execution.sh
# modify last execution date - hardcoded in the script
modify_script
# run the chart
python3.7 weight_chart.py  
