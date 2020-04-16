import unittest
import sys
import serial

# on which port should the tests be performed:
PORT = 'COM3'
BAUDRATE = 115200
#~ BAUDRATE=9600

if sys.version_info >= (3, 0):
    bytes_0to255 = bytes(range(256))
else:
    bytes_0to255 = ''.join([chr(x) for x in range(256)])


class TestHighLoad(unittest.TestCase):
    """Test sending and receiving large amount of data"""

    N = 16
    #~ N = 1

    def setUp(self):
        self.s = serial.serial_for_url(PORT, BAUDRATE, timeout=10)

    def tearDown(self):
        self.s.close()

    def test0_WriteReadLoopback(self):
        """Send big strings, write/read order."""
        for i in range(self.N):
            q = bytes_0to255
            self.s.write(q)
            self.assertEqual(self.s.read(len(q)), q)  # expected same which was written before
        self.assertEqual(self.s.inWaiting(), 0)  # expected empty buffer after all sent chars are read

    def test1_WriteWriteReadLoopback(self):
        """Send big strings, multiple write one read."""
        q = bytes_0to255
        for i in range(self.N):
            self.s.write(q)
        read = self.s.read(len(q) * self.N)
        self.assertEqual(read, q * self.N, "expected what was written before. got {} bytes, expected {}".format(len(read), self.N * len(q)))
        self.assertEqual(self.s.inWaiting(), 0)  # "expected empty buffer after all sent chars are read")


if __name__ == '__main__':
    import sys
    #sys.stdout.write(__doc__)
    if len(sys.argv) > 1:
        PORT = sys.argv[1]
    sys.stdout.write("Testing port: {!r}\n".format(PORT))
    sys.argv[1:] = ['-v']
    # When this module is executed from the command-line, it runs all its tests
    unittest.main()