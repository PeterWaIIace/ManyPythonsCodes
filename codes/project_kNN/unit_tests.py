import unittest
import kNN
import numpy as np

class TestkNN(unittest.TestCase):

    def test_euclideanDistance(self):
        data1 = np.random.rand(20)*100
        data2 = np.random.rand(20)*100
        self.assertGreaterEqual(kNN.euclideanDistance(data1, data2, len(data1)), 0)
        self.assertGreaterEqual(kNN.euclideanDistance(-data1, -data2, len(data1)), 0)
        self.assertGreaterEqual(kNN.euclideanDistance(data1, -data2, len(data1)), 0)
        self.assertGreaterEqual(kNN.euclideanDistance(-data1, data2, len(data1)), 0)
        self.assertGreaterEqual(kNN.euclideanDistance(data1, data2, 1), 0)
        self.assertGreaterEqual(kNN.euclideanDistance(data1, data2, 0), 0)
        self.assertRaises(IndexError, lambda: kNN.euclideanDistance(data1, data2, len(data1)+1))

    def test_getAccuracy(self):
        data1 = np.random.rand(20)
        data2 = []
        for d in data1:
            data2.append([d])

        self.assertEqual(100, kNN.getAccuracy(data2, data1))

        for i in range(0, int(len(data2)/2)):
            data2[2*i][0] = -data2[2*i][0]

        self.assertEqual(50, kNN.getAccuracy(data2, data1))

if __name__ == '__main__':
    unittest.main()