# orphaned_snapshot

Easy script to find EBS snapshots which has not parent volume any more. 

AWS CLI with AWS credential.
Python runtime.

How to use:
% python ./orphaned_snapshots.py

Sample output:

1 snap-07722fa9e9974c95f is snapshot for vol-00d035909c8b9715c taken on 2022-05-25. vol-00d035909c8b9715c was recovered from  on 2022-03-25
2 snap-02e2fcee42057f27f is snapshot for vol-0b3d12805ac0a3750 taken on 2019-08-23. vol-0b3d12805ac0a3750 was recovered from  on 2017-03-13
3 snap-054fd31234aaa2107 is snapshot for vol-0d8d67703274f09f6 taken on 2017-07-10. Missing parent volume, please check with your admin if this is cost efficient.
4 snap-05048b5bd1464a398 is snapshot for vol-01eb49b06545155a5 taken on 2017-09-12. Missing parent volume, please check with your admin if this is cost efficient.
5 snap-012177594985fb230 is snapshot for vol-09d22e8a653e24135 taken on 2022-02-23. vol-09d22e8a653e24135 was recovered from snap-054fd31234aaa2107 on 2022-02-23

Script lists snapshots in the AWS account (self), and find the parent volume id respectively. Then, chekcs if the volume of the id exists in the account or not. As far as the volume looks exist, the script shows that the volume was created newly before (like line 1 or 2) or the volume was created from snapshot before (line 5). If the script can not find the volume existance (like like 3 or 4), maybe it is deletion candidate if the snapshot is no more needed.

