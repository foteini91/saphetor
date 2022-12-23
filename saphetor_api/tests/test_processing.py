from django.test import TestCase
from saphetor_api import processing 
from unittest.mock import MagicMock
import pandas as pd


class TestProcessing(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass
    
    def test1_read_vcf_file(self):
        filename = "/home/foteinip/saphetor/saphetor_api/tests/test_file"
        columns = ["CHROM", "POS", "ID", "REF","ALT"]
        mock_pd= MagicMock()
        mock_pd.read_csv.return_value = pd.DataFrame([{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}])
        
        processing.pd=mock_pd

        p_obj = processing.Processing()
        response = p_obj.read_vcf_file(filename, columns )
        
        expected_response = [{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}]

        self.assertCountEqual(response ,expected_response)

    def test2_read_vcf_file_by_id(self):
        filename = "/home/foteinip/saphetor/saphetor_api/tests/test_file"
        columns = ["CHROM", "POS", "ID", "REF","ALT"]
        id = 'rs1570356'
        mock_pd= MagicMock()
        mock_pd.read_csv.return_value = pd.DataFrame([{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}])
        
        processing.pd=mock_pd

        p_obj = processing.Processing()
        response = p_obj.read_vcf_file(filename, columns,id )
        expected_response = [{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}] 

        self.assertCountEqual(response ,expected_response)

    def test3_update_data_in_file(self):

        filename = "/home/foteinip/saphetor/saphetor_api/tests/test_file"
        columns = ["CHROM", "POS", "ID", "REF","ALT","QUAL","FILTER","INFO","FORMAT"]
        json_obj={"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G","ID": "rs1"}
        id = 'rs1570356'
        mock_pd= MagicMock()
        mock_pd.read_csv.return_value = pd.DataFrame([{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}])
        
        processing.pd=mock_pd
        p_obj = processing.Processing()
        response = p_obj.update_data_in_file(id, filename, json_obj , columns)
        self.assertEqual(response ,"SUCCESS_UPDATE")

    def test4_update_data_in_file_failure(self):

        filename = "/home/foteinip/saphetor/saphetor_api/tests/test_file"
        columns = ["CHROM", "POS", "ID", "REF","ALT","QUAL","FILTER","INFO","FORMAT"]
        json_obj={"CHROM": "chr1", "POS": 1000, "ALT": "A", "REF": "G","ID": "rs1"}
        id = 'rs111111'

        mock_pd= MagicMock()
        mock_pd.read_csv.return_value = pd.DataFrame([{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}])
        
        processing.pd=mock_pd

        p_obj = processing.Processing()
        response = p_obj.update_data_in_file(id, filename, json_obj , columns)
        self.assertEqual(response ,"EMPTY_UPDATE")

    def test5_delete_data_from_file(self):
        
        filename = "/home/foteinip/saphetor/saphetor_api/tests/test_file"
        columns = ["CHROM", "POS", "ID", "REF","ALT","QUAL","FILTER","INFO","FORMAT"]
        id = 'rs1570356'
        mock_pd= MagicMock()
        mock_pd.read_csv.return_value = pd.DataFrame([{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}])
        
        processing.pd=mock_pd

        p_obj = processing.Processing()
        response = p_obj.delete_data_from_file(id, filename , columns)
        self.assertEqual(response ,"SUCCESS_DELETION")

    def test5_delete_data_from_file_fail(self):
        
        filename = "/home/foteinip/saphetor/saphetor_api/tests/test_file"
        columns = ["CHROM", "POS", "ID", "REF","ALT","QUAL","FILTER","INFO","FORMAT"]
        id = 'rs123____'
        mock_pd= MagicMock()
        mock_pd.read_csv.return_value = pd.DataFrame([{'CHROM': 'chr1', 'POS': 42037875, 'ID': 'rs1570356', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 42037898, 'ID': 'rs4511101', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1000, 'ID': 'rs1', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1268987, 'ID': 'rs149341566', 'REF': 'G', 'ALT': 'A'}, {'CHROM': 'chr1', 'POS': 1269554, 'ID': 'rs307377', 'REF': 'T', 'ALT': 'C'}, {'CHROM': 'chr1', 'POS': 1269888, 'ID': 'rs139522421', 'REF': 'C', 'ALT': 'A'}])
        
        processing.pd=mock_pd

        p_obj = processing.Processing()
        response = p_obj.delete_data_from_file(id, filename , columns)
        self.assertEqual(response ,"EMPTY_DELETION")






    
