from qr import encoding
from resources.version_capacities import version_capacities

class QRCode:
    def __init__(self, data):
        self.data = data
        self.error_correction_level = "M"
        self.data_length = len(self.data.encode("utf-8"))
        self.version = self.get_version()
        self.size = ((self.version-1)*4)+21
        self.matrix = self.initialize_matrix()

    def initialize_matrix(self):
        matrix = []
        for r in range(self.size):
            row = []
            for c in range(self.size):
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
        print(data_string)


        
        print(len(data_string))




    