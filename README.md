# orphaned_snapshot

Easy script to find EBS snapshots which does not have parent volume any more. 

Requirements:
- AWS CLI 
- AWS credential.
- Python runtime.

How to use:
```
% python ./orphaned_snapshots.py
```

Sample output:

```
1 snap-0405eba2e66b8f59d is snapshot for vol-0cce165d7aca3bbc0 taken on 2017-03-13 standard tier. Missing parent volume, please check with your admin if this is cost efficient or candidate for archiving., my first snapshot from storage gw
2 snap-07722fa9e9974c95f is snapshot for vol-00d035909c8b9715c taken on 2022-05-25 standard tier. vol-00d035909c8b9715c was recovered from  on 2022-03-25, snapshot3
3 snap-02e2fcee42057f27f is snapshot for vol-0b3d12805ac0a3750 taken on 2019-08-23 standard tier. vol-0b3d12805ac0a3750 was recovered from  on 2017-03-13, 
4 snap-0c900bd54ccc61049 is snapshot for vol-0e31ac5c9c9265826 taken on 2018-06-16 archive tier. Missing parent volume, but is on archive tier., 
5 snap-054fd31234aaa2107 is snapshot for vol-0d8d67703274f09f6 taken on 2017-07-10 standard tier. Missing parent volume, please check with your admin if this is cost efficient or candidate for archiving., 
6 snap-744b7efb is snapshot for vol-0198baeb843d5d85e taken on 2017-03-30 standard tier. Missing parent volume, please check with your admin if this is cost efficient or candidate for archiving., Created by CreateImage(i-05b00685b550de919) for ami-d70722b0 from vol-0198baeb843d5d85e
7 snap-0869a66710dd5fae2 is snapshot for vol-09d22e8a653e24135 taken on 2023-03-26 standard tier. vol-09d22e8a653e24135 was recovered from snap-054fd31234aaa2107 on 2022-02-23, This snapshot is created by the AWS Backup service.
8 snap-012177594985fb230 is snapshot for vol-09d22e8a653e24135 taken on 2022-02-23 standard tier. vol-09d22e8a653e24135 was recovered from snap-054fd31234aaa2107 on 2022-02-23, manual snapshot EC2 console

```

This script lists snapshots in the AWS account (self), and find the parent volume id respectively. Then, chekcs if the volume of the id exists within the AWS account or not. As far as the parent volume looks exist, the script shows that the volume was created newly before (like line 2 or 3) or the volume was created from snapshot before (like line 7 or 8). If the script can not find the volume existance (like line 1 or 5), maybe it would be deletion candidate or archive candidate if the snapshot is no more needed. AMI related snapshot is shown like line 6 and snapshot which has been already archived is shown like line 4. Line 7 shows the snapshot is created by AWS Backup where the snapshot can not be deleted with EC2 API / EC2 Management Console, but can be deleted on AWS Backup.

Please be careful before actually deleting snapshot even if the parent volume is missing. It might be used as backup. Please check your admin if it is cost effective or not.
