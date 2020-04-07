# 677 Lab 2

Overview

1. All the tests are written in python scripts within their respective sub-directories
2. A central ‘run_client.sh’ bash script calls all the test python scripts sequentially
3. The tests spin up a varying number of clients - with each client creating its own respective output file of the format ‘client_<client_number>_output.txt’ and ‘client_<client_number>_metrics.txt’ for each test within its own sub - directory on the local machine
4. All the clients run a fixed number of requests (varying across tests) which are randomly generated from the available services (search/lookup/buy) 


Directions to run

1. The tests themselves  can be executed individually or all together by executing run_client.sh on their local machines
2. Additionally, graders can execute run_pygmy.sh on their local machines - which is the master script that handles remote login into all the edlab machines, spinning up of all the servers on each machine and execution of all tests (i.e, calling run_client.sh) through a single command 

