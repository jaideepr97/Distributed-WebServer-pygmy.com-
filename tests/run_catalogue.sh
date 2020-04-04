#!/usr/bin/expect

spawn ssh jrao@elnux1.cs.umass.edu "cd cs677/lab-2-rao-gupta/src; 
source venv/bin/activate;
python3 catalogue/catalogue.py"
expect "password"
send "Vaticancameos1!\r"
interact
