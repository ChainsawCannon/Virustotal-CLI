# VirusTotal-CLI
## This program has no affiliation with virustotal as a company and uses their APIs and libraries, please check the service [here](https://www.virustotal.com/gui/)

# About
Virustotal CLI (being called VT-CLI from here on out) is an open-source python tool using the official [vt-py libraries](https://github.com/VirusTotal/vt-py). This tool is designed to scan urls, hashes, and files on a users system.
Be aware this program requires a VirusTotal API key in order to function (Bring your own, put it in a txt file named "api_key.txt" and it should work fine!).

# How it works
VT-CLI uses the VirusTotal API to scan programs, hashes, and URLs. The API sends the information of what is given to VirusTotal itself and appears with information on the scan in the terminal. This example shown
below is Wanacry being scanned on the system:
![picture of sample malicious file scan](https://chainsawcannon.neocities.org/images/malicious-sample.png)
Then a non-malicious file being scanned (in this case [YataiDON by YonoKid](https://github.com/Yonokid/YataiDON))
![picture of non-malicious file scan](https://chainsawcannon.neocities.org/images/yataisample.png)
Then a sample URL (google.com) being scanned:
![picture of google.com being scanned](https://chainsawcannon.neocities.org/images/googlescan.png)
lastly, a known virus hash being scanned:
![picture of a hash scan](https://chainsawcannon.neocities.org/images/hashscan.png)

These are the basic capabilities I focused on to automate the process of scanning files given in a cyberattack plus URLs accessed by machines incorporated into a command and control server.
I would recommend using this program in an environment where scanning specific files is needed such as when going through a triage in a SIEM software (or on simulations like letsdefend). 

# Dependencies 
This program depends on vt-py by VirusTotal and hashlib, please make sure these are installed before using

# Manual
The usage for this program is as follows 
-hp [filepath] directs files to print their SHA256 hash (originally made for testing purposes)
-hs [hash] scans a hash given
-fs [filepath] scans a file given
-url [url] scans a URL given
-about will spit out a nice about message! 
You would execute the file as follows in the directory of the tool: python main.py -hp /home/user/file.txt (example for linux systems)
# Things to work on and potential add-ons
I would like to maybe make a gui version of this program to run natively on machines, if I somehow get my hands on a premium key I would also like to add tons of extra features!
# Credits
[VirusTotal for vt-py library](https://github.com/VirusTotal/vt-py)
[FreePythonCode for basic syntax for formatting](https://www.thiscodeworks.com/url-scanner-using-virustotal-api-python-coding-python-url-securty/6803711e01512a0014e81cfe)

Thanks for reading, this was made with 💜 by ChainsawCannon/Shay (She/They)
No AI was used in the creation of this tool. 
