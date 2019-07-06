check_exe () {
if [ "$1" = "$2" ]; then
    # already executed today - exit script
    return 1
else
    # script wasn't executed today
    last_saved_date=$2
    # save new data from the user
    bash get_data.sh $1
    return 0
fi
}


last_saved_date="2019-07-06"
date=`date --iso-8601` # 2019-07-06

# check if script has already been executed today and we have the data from the user
check_exe $date $last_saved_date
