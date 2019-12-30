import unittest
from circle import Circle

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(3.5,"blue")
        self.circle2 = Circle()
    
    def test_circleConsturctor(self):
        self.assertEqual(self.circle1.radius,3.5)
        self.assertEqual(self.circle1.color,"blue")

        self.assertEqual(self.circle2.radius,1.0)
        self.assertEqual(self.circle2.color,"red")
    
    def test_circleSettersAndGetters(self):
        self.circle1.setRadius(4.0)
        self.circle1.setColor("green")

        self.assertEqual(self.circle1.getRadius(),4.0)
        self.assertEqual(self.circle1.getColor(),"green")
    
if __name__ == "__main__":
    unittest.main()