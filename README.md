# RobotFramework-Library-Databricks

Library in RobotFramework for connections in databricks using SQL 



## How to use the library
git clone https://github.com/Rommelfoxx/RobotFramework-Library-Databricks.git

instantiate the library in project settings 

..\Libraries\Databricks\dataConnector.py 


## Keywords 

Keywords for connection and query in databricks 

### connect_to_databricks 
Keyword for connect in databricks 

#### arguments 

serverName - name or server address databricks
httpPath   - Databricks compute resources URL
acessToken  - Token generate in databricks 

### query_databricks
Query for consulting databricks 

#### arguments 
query - query SQL for consulting 

###disconnect_databricks 
Keyword for close connection databricks 



