import os

os.system("raspivid -o - -t 0 -hf -w 400 -h 200 -fps 16 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264")
