ssh  jrao@elnux3.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/src; nohup chmod +x run_front_end.sh; nohup ./run_front_end.sh > /dev/null 2>&1 &'"
ssh  jrao@elnux1.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/src; nohup chmod +x run_catalogue.sh; nohup ./run_catalogue.sh > /dev/null 2>&1 &'"
ssh -i .ssh/id_rsa jrao@elnux2.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/src; nohup chmod +x run_order.sh; nohup ./run_order.sh > /dev/null 2>&1 &'"
ssh -i .ssh/id_rsa jrao@elnux7.cs.umass.edu "sh -c 'cd cs677/lab-2-rao-gupta/tests; nohup chmod +x run_client.sh; nohup ./run_client.sh > /dev/null 2>&1 &'"
