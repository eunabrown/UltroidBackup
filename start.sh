#!/bin/bash

# Start pyUltroid in the background
python3 -m pyUltroid &

# Start server.py in the foreground
exec python3 server.py
