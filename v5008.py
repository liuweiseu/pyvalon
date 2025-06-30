#! /usr/bin/env python
"""
usage: v5015.py [-h] [--dev DEV] [--baud BAUD] [--freq FREQ] [--amp AMP] [--ref REF] [--rfout RFOUT] [--pwr PWR] [--v]

Usage for Setting V5015.

optional arguments:
  -h, --help     show this help message and exit
  --dev DEV      Serial port for V5015.
  --baud BAUD    Baud rate.
  --freq FREQ    The frequency in MHz.
  --amp AMP      The amplitude in dBm.
  --ref REF      The reference source('internal' or 'external' or 'status')
  --rfout RFOUT  The rfout status('on' or 'off' or 'status')
  --pwr PWR      The power status('on' or 'off' or 'status')
  --v            Verbose
"""
from Valon import V500X
from argparse import ArgumentParser

JUST_LEN = 12

def CheckStatus(synth, s):
    print('%s: %s'%('synthesizer'.ljust(JUST_LEN), s))
    freq = synth.GetFreq(s)
    print('%s: %.02f'%('Freq(MHz)'.ljust(JUST_LEN), freq))
    rf_level = synth.GetRFLevel(s)
    print('%s: %d'%('RF Level'.ljust(JUST_LEN), rf_level))
    ref = synth.GetRefSelect()
    print('%s: %s'%('Reference'.ljust(JUST_LEN), ref))
    lock = synth.GetPhaseLock(s)
    if lock == True:
        print('%s: %s'%('Lock'.ljust(JUST_LEN), 'Locked'))  
    else:
        print('%s: %s'%('Lock'.ljust(JUST_LEN), 'Unlocked'))  

def GetSynth(args):
    if args.synth == None:
        print('Please specify which synthesizer you want to use: A - synthesizer 1; B - synthesizer 2.')
    else:
        return args.synth

def main():
    parser = ArgumentParser(description="Usage for Setting V5008.")
    parser.add_argument('--dev',dest='dev', type=str, default='/dev/ttyUSB0',help='Serial port for V5008.')
    parser.add_argument('--baud',dest='baud', type=int, default=9600, help='Baud rate.')
    parser.add_argument('--synth',dest='synth', type=str, choices=['A', 'B'], default=None, help='A - synthesizer 1; B - synthesizer 2.')
    parser.add_argument('--freq', dest='freq', type=float, help='The frequency in MHz.')
    parser.add_argument('--amp', dest='amp', type=int, choices=[-4, -1, 2, 5], default=-999, help='The amplitude level.')
    parser.add_argument('--ref',dest='ref',type=str, choices=['external', 'internal'], default='', help='The reference source(\'internal\' or \'external\')')
    parser.add_argument('--status', dest='status', default=False, action='store_true', help='Check the synthesizer status')
    parser.add_argument('--flash', dest='flash', default=False, action='store_true', help='Write the parameters into flash')
    args = parser.parse_args()
    
    print('%s: %s'%('Dev'.ljust(JUST_LEN),args.dev))
    print('%s: %s'%('Baud'.ljust(JUST_LEN),args.baud))

    synth = V500X(args.dev, args.baud)    
    # set freq
    if args.freq :
        s = GetSynth(args)
        r = synth.SetFreq(s, args.freq)
        if r == False:
            print('Frequency set faild.')
        else:
            freq = synth.GetFreq(s)
            print('%s: %s'%('synthesizer'.ljust(JUST_LEN), s))
            print('%s: %.02f'%('Freq(MHz)'.ljust(JUST_LEN), freq))
    # set RF level
    if args.amp != -999:
        s = GetSynth(args)
        r = synth.SetRFLevel(s, args.amp)
        if r == False:
            print('Amp set faild.')
        else:
            rf_level = synth.GetRFLevel(s)
            print('%s: %s'%('synthesizer'.ljust(JUST_LEN), s))
            print('%s: %d'%('RF Level'.ljust(JUST_LEN), rf_level))
    # set ref
    if args.ref != '':
            r = synth.SetRefSelect(args.ref)
            if r == False:
                print('Reference set faild.')
            else:
                ref = synth.GetRefSelect()
                print('%s: %s'%('Reference'.ljust(JUST_LEN), ref))
    if args.status:
        print('')
        CheckStatus(synth, 'A')
        print('')
        CheckStatus(synth, 'B')
    if args.flash:
        if args.status == False:
            print('')
            CheckStatus(synth, 'A')
            print('')
            CheckStatus(synth, 'B')
        synth.Flash()
        print('')
        print('The parameters have been written into flash!')
    synth.close()

if __name__=='__main__':
    main()
