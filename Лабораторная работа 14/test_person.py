import unittest
from main import Student, Teacher, AdminStaff


class TestStudent(unittest.TestCase):
    def test_gpa_range(self):
        s = Student("Алиса", 19, "IS-23", 3.7)
        self.assertTrue(0 <= s.gpa <= 4.0)


class TestTeacher(unittest.TestCase):
    def test_experience(self):
        t = Teacher("Пётр", 40, "Математика", 15)
        self.assertEqual(t.experience, 15)


class TestAdminStaff(unittest.TestCase):
    def test_position(self):
        a = AdminStaff("Ирина", 35, "HR-менеджер", "Отдел кадров")
        self.assertEqual(a.position, "HR-менеджер")


if __name__ == "__main__":
    unittest.main()
