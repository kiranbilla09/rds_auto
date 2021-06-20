import boto3
client = boto3.client('rds')
response = client.describe_db_instances()
for i in response['DBInstances']:
   db_name = i['DBName']
   db_instance_name = i['DBInstanceIdentifier']
   db_type = i['DBInstanceClass']
   db_storage = i['AllocatedStorage']
   db_engine = i['Engine']
   print (db_name,db_instance_name,db_type,db_storage,db_engine)
