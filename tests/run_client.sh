cd test_1; python3 test1.py; cd ..;
cd test_2; python3 test2.py; cd ..;
cd test_3; python3 test3.py; cd ..;
cd test_4; python3 test4.py; cd ..;
cd test_5; python3 test5.py; cd ..;
sleep .5
curl http://elnux1.cs.umass.edu:34602/shutdown
sleep .5
curl http://elnux2.cs.umass.edu:34601/shutdown
sleep .5
curl http://elnux3.cs.umass.edu:34600/shutdown

