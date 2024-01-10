from scapy.all import Packet, XStrField, rdpcap, PcapWriter
import argparse

# Colors code
class color:
    RED = "\033[91m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    END = "\033[0m"

# Create a simple protocol 
class Comment(Packet):
    name = "Comment Protocol"
    fields_desc=[ XStrField("comment", 30) ]

def add_comment_to_packet(input_pcapng_file, output_pcapng_file, comment, packet_number):
    
    print(color.BLUE + '\n[+]' + color.END + f' Reading {input_pcapng_file}...')
    
    # Load input file packets into packets array
    packets = rdpcap(input_pcapng_file) 
    
    # Adjust index
    packet_index = packet_number - 1 
    
    # Open file to write
    o_open_file = PcapWriter(output_pcapng_file) 
    
    if 0 <= packet_index < len(packets):
 
        for p in packets:
            if p == packets[packet_index]:
                print(color.BLUE + '\n[+]' + color.END + ' Adding comment...\n')
                p /= Comment(comment=comment)  # Append a layer with the encoded comment to the packet
                p.show()
                o_open_file.write(p)  # Write packet in new file
                o_open_file.flush()
                print(color.BLUE + '\n[+]' + color.END + f' Generating {output_pcapng_file}...')

            else:
                o_open_file.write(p) # Write packet in new file
                o_open_file.flush()

        print(color.GREEN + '\n[+]' + color.END + ' Comment added succesfully\n')
    
    else:
        print("Packet number out of range")
        exit(1)

def read_comment_from_packet(input_pcapng_file, packet_number):

    print(color.BLUE + '\n[+]' + color.END + f' Reading {input_pcapng_file}...\n')
    packets = rdpcap(input_pcapng_file)
    packet_index = packet_number - 1 # Adjust index

    if 0 <= packet_index < len(packets):
        packet = packets[packet_index]
        layer = packet.lastlayer()
        if str(layer)=="Padding":
            comment = packet.getfieldval("load")
            comment_json = {
                "comment": comment.decode('utf-8')  # Decoding if the comment is encoded
            }
            print(color.GREEN + f"Comment found in packet {packet_number}:\n" + color.END + f"{comment_json}\n")
        else:
            print(color.RED + f"No comment found in packet {packet_number}\n" + color.END)
    else:
        print("Packet number out of range")
        exit(1)


def main():
    parser = argparse.ArgumentParser(description='Tool for adding and reading comments in PCAPNG files')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a comment in the specified packet and generate a new pcapng file with the comment inserted into that packet')
    add_parser.add_argument('input_pcapng_file', type=str, help='Input PCAPNG file')
    add_parser.add_argument('output_pcapng_file', type=str, help='Output PCAPNG file')
    add_parser.add_argument('comment', type=str, help='Comment to add')
    add_parser.add_argument('packet_number', type=int, help='Packet number')

    read_parser = subparsers.add_parser('read', help='Read the comment contained in the selected packet from the specified pcapng file')
    read_parser.add_argument('input_pcapng_file', type=str, help='Input PCAPNG file')
    read_parser.add_argument('packet_number', type=int, help='Packet number')

    args = parser.parse_args()

    if args.command == 'add':
        add_comment_to_packet(args.input_pcapng_file, args.output_pcapng_file, args.comment, args.packet_number)
    elif args.command == 'read':
        read_comment_from_packet(args.input_pcapng_file, args.packet_number)
    elif args.command == '-h' or args.command == '--help':
        help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
