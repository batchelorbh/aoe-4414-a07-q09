#!/usr/bin/env python
# max_bitrate.py
#
# Calculates maximum achievable bitrate
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km
#                               rx_gain_db n0_j bw_hz
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    tx_w                transmitted power in watts
#    tx_gain_db          transmitter antenna gain in decibels
#    freq_hz             carrier frequency in hertz
#    dist_km             distance between transmitter & receiver in kilometers
#    rx_gain_db          receiver antenna gain in decibels
#    n0_j                noise spectral density in joules
#    bw_hz               bandwidth in hertz
#
# Output:
#    Prints the maximum achievable bitrate in bits per second (floored)
#
# Revision history:
#    12/06/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
import math

#Define constants
c = 2.99792458e8 #Speed of light in m/s

#Pre-initialize input parameters
tx_w = float('nan') #transmitted power in watts
tx_gain_db = float('nan') #transmitter antenna gain in decibels
freq_hz = float('nan') #carrier frequency in hertz
dist_km = float('nan') #between transmitter & receiver in kilometers
rx_gain_db = float('nan') #receiver antenna gain in decibels
n0_j = float('nan') #noise spectral density in joules
bw_hz = float('nan') #bandwidth in hertz

#Arguments are strings by default
if len(sys.argv) == 8:
   tx_w = float(sys.argv[1])
   tx_gain_db = float(sys.argv[2])
   freq_hz = float(sys.argv[3])
   dist_km = float(sys.argv[4])
   rx_gain_db = float(sys.argv[5])
   n0_j = float(sys.argv[6])
   bw_hz = float(sys.argv[7])
else:
   print(('Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km ' \
          'rx_gain_db n0_j bw_hz'))
   sys.exit()

#Main body of script
L_l = 10**(-1 / 10) #Transmitter to antennta line loss
L_a = 1 #Atmospheric loss
lambda_ = c / freq_hz; #wavelength
S = dist_km * 1000 #distance in meters

C = tx_w * L_l * tx_gain_db * (lambda_ / (4 * math.pi * S))**2 * L_a * rx_gain_db
N = n0_j * bw_hz

r_max = bw_hz * math.log((1+C/N),2)

print(math.floor(r_max))