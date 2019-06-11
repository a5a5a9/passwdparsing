README

This Utility parses the UNIX /etc/passwd and /etc/groups files and combine the data into a single JSON output. 


Installation

$ git clone https://github.com/adalandrade/passwdparsing.git

$ cd passwdparsing

Then you can use the following options to run the script.

$ python3 passwd-parser.py -r -p /path/to/your/file/passwd -g /path/to/your/file/group

usage: passwd-parser.py [-h] [--run] [--passwd PASSWD] [--group GROUP]



optional arguments:


  -h, --help            show this help message and exit
  
  -r, --run             run the program
  
  -p, --passwd          passwd_path
  
  -g, --group           group_path                      
  

Default passwd path  '/etc/passwd'
Default group path   '/etc/group'



