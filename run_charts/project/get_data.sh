save_data () {
data="$1 $2"
file=weight_stat.txt
vi $file <<EndOfCommands
Go!!echo "$data"

:x
EndOfCommands
}

echo -e "Hello. How you doin?\nWhat was your weight today?"
read given_weight
save_data $1 $given_weight
