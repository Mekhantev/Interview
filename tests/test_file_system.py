import random
import string
from unittest import TestCase
from oop.file_system import *


class TestFile(TestCase):
    def test_size(self):
        content = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 20)))
        f = File('file_name', content, Directory('directory_name'))
        self.assertEqual(f.size, len(content))


class TestDirectory(TestCase):
    def test_size(self):
        directory = Directory('directory_name')
        content = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 20)))
        directory.add_entry(File('file_name', content, directory))
        self.assertEqual(directory.size, len(content))

    def test_count_entries(self):
        directory = Directory('directory_name')
        content = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 20)))
        directory.add_entry(File('file_name', content, directory))
        inner_dir = Directory('inner_dir', directory)
        for i in range(5):
            inner_dir.add_entry(File('file'.join(str(i)), '1', inner_dir))
        directory.add_entry(inner_dir)
        self.assertEqual(directory.count_entries(), 7)

    def test_add_entry(self):
        directory = Directory('directory_name')
        content = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 20)))
        file = File('file_name', content, directory)
        directory.add_entry(file)
        self.assertEqual(file, directory.entries[0])
        self.assertRaises(EntryAlreadyExistsError, directory.add_entry, file)

    def test_remove_entry(self):
        directory = Directory('directory_name')
        content = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 20)))
        file = File('file_name', content, directory)
        directory.add_entry(file)
        directory.remove_entry(file)
        self.assertEqual(0, directory.count_entries())
        directory.remove_entry(file)
        self.assertEqual(0, directory.count_entries())


class TestEntry(TestCase):
    def test_full_path(self):
        directory_name = 'directory_name'
        file_name = 'file_name'
        directory = Directory(directory_name)
        content = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(10, 20)))
        directory.add_entry(File(file_name, content, directory))
        self.assertEqual(directory.entries[0].full_path, os.path.join(directory_name, file_name))