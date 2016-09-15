"""Testing harness for Netflix project"""

from unittest import main, TestCase
from io import StringIO
from Netflix import predict_probe_data, netflix_solve


class TestNetflix(TestCase):

    """Test class for unit tests"""

    def test_predict_probe_data_1(self):
        """Test 1 for predict_probe_data()"""
        reader = StringIO('138:\n1735266\n1270280\n')
        writer = StringIO()
        predict_probe_data(reader, writer)
        self.assertEqual(writer.getvalue(), '138:\n3.3\n3.2\n')

    def test_predict_probe_data_2(self):
        """Test 2 for predict_probe_data()"""
        reader = StringIO('1380:\n804004\n2369086\n')
        writer = StringIO()
        predict_probe_data(reader, writer)
        self.assertEqual(writer.getvalue(), '1380:\n3.5\n3.4\n')

    def test_predict_probe_data_3(self):
        """Test 3 for predict_probe_data()"""
        reader = StringIO('13800:\n2232104\n802351\n')
        writer = StringIO()
        predict_probe_data(reader, writer)
        self.assertEqual(writer.getvalue(), '13800:\n3.5\n3.9\n')

    def test_netflix_solve_1(self):
        """Test 1 for netflix_solve()"""
        reader = StringIO('5051:\n1424647\n516192\n')
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), '5051:\n2.9\n4.1\nRMSE: 1.34\n')

    def test_netflix_solve_2(self):
        """Test 2 for netflix_solve()"""
        reader = StringIO('5052:\n222269\n1622303\n')
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), '5052:\n4.4\n3.5\nRMSE: 1.22\n')

    def test_netflix_solve_3(self):
        """Test 3 for netflix_solve()"""
        reader = StringIO('5054:\n525818\n551652\n')
        writer = StringIO()
        netflix_solve(reader, writer)
        self.assertEqual(writer.getvalue(), '5054:\n3.6\n3.7\nRMSE: 1.16\n')


if __name__ == "__main__":
    main()