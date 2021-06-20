import boto3
import botocore
import sys
import random
import time
# Create DB snapshot
rds_client = boto3.client(service_name="rds", region_name="symphony",
                              endpoint_url="https://%s/api/v2/aws/rds" % CLUSTER_IP,
                              verify=False,
                              aws_access_key_id=AWS_ACCESS,
                              aws_secret_access_key=AWS_SECRET)
run_index = '%03x' % random.randrange(2**12)
db_instance_name = 'test_instance_db_%s' % run_index
db_snapshot_name = 'test_snapshot_db_%s' % run_index
create_db_snapshot_response = rds_client.create_db_snapshot(
                                    DBInstanceIdentifier=db_instance_name,
                                    DBSnapshotIdentifier=db_snapshot_name)
# check Create DB instance returned successfully
if create_db_snapshot_response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Successfully created DB snapshot %s" % db_instance_name)
else:
    print("Couldn't create DB snapshot")

print("waiting for db snapshot %s to become ready" % db_instance_name)
number_of_retries = 20
snapshot_success = False
for i in xrange(number_of_retries):
    time.sleep(30)
    snp_status = rds_client.describe_db_snapshots(DBSnapshotIdentifier=db_snapshot_name)['DBSnapshots'][0]['Status']
    if snp_status == 'available':
        snapshot_success = True
        print("DB snapshot %s is ready" % db_snapshot_name)
        break
    else:
        print("DB snapshot %s is initializing. Attempt %s" % (db_snapshot_name, i))
assert snapshot_success, "DB failed %s to initialize" % db_snapshot_name
