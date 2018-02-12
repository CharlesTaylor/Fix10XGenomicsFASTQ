import sys

def make_fqcounter():
    x = -1
    def count():
        nonlocal x
        x = (x+1) & 3
        return x
    return count

def main():
    barcode_length = int(sys.argv[1])
    fqline = make_fqcounter()
    barcode = ""
    barqual = ""
    for line in sys.stdin:
        c = fqline()
        if c is 0:
            read_id = line[:-1].split(" ")[0]
        elif c is 1:
            read = line[barcode_length:-1]
            barcode = "BX:Z:"+line[:barcode_length]+"-1"
        elif c is 2:
            pass    #+
        elif c is 3:

            barqual = "QX:Z:"+line[:barcode_length]
            print(read_id.replace(" ","-"),barcode,barqual)
            print(read) 
            print("+")
            print(line[barcode_length:-1])

main()
