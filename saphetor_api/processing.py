import pandas as pd
import numpy as np
from .header import HEADER

class Processing:

    def read_vcf_file(self, filename, columns, id=None):

        vcf_df=pd.read_csv(filename,
                            sep='\t',
                            comment="#", 
                            names=columns, 
                            index_col=False)
        
        if id: vcf_df = vcf_df[vcf_df['ID'] == id]  
            

        vcf_list = vcf_df.to_dict(orient='records') 

        return vcf_list

    def add_json_to_file(self, filename, json_obj , columns  ):
        json_df = pd.DataFrame(json_obj, columns=columns)
        json_df["QUAL"]=0.0
        json_df["FILTER"]="PASS"
        json_df["INFO"]="." 
        json_df["FORMAT"]="."
        json_df.to_csv(filename, 
                        mode='a',
                        header=False , 
                        index=False, 
                        sep='\t')

    def update_data_in_file(self, id, filename, json_obj , columns):
        vcf_df=pd.read_csv(filename, sep='\t',comment="#", names=columns, index_col=False)
        df_to_update = vcf_df[vcf_df['ID'] == id]

        if df_to_update.empty:
            return "EMPTY_UPDATE"

        vcf_df['ID'] = np.where(vcf_df['ID'] == id, json_obj["ID"], vcf_df['ID'])
        vcf_df["CHROM"] = np.where(vcf_df['ID'] == json_obj["ID"], json_obj["CHROM"], vcf_df['CHROM'])
        vcf_df["POS"] = np.where(vcf_df['ID'] == json_obj["ID"], json_obj["POS"], vcf_df['POS'])
        vcf_df["REF"] = np.where(vcf_df['ID'] == json_obj["ID"], json_obj["REF"], vcf_df['REF'])
        vcf_df["ALT"] = np.where(vcf_df['ID'] == json_obj["ID"], json_obj["ALT"], vcf_df['ALT'])

        with open(filename, 'w') as vcf:
            vcf.write(HEADER)
            vcf_df.to_csv(vcf, mode='a' , index=False, sep='\t') 

        return "SUCCESS_UPDATE"

    def delete_data_from_file(self, id, filename , columns):

        vcf_df=pd.read_csv(filename, sep='\t',comment="#", names=columns, index_col=False)
        df_to_delete = vcf_df[vcf_df['ID'] == id]
        
        if df_to_delete.empty:
            return "EMPTY_DELETION"
        vcf_df.drop(vcf_df[vcf_df['ID'] == id].index,axis=0,inplace=True)
    
        with open(filename, 'w') as vcf:
            vcf.write(HEADER)
            vcf_df.to_csv(vcf, mode='a' , index=False, sep='\t')         
        
        return "SUCCESS_DELETION"

       



