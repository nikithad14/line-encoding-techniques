'''2025 Author: Nikitha D <dnikitha2020@gmail.com>'''
'''
Dependencies : numpy matplotlib
Description:
      This Python script visualizes different line encoding techniques used in digital communication.
      It takes a binary input and generates signals for NRZ, RZ, Manchester, Differential Manchester, AMI, and Pseudoternary encoding. 
      The encoded signals are plotted alongside the clock and input signals for easy comparison.
'''
import numpy as np
import matplotlib.pyplot as plt
data = input("Enter the input bits: ")
data = [int(i) for i in data]
clockfrequency = 1
clockperiod = 1/clockfrequency
t = np.arange(0,len(data),0.01)
clock = np.where((t%clockperiod)<(clockperiod/2),1,-1)

def input_signal(clock,data):
    encoded_signal=np.zeros_like(clock)
    for i in range(len(data)):
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = data[i]
    return encoded_signal

def nrz(clock,data):
    encoded_signal=np.zeros_like(clock)
    for i in range(len(data)):
        if(data[i]==1):
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 1
        else:
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 0
    return encoded_signal

def nrz_l(clock,data):
    encoded_signal=np.zeros_like(clock)
    for i in range(len(data)):
        if(data[i]==1):
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = -1
        else:
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 1
    return encoded_signal

def nrz_i(clock,data):
    encoded_signal=np.zeros_like(clock)
    x=data
    x[0]=1
    y=-1
    for i in range(len(data)):
        if(x[i]==1):
            y=y*(-1)
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = y
        else:
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = y
    return encoded_signal

def rz(clock,data):
    encoded_signal=np.zeros_like(clock)
    for i in range(len(data)):
        if(data[i]==1):
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 0.5) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 1
            start_idx = int((i + 0.5) * len(clock) / len(data))
            end_idx = int(i * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 0
        else:
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 0.5) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = -1
            start_idx = int((i + 0.5) * len(clock) / len(data))
            end_idx = int(i * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 0
    return encoded_signal

def manchester(clock, data):
    encoded_signal = np.zeros_like(clock)
    for i in range(len(data)):
        start_idx = int(i * len(clock) / len(data))
        mid_idx = int((i + 0.5) * len(clock) / len(data))
        end_idx = int((i + 1) * len(clock) / len(data))
        if data[i] == 1:
            encoded_signal[start_idx:mid_idx] = -1
            encoded_signal[mid_idx:end_idx] = 1
        else:
            encoded_signal[start_idx:mid_idx] = 1
            encoded_signal[mid_idx:end_idx] = -1
    return encoded_signal

def diff_manchester(clock,data):
    encoded_signal = np.zeros_like(clock)
    bit_length = int(len(clock) / len(data))
    encoded_signal[0:int(0.5 * bit_length)] = 1
    encoded_signal[int(0.5 * bit_length):bit_length] = -1
    for i in range(1, len(data)):
        if data[i] == 1:
            encoded_signal[i * bit_length:(i + 1) * bit_length] = -encoded_signal[(i - 1) * bit_length:i * bit_length]
        else:
            encoded_signal[i * bit_length:(i + 1) * bit_length] = encoded_signal[(i - 1) * bit_length:i * bit_length]
    return encoded_signal

def ami(clock,data):
    encoded_signal = np.zeros_like(clock)
    x=(-1)
    for i in range(len(data)):
        if(data[i]==1):
            x *= -1
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = x
        else:
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = data[i]
    return(encoded_signal)

def pseudo(clock,data):
    encoded_signal = np.zeros_like(clock)
    x=(-1)
    for i in range(len(data)):
        if(data[i]==0):
            x *= -1
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = x
        else:
            start_idx = int(i * len(clock) / len(data))
            end_idx = int((i + 1) * len(clock) / len(data))
            encoded_signal[start_idx:end_idx] = 0
    return(encoded_signal)
    
input_signal=input_signal(clock,data)
nrz_encoding=nrz(clock,data)
nrz_l_encoding=nrz_l(clock,data)
nrz_i_encoding=nrz_i(clock,data)
rz_encoding=rz(clock,data)
manchester_encoding=manchester(clock,data)
differential_manchester_encoding=diff_manchester(clock,data)
ami_encoding=ami(clock,data)
pseudoternary_encoding=pseudo(clock,data)

plt.figure(figsize=(12, 8))
plt.subplot(6, 1, 1)
plt.plot(t, clock, label='Clock Signal')
plt.legend()
plt.subplot(6, 1, 2)
plt.plot(t, input_signal, label='Input Signal')
plt.legend()
plt.subplot(6, 1, 3)
plt.plot(t, nrz_encoding, label='NRZ Encoded Signal')
plt.legend()
plt.subplot(6, 1, 4)
plt.plot(t, nrz_l_encoding, label='NRZ level Encoded Signal')
plt.legend()
plt.subplot(6, 1, 5)
plt.plot(t, nrz_i_encoding, label='NRZ invert Encoded Signal')
plt.legend()
plt.subplot(6, 1, 6)
plt.plot(t, rz_encoding, label='RZ Encoded Signal')
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
plt.subplot(6, 1, 1)
plt.plot(t, clock, label='Clock Signal')
plt.legend()
plt.subplot(6, 1, 2)
plt.plot(t, input_signal, label='Input Signal')
plt.legend()
plt.subplot(6, 1, 3)
plt.plot(t, manchester_encoding, label='Manchester Encoded Signal')
plt.legend()
plt.subplot(6, 1, 4)
plt.plot(t, differential_manchester_encoding, label='Differential Manchester Encoded Signal')
plt.legend()
plt.subplot(6, 1, 5)
plt.plot(t, ami_encoding, label='AMI Encoded Signal')
plt.legend()
plt.subplot(6, 1, 6)
plt.plot(t, pseudoternary_encoding, label='Pseudoternary Encoded Signal')
plt.legend()

plt.tight_layout()
plt.show()






            
