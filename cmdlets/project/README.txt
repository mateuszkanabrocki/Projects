How to run this:

example:
history | ./tail.py -10 | ./sed.py "s/^[ 0-9]*//" | ./cut.py -d ' ' -f 1,3 | ./sort.py - | ./uniq.py

Existing scripts:
./tail.py
./sed.py
./cut.py
./sort.py
