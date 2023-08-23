# strings contain unicode, bytes are raw 8-bit values
# strings and bytes are not directly interchangeable

def main():
    b=bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s="This is a string"
    print(s)

    # We CANNOT concatenate bytes and strings just like b+s

    s2=b.decode('utf-8')
    print(s2)
    print(s+s2)

    b2 = s.encode('utf-8')
    print(b2)
    print(b+b2)

    b3 = s.encode('utf-32')
    print(b3)

if __name__=="__main__":
    main()
