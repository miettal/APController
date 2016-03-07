ssid=taisyo
psk=taisyoman
power=100
ch5g=100
ch24g=1

#wl -i eth1 channels #5GHz
#36 40 44 48 52 56 60 64 100 104 108 112 116 132 136 140 144 149 153 157 161 165 
#wl -i eth2 channels #2.4GHz
#1 2 3 4 5 6 7 8 9 10 11

echo setting...
# eth1 wl0 5GHz
## ssid
wl -i eth1 ssid $ssid
## security
nvram set wl0_akm=psk2 
nvram set wl0_security_mode=psk2 
nvram set wl0_wpa_psk=$psk
nvram set wl0_crypto=tkip 
nvram set wl0_wds0=*,auto,tkip,psk2,gateway-testbed,$psk
nvram set wl0_wep=disabled 
## power
wl -i eth1 txpwr1 -dm $power
## channel
wl -i eth1 channel $ch5g

# eth2 wl1 2.4GHz
## ssid
wl -i eth2 ssid $ssid
## security
nvram set wl1_akm=psk2 
nvram set wl1_security_mode=psk2 
nvram set wl1_wpa_psk=$psk
nvram set wl1_crypto=tkip 
nvram set wl1_wds0=*,auto,tkip,psk2,gateway-testbed,$psk
nvram set wl1_wep=disabled 
## power
wl -i eth2 txpwr1 -dm $power
## chanel
wl -i eth2 channel $ch24g

echo
echo config is...
# print config
echo "eth1(2.4GHz)"
wl -i eth1 ssid
echo Current PSK:`nvram get wl0_wpa_psk`
wl -i eth1 txpwr1

echo "eth1(2.4GHz)"
wl -i eth2 ssid
echo Current PSK:`nvram get wl1_wpa_psk`
wl -i eth2 txpwr1

echo
# save config
echo saving...
nvram commit

echo
# restart
echo restarting...
wl radio off
wl radio on
stopservice wan
startservice wan

echo
echo "done!"
