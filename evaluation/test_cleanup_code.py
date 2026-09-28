import importlib.util
import unittest
from pathlib import Path


def load_utils():
    path = Path(__file__).resolve().parent / "utils.py"
    spec = importlib.util.spec_from_file_location("codegeex_utils", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CleanupCodeTest(unittest.TestCase):
    def test_a_solution_without_assert_keeps_its_last_character(self):
        utils = load_utils()
        code = "def add(a, b):\n    return a + b"
        self.assertEqual(utils.cleanup_code(code, "mbpp", "python"), code)

        with_assert = "def add(a, b):\n    return a + b\nassert add(1, 2) == 3"
        self.assertEqual(
            utils.cleanup_code(with_assert, "mbpp", "python"),
            "def add(a, b):\n    return a + b",
        )


if __name__ == "__main__":
    unittest.main()
