import unittest
from tools import get_full_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_full_name('mehran', 'sadeghi')
        self.assertEqual(formatted_name, 'Mehran Sadeghi')
    
    def test_first_middle_last_name(self):
        formatted_name = get_full_name('amir', 'rostami', 'hossein')
        self.assertEqual(formatted_name, 'Amir Hossein Rostami')


# if __name__ == "__main__":
#     unittest.main()

mehran = ['mehran', 'ahmad', 'mohsen']
for moh in mehran:
    if 'moh' in moh:
        print('mohiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        print('just merge :)')
        print('my name is master')
        print('im the extra line of master :))))))))')