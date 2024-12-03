
import serial
import time

RECV_LEN = 1024

class Valon(object):
    """
    Description:
        This class is defined for all the valon devices,
        which uses serial port.
    """
    def __init__(self, dev, baud):
        self.ser = serial.Serial(dev,baud,timeout=0.5, rtscts=False, xonxoff=False)
    
    def sendcmd(self, cmd):
        self.ser.write(cmd.encode('utf-8'))
        r = self.ser.read(RECV_LEN).decode()
        return r
    def close(self):
        self.ser.close()

class V5015(Valon):
    """
    Description:
        This class is based on Valon class, 
        and is especially for V5015
    """
    def SetFreq(self, f=-1, u='MHz', verbose=False):
        """
        Set Frequency.

        Inputs:
            - f (float): the freqency value.
            - u (str): freqency unit, such as "MHz".
            - verbose (bool): be verbose
                Default=False
        Ouputs:
            - r (str): the frequency been set
        """
        if f == -1:
            cmd = 'F\r'
        else:
            if u == 'MHz' and f > 15000:
                f = 15000
                print('The max freq is 15000MHz.')
            elif u == 'GHz' and f > 15:
                f = 15
                print('The max freq is 15GHz.')
            cmd = 'F ' + str(f) + ' ' + u + '\r'
        r = self.sendcmd(cmd)
        if verbose:
            print(r)
        if f == -1:
            rs = r.split(';')[0].split(' ')
        else:
            rs = r.split('\r')[0].split(' ')
        return rs[1]+rs[2]
    
    def SetAmp(self, a=100, verbose=False):
        """
        Set Amplitude in dBm.

        Inputs:
            - a (float): amplitude in dBm.
            - verbose (bool): be verbose
                Default=False
        Ouputs:
            - r (str): the amplitude been set
        """
        if a == 100:
            cmd = 'PWR\r'
        else:
            if a > 14:
                a = 14
                print('The max amplitude is 14dBm.')
            cmd = 'PWR ' + str(a) + '\r' 
        r = self.sendcmd(cmd)
        if verbose:
            print(r)
        
        rs0 = r.split(';')[0].split(' ')
        rs1 = r.split(';')[1].split(' ')[3].split('\r')
        if a == 100:
            return rs0[1]+rs1[0]
        else:
            return rs0[2]+rs1[0]
        
    
    def SetRef(self, s='', f=10, verbose=False):
        """
        Set Ref and Ref source in MHz 

        Inputs:
            - s (str): reference source('internal' or 'external'). 
                Default=''
            - f (int): reference frequency in MHz. It should be in the ref_list.
                Default=10
            - verbose (bool): be verbose
                Default=False
        Outputs:
            - r (str): ref source and ref frequency in MHz
        """
        if s == 'internal':
            src = str(0)
        elif s == 'external':
            src = str(1)
        else:
            src = ''
        # set refernce source first
        cmd = 'REFS ' + src + '\r'
        r = self.sendcmd(cmd)
        if verbose:
            print(r)
        rs = r.split(';')[0].split(' ')
        ref_src=''
        if rs[2] == '0':
            ref_src += 'internal'
        elif rs[2] == '1':
            ref_src += 'external'
        # ser reference frequency in MHz
        cmd = 'REF ' + str(f) + ' ' + 'MHz\r'
        r = self.sendcmd(cmd)
        if verbose:
            print(r)
        rs1 = r.split(';')[0].split(' ')
        rs2 = r.split(';')[0].split(' ')[2].split('\r')
        ref_val = rs1[1] + rs2[0]
        return ref_src + ' ' + ref_val
    
    def RFout(self, s='', verbose=False):
        """
        Turn on/off the RFout.

        Inputs:
            - s (str): RFout status('on' or 'off')
            - verbose (bool): be verbose
                Default=False
        Outputs:
            - r (str): RFout status
        """
        if len(s) == 0:
            cmd = 'OEN\r'
            index = 1
        else:
            cmd = 'OEN ' + s.upper() + '\r'
            index = 2
        r = self.sendcmd(cmd)
        if verbose:
            print(r)
        rs = r.split(';')[0].split(' ')
        if rs[index] == '0':
            return 'OFF'
        elif rs[index] == '1':
            return 'ON'
    
    def PWRout(self, s='', verbose=False):
        """
        Power on/off the synth.

        Inputs:
            - s(str): Power status('on' or 'off')
            - verbose (bool): be verbose
                Default=False
        Ouputs:
            - r(str): Power status
        """
        if len(s) == 0:
            cmd = 'PDN\r'
            index = 1
        else:
           cmd = 'PDN ' + s.upper() + '\r' 
           index = 2
        r = self.sendcmd(cmd)
        if verbose:
            print(r)
        rs = r.split(';')[0].split(' ')
        if rs[index] == '0':
            return 'OFF'
        elif rs[index] == '1':
            return 'ON'
        
