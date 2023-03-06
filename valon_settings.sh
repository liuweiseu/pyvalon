#! /bin/bash

source /data/Tools/miniconda3/bin/activate
conda activate valon

echo `which python`

if [ $1 == 'on' ]; then
	./v5015.py --freq 1000 --amp 4 --rfout on --pwr on
else
	./v5015.py --freq 1000 --amp 4 --rfout off --pwr off
fi

