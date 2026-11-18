import unittest
from main import infer_type, summarize_lines

class SchemaDriftTests(unittest.TestCase):
    def test_boolean_is_not_integer(self):
        self.assertEqual(infer_type(True),"boolean")
    def test_reports_missing_and_type_change(self):
        result=summarize_lines(['{"id":1,"name":"A"}','{"id":"2"}'])
        self.assertEqual(result["fields"]["name"]["missing"],1)
        self.assertEqual(result["fields"]["id"]["types"],["integer","string"])

if __name__=="__main__": unittest.main()
