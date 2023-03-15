#Copyright 2015 Amazon Web Services, Inc. or its affiliates. All rights reserved.

import boto3
import sys
import botocore

ec2 = boto3.client('ec2')

snapshotids=[
   'snap-07722fa9e9974c95f',
   'snap-02e2fcee42057f27f',
   'snap-05048b5bd1464a398', 
   'snap-012177594985fb230',
   'snap-054fd31234aaa2107'
   ]

awsids=[
   'self'
]

# response = ec2.describe_snapshots(SnapshotIds=snapshotids)
response = ec2.describe_snapshots(OwnerIds=awsids)
snapshots = response["Snapshots"]

count = 1

for snapshot in snapshots:
   snapshot_id = snapshot["SnapshotId"]
   volume_id = snapshot["VolumeId"]
   taken_on = snapshot["StartTime"].date()
   ids=[volume_id]
   try :
      response = ec2.describe_volumes(VolumeIds=ids)
      volumes = response["Volumes"]
      for volume in volumes:
         vid = volume["VolumeId"]
         from_sid = volume["SnapshotId"]
         restored_date = volume["CreateTime"].date()
      description = vid + " was recovered from " + from_sid + " on " + str(restored_date) 
   except:
      description = "Missing parent volume, please check with your admin if this is cost efficient."
   finally:
      print('{} {} is snapshot for {} taken on {}. {}'.format(count, snapshot_id, volume_id, taken_on, description))
      count += 1
