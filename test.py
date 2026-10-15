import unittest
from evaluation import diagnose

class EvaluationTests(unittest.TestCase):
    def test_evaluation(self):
        patient_ex_m = {
            'radius_mean': 27,
            'texture_mean': 38,
            'perimeter_mean': 188
        }

        patient_ex_b = {
            'radius_mean': 7,
            'texture_mean': 9.8,
            'perimeter_mean': 50.5
        }

        patient_ex_eq = {
            'radius_mean': 12.5,
            'texture_mean': 16.2,
            'perimeter_mean': 106.5
        } 

        self.assertEqual(diagnose(patient_ex_m, patient_ex_m.keys(), 1), 'M')
        self.assertEqual(diagnose(patient_ex_b, patient_ex_b.keys(), 2), 'B')
        self.assertEqual(diagnose(patient_ex_eq, patient_ex_b.keys(), 3), 'B')

if __name__ == "__main__":
    unittest.main()