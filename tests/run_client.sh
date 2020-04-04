#!/usr/bin/expect

spawn ssh jrao@elnux7.cs.umass.edu "curl -o out.json http://elnux3.cs.umass.edu:34600/search/distributed%20systems"
expect "password"
send "Vaticancameos1!\r"
interact
