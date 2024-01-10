# pypcapng
Simple tool for adding and reading comments in PCAPNG files.

usage: pypcapng.py [-h] {add,read} ...

positional arguments:
  {add,read}
    add       Add a comment in the specified packet and generate a new pcapng file with the comment inserted into that packet
    read      Read the comment contained in the selected packet from the specified pcapng file

options:
  -h, --help  show help message and exit
