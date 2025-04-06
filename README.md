# ssidpwdgen
Python tool to generate encrypted string for ssid, wifi_password
Need to pip install cryptography
Run python ssidpwdgen -h for usage
The Fernet key and encrypted data string are displayed
The decrypt function is to verify the encryption
The code that receives the encrypted data needs to fow the decode function to get back the ssid and pwd
