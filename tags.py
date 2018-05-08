import boto3
import pytz
from datetime import datetime
from pytz.reference import Eastern


def utc_time(eastern_time):
    utc_dt = datetime(2002, 10, 27, int(eastern_time), 0, 0, tzinfo=Eastern)
    loc_dt = utc_dt.astimezone(pytz.timezone('UTC'))
    print loc_dt.strftime('%H%M')

ec2 = boto3.resource('ec2')
ec2instance = ec2.Instance('i-0eca61c23f19dd5e8')


for tags in ec2instance.tags:
    if tags["Key"] == 'Schedule':
        schedule_times = tags["Value"]

start_time = schedule_times.split(':')[0]
end_time = schedule_times.split(':')[1]

utc_start_time = utc_time(start_time)
utc_end_time = utc_time(end_time)

ec2instance.create_tags(
          DryRun=False,
          Tags=[
              {
                  'Key': 'RunSchedule',
                  'Value': start_time
              },
          ]
      )





