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


date=`date --iso-8601` # 2019-07-05
last_saved_date="2019-07-04"

if [ "$date" = "$last_saved_date" ]; then
    echo "Equall!" # already executed today - exit script
    exit 0
else
    echo "Not equal!"  # script wasn't executed today
    last_saved_date=$date
    echo "$last_saved_date"
    bash get_data.sh $last_saved_date
fi
echo "Done"
python3.7 weight_chart.py

