import boto3
#s3_ob=boto3.resource('s3',aws_access_key_id="AKIAUWLPSPPS7GA452VY",aws_secret_access_key="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")
aws_msg_con=boto3.session.Session(profile_name="default")
s3_ob=boto3.resource('s3')
for each_b in s3_ob.buckets.all():
    print (each_b.name)
