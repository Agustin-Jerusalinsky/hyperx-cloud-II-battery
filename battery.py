import hid


def get_battery_level(h=None):

    vid = 0x0951  # Hyperx vendor ID

    pid = 0x1718  # Hyperx Cloud II product ID
    if not h:
        h = hid.device()
        h.open(vid, pid)  # TREZOR VendorID/ProductID

    report = h.get_input_report(6,62) #ask for report so it doesnt return broken pipe error

    ## setter that trigger the battery level response
    setter = "060002009a0000684a8e0a000000bb0200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

    def hex_to_array(hex_string):
        return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]    

    # send the setter
    h.write(hex_to_array(setter))

    # read the response
    read = h.read(255)

    #battery is the 7th byte
    return h,read[7]


if __name__ == "__main__":
    print(get_battery_level()[1])

