#! /bin/bash

source /data/Tools/miniconda3/bin/activate valon

echo `which python`

if [ $1 == 'on' ]; then
	./v5015.py --dev /dev/ttyUSB1 --freq 50 --amp 4 --rfout on --pwr on --v
else
	./v5015.py --dev /dev/ttyUSB1 --freq 50 --amp 4 --rfout off --pwr off --v 
fi

