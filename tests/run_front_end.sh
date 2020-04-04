#!/usr/bin/expect

spawn ssh jrao@elnux3.cs.umass.edu "cd cs677/lab-2-rao-gupta/src; 
source venv/bin/activate;
python3 front-end/front-end.py"
expect "password"
send "Vaticancameos1!\r" 
interact

