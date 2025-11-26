import unittest
from main import Student, Teacher, AdminStaff


class TestStudent(unittest.TestCase):
    def test_gpa_range(self):
        s = Student("Алиса", 19, "IS-23", 3.7)
        self.assertTrue(0 <= s.gpa <= 4.0)

    def test_student_display(self):
        s = Student("Алиса", 19, "IS-23", 3.7)
        self.assertIn("Студент", s.display_info())


class TestTeacher(unittest.TestCase):
    def test_teacher_attributes(self):
        t = Teacher("Игорь", 40, "Физика", 15)
        self.assertEqual(t.subject, "Физика")
        self.assertEqual(t.experience, 15)


class TestAdminStaff(unittest.TestCase):
    def test_admin_display(self):
        a = AdminStaff("Мария", 30, "Секретарь", "Отдел кадров")
        self.assertIn("Админ.персонал", a.display_info())


if __name__ == "__main__":
    unittest.main()
