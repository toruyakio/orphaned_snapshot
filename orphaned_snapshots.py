#Copyright 2015 Amazon Web Services, Inc. or its affiliates. All rights reserved.

import boto3
import sys
import botocore

ec2 = boto3.client('ec2')


# If you would like to work with specific Snapshot IDs which you are already aware with.

snapshotids=[
   'snap-07722fa9e9974c95f',
   'snap-02e2fcee42057f27f',
   'snap-05048b5bd1464a398', 
   'snap-012177594985fb230',
   'snap-054fd31234aaa2107',
   'snap-744b7efb',
   'snap-0405eba2e66b8f59d'
   ]

awsids=[
   'self'
]


# Example in case that you would like to work with AMI related Snapshot IDs.

filters=[
   {
      'Name': 'description',
      'Values': [
         '*ami-*'
      ]
   }
]

# response = ec2.describe_snapshots(SnapshotIds=snapshotids)
# response = ec2.describe_snapshots(Filters=filters, OwnerIds=awsids)
response = ec2.describe_snapshots(OwnerIds=awsids)
snapshots = response["Snapshots"]

count = 1

for snapshot in snapshots:
   snapshot_id = snapshot["SnapshotId"]
   volume_id = snapshot["VolumeId"]
   taken_on = snapshot["StartTime"].date()
   description = snapshot["Description"]
   ids=[volume_id]
   try :
      response = ec2.describe_volumes(VolumeIds=ids)
      volumes = response["Volumes"]
      for volume in volumes:
         vid = volume["VolumeId"]
         from_sid = volume["SnapshotId"]
         restored_date = volume["CreateTime"].date()
      guidance = vid + " was recovered from " + from_sid + " on " + str(restored_date) 
   except:
      guidance = "Missing parent volume, please check with your admin if this is cost efficient."
   finally:
      print('{} {} is snapshot for {} taken on {}. {}, {}'.format(count, snapshot_id, volume_id, taken_on, guidance, description))
      count += 1
