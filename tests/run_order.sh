#!/usr/bin/expect

spawn ssh jrao@elnux2.cs.umass.edu "cd cs677/lab-2-rao-gupta/src; 
source venv/bin/activate;
python3 order/order.py"
expect "password"
send "Vaticancameos1!\r"
interact
