import unittest
import Lab_02


class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        self.list = []

    def test_add_student(self):
        student = {
            "name": "Bob",
            "phone": "0631234567",
            "email": "damsbob@gmail.com",
            "group": "kb-242"}

        Lab_02.add_student(self.list, "Bob", "0631234567",
                           "damsbob@gmail.com", "kb-242")
        assert len(self.list) == 1
        assert self.list[0] == student

    def test_delete_student(self):
        self.list = [{"name": "Bob", "phone": "0631234567",
                      "email": "damsbob@gmail.com", "group": "kb-242"}]
        result = Lab_02.delete_student(self.list, "Bob")
        assert result == True
        assert len(self.list) == 0


if __name__ == '__main__':
    unittest.main()
