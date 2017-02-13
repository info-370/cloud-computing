import boto3 as aws
from botocore.handlers import disable_signing
import csv
import sys

# Check for python version to use correct library
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

def get_census_data(city):
    """
    Gets a pandas data frame for `city` with cencus tract
    data
    """
    filename = city + "_race.csv"
    s3 = aws.resource('s3')

    # Making sure you dont need credentials to make a request. Don't
    # try this at home
    s3.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)
    obj = s3.Object(bucket_name="370-lab-05", key=filename)
    res = obj.get()
    raw_data = res['Body'].read().decode('UTF-8')
    data = StringIO(raw_data)

    reader = csv.DictReader(data)

    result = {}
    for row in reader:
        for column, value in row.items():
            result.setdefault(column, []).append(value)
    return result

def get_avg_pop(city):
    """
    Given a city name, gets the average population of a census
    tract in that city (total population / number of census tracts)
    """
    df = get_census_data(city) # Makes a call to get the city data from S3

    # Calculate and return the average census tract population
    num_tracts = 0
    total_pop = 0
    for pop in df["pop"]:
        total_pop += int(pop);
        num_tracts += 1
    return total_pop / num_tracts
