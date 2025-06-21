# PyValon
The software is used for Valon Synthesizer configuration.  
It supports V5015, V5007 and V5008 so far.  
The code for V5007 and V5008 refers to the code [here](https://github.com/nrao/ValonSynth), but it's totally written in Python.  
You can use this software to configure the output frequency, output power and set the reference clock.  
# Getting start
1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)(optional)  
Miniconda is recommended to create a vritual python environment, so that it won't mess up the python environment on your system.  
If miniconda is installed, please create and activate the python environment.
    ```
    conda create -n valon python=3.12
    conda activate valon
    ```
    **Note:** All Python3.x should work.
2. Install necessary packages
    ```
    pip install pyserial
    ```
3. clone the repository
    ```
    git clone https://github.com/liuweiseu/pyvalon.git
    ```
4. use the `v5015.py` or `v5008.py` to configure your Valon Synthesizer.
* V5015 configuration
    ```
    $ ./v5015.py -h
    usage: v5015.py [-h] [--dev DEV] [--baud BAUD] [--freq FREQ] [--amp AMP] [--ref REF] [--rfout RFOUT] [--pwr PWR] [--v]

    Usage for Setting V5015.

    options:
    -h, --help     show this help message and exit
    --dev DEV      Serial port for V5015.
    --baud BAUD    Baud rate.
    --freq FREQ    The frequency in MHz.
    --amp AMP      The amplitude in dBm.
    --ref REF      The reference source('internal' or 'external' or 'status')
    --rfout RFOUT  The rfout status('on' or 'off' or 'status')
    --pwr PWR      The power status('on' or 'off' or 'status')
    --v            Verbose
    ```
* V5007/V5008 configuration
    ```
    $ ./v5008.py -h
    usage: v5008.py [-h] [--dev DEV] [--baud BAUD] [--synth {A,B}] [--freq FREQ] [--amp {-4,-1,2,5}] [--ref {external,internal}] [--status] [--flash]

    Usage for Setting V5008.

    options:
    -h, --help            show this help message and exit
    --dev DEV             Serial port for V5008.
    --baud BAUD           Baud rate.
    --synth {A,B}         A - synthesizer 1; B - synthesizer 2.
    --freq FREQ           The frequency in MHz.
    --amp {-4,-1,2,5}     The amplitude level.
    --ref {external,internal}
                            The reference source('internal' or 'external')
    --status              Check the synthesizer status
    --flash               Write the parameters into flash
    ```