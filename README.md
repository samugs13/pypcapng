## pypcapng.py

Tool for adding and reading comments in PCAPNG files

### Usage

```bash
python3 pypcapng.py [-h] {add,read} ...
```

### Positional Arguments

- `{add,read}`
  - `add`: Add a comment in the specified packet and generate a new pcapng file with the comment inserted into that packet.
    
    ```bash
    python3 pypcapng.py add <input_pcapng_file> <output_pcapng_file> <comment> <packet_number>
    ```
  - `read`: Read the comment contained in the selected packet from the specified pcapng file.
      
    ```bash
    python3 pypcapng.py read <input_pcapng_file> <packet_number>
    ```

### Options

- `-h, --help`: Show help message and exit

### Example

![pypcapng](https://github.com/samugs13/pypcapng/assets/78796980/661a49ce-d4de-4f3a-a91b-52d08446608a)
