from qr import encoding
from resources import EC_info
from resources.version_capacities import version_capacities

class QRCode:
    def __init__(self, data):
        self.data = data
        self.error_correction_level = "M"
        self.data_length = len(self.data.encode("utf-8"))
        self.version = self.get_version()
        self.size = ((self.version-1)*4)+21
        self.matrix = self.initialize_matrix()
        self.data_codewords = []
        self.group1_data = []
        self.group2_data = []

    def initialize_matrix(self):
        matrix = []
        for _ in range(self.size):
            row = []
            for _ in range(self.size):
                row.append(None)
            matrix.append(row)
        return matrix
                
    def get_version(self):
        for version in version_capacities:
            capacity = version_capacities[version]
            if self.data_length <= capacity:
                return version
        raise ValueError("Data is too large for a QR code")

    def encode_data(self):
        data_string = "0100"
        
        data_string = encoding.add_character_count_bits(data_string, self.version, self.data_length)

        data_string = encoding.encode(self.data, data_string)
        data_string = encoding.reach_requirement(data_string, self.version)

        self.data_codewords = encoding.get_data_codewords(data_string)

    def structure_data(self):
        g1_blocks = EC_info.group1_blocks[self.version]
        g2_blocks = EC_info.group2_blocks[self.version]
        data_per_g1_block = EC_info.data_group1_blocks[self.version]
        data_per_g2_block = EC_info.data_group2_blocks[self.version]

        index = 0
        for _ in range(g1_blocks):
            block = []
            for _ in range(data_per_g1_block):
                block.append(self.data_codewords[index])
                index += 1
            self.group1_data.append(block)
        for _ in range(g2_blocks):
            block = []
            for _ in range(data_per_g2_block):
                block.append(self.data_codewords[index])
                index += 1
            self.group2_data.append(block)



    