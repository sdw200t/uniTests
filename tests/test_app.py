import unittest
from app import add_new_doc, get_doc_owner_name, delete_doc


class TestFunction(unittest.TestCase):
    # Запуск перед каждым тестом
    def setUp(self) -> None:
        return super().setUp()

    # Запуск после каждого теста
    def tearDown(self) -> None:
        return super().tearDown()

    def test_add_new_doc(self):
        result = add_new_doc('12/1', 'INN', 'Ivanov', '125')
        self.assertEqual(result, True)

    def test_get_doc_owner_name(self):
        result = get_doc_owner_name('10006')
        self.assertEqual(result, 'Аристарх Павлов')

    def test_delete_doc(self):
        result = delete_doc('10006')
        self.assertEqual(result, True)
