ssh aayushgupta@elnux3.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/src; nohup chmod +x run_front_end.sh; nohup ./run_front_end.sh > /dev/null 2>&1 &'"
ssh aayushgupta@elnux1.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/src; nohup chmod +x run_catalogue.sh; nohup ./run_catalogue.sh > /dev/null 2>&1 &'"
ssh aayushgupta@elnux2.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/src; nohup chmod +x run_order.sh; nohup ./run_order.sh > /dev/null 2>&1 &'"
sleep .5
ssh aayushgupta@elnux7.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/tests; nohup chmod +x run_client.sh; nohup ./run_client.sh > /dev/null 2>&1 &'"
#cd tests/ && ./run_client.sh ;
#sleep .5
#curl http://elnux1.cs.umass.edu:34602/shutdown
#sleep .5
#curl http://elnux2.cs.umass.edu:34601/shutdown
#sleep .5
#curl http://elnux3.cs.umass.edu:34600/shutdown