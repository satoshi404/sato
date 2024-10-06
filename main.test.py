import unittest
from main import compiler_mode, program_to_op, FUNC

class TestCompilerMode(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
def test_function_with_no_arguments(self):
    # Arrange
    program = "var a = 3 out a"

    # Act
    op, value, pos = program_to_op(program)

    # Assert
    self.assertEqual(op, FUNC)
    self.assertEqual(value, "no_args")
    self.assertEqual(pos, 0)
    self.assertEqual(len(stack), 0)

    def test_function_with_no_arguments(self):
        # Arrange
        program = "var a = 8 out a"
    
        # Act
        op, value, pos = program_to_op(program)
    
        # Assert
        self.assertEqual(op, FUNC)
        self.assertEqual(value, "no_args")
        self.assertEqual(pos, 0)
        self.assertEqual(len(stack), 0)
        self.assertIn("a", variables)
        self.assertEqual(variables["a"], 8)