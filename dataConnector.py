from databricks import sql

    
def connect_to_databricks (serverName=None, httpPath=None, acessToken=None):
        connection  = sql.connect(
             server_hostname=serverName,
             http_path=httpPath,
            access_token=acessToken)
        global cursor
        cursor = connection.cursor()
        #cursor.execute("select * from db_sid_output.t_sid_digital_output_predicao_pn where proc_date = '2021-12-09' and ( sku_gm_id = '115000')")
        

def query_databricks (query=None):
         cursor.execute(query)
         result = cursor.fetchall()
         for row in result:
             print(row)
         return result

         
def disconnect_databricks ():
         cursor.close()