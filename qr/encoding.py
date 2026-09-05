from resources.data_bit_requirements import data_bits_requirement

def add_character_count_bits(data_string, version, data_length):
    if version <= 9:
        character_count = format(data_length, "08b")
    else:
        character_count = format(data_length, "016b")
    data_string += str(character_count)
    return data_string

def encode(data, data_string):
    encoded_data = data.encode("utf-8")
    for byte in encoded_data:
        data_string += str(format(byte, "08b"))
    return data_string

def reach_requirement(data_string, version):
    bit_requirement = data_bits_requirement[version]

    difference = bit_requirement - len(data_string)
    if difference <= 4:
        while 0 < difference <= 4:
            data_string += "0"
            difference -= 1
    else:
        data_string += "0000"
        if len(data_string) % 8 != 0:
            num_zeroes = 8 - (len(data_string) % 8)
            for _ in range(num_zeroes):
                data_string += "0"
    difference = bit_requirement - len(data_string)
    if difference > 0:
        num_bytes = difference // 8
        pad_bytes = ["11101100", "00010001"]
        index = 0
        for _ in range(num_bytes):
            data_string += pad_bytes[index]
            if index == 0:
                index = 1
            else:
                index = 0
    return data_string


        
    
    