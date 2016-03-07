-初期設定
--純正ファーム->DDWRT化
1. ルータ本体に書かれているSSID,PASSWDで接続
2. http://192.168.11.1
3. ユーザー名:admin, パスワード:password,ログイン
4. 詳細設定->管理->ファームウェア更新
5. ファームウェアファイル名->DD-WRT/factory-to-dd-wrt.bin,更新実行
6. SSID:dd-wrt,PASSWD:無しで接続
7. http://192.168.1.1
8. Router Password->Router Username->****
9. Router Password->RouterPassword->****
10. Router Password->Re-enter to confirm->****
--Hostname
1. TopMenu->Setup->Basic Setup
2. ... -> Wan Setup->Router Name->AP**
3. ... -> Wan Setup->Hostname->AP**
--NTP
1. TODO
--Syslog
1. TODO
--SSH有効化
1. TopMenu->Services->Services
2.  ... ->SSHd->Enable
3.  ... ->Authorized Keys->****
--Telnet無効化
1. TopMenu->Services->Services
2. ... ->Telnet Disable
--HTTP無効化,HTTPS有効化
1. TopMenu->Administration->Management
2. ... ->Web Access->Protocol->HTTP->Uncheck
3. ... ->Web Access->Protocol->HTTPS->Check
--JFFS2有効化
1. TopMenu->Administration->Management
2. ... ->JFFS2 Support->Internal Flash Storage->Enable
3. ... ->JFFS2 Support->Clean Internal Flash Storage->Enable
--SSID
1. TopMenu->Wireless->BasicSettings
2. ... ->Physical Interface wl0->SSID->[ssid]
3. ... ->Physical Interface wl1->SSID->[ssid]
--PASSWD
1. TopMenu->Wireless->Wireless Security
2. ... ->Physical Interface wl0->Security Mode->WPA2 Personal
3. ... ->Physical Interface wl0->WPA Shared Key->****
4. ... ->Physical Interface wl1->Security Mode->WPA2 Personal
5. ... ->Physical Interface wl1->WPA Shared Key->****

Static IP化
1．TopMenu->Basic Setup->Network Setup
2. ... ->WAN Setup->WAN Connection Type->Connection Type->Static IP
3. ... ->WAN Setup->WAN Connection Type->WAN IP Address->203.178.156.1[+AP NUM]
4. ... ->WAN Setup->WAN Connection Type->Subnet Mask->255.255.254.0
5. ... ->WAN Setup->WAN Connection Type->Gateway->203.178.156.1
6. ... ->WAN Setup->WAN Connection Type->Static DNS1->8.8.8.8

-ブリッジ化
--SSH上
1. ssh root@dd-wrt
2. $brctl addif br0 vlan2
3. $brctl delif br0 vlan1
--WEB UI上
1．TopMenu->Basic Setup->Network Setup
2. ... ->Network Address Server Settings (DHCP)->Use DNSMasq for DNS->Uncheck
3. TopMenu->Setup->Networking
4. ... ->Port Setup->WAN Port Assignment->br0

-初期化
1. TopMenu->Administration->Factory Defaults
2. ...-> Restore Factory Defaults->Yes

