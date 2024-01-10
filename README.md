## pypcapng.py

Tool for adding and reading comments in PCAPNG files

### Usage

```bash
pypcapng.py [-h] {add,read} ...
```

### Positional Arguments

- `{add,read}`
  - `add`: Add a comment in the specified packet and generate a new pcapng file with the comment inserted into that packet.
    
    ```bash
    pypcapng.py add <input_pcapng_file> <output_pcapng_file> <comment> <packet_number>
    ```
  - `read`: Read the comment contained in the selected packet from the specified pcapng file.
      
    ```bash
    pypcapng.py read <input_pcapng_file> <packet_number>
    ```

### Options

- `-h, --help`: Show help message and exit

### Example
![pypcapng](https://github.com/samugs13/pypcapng/assets/78796980/18395399-fb10-4ec6-aa05-dfe9cd725cc9)
