# import required modules (please install globaly or using virtualenv)
import requests
from datetime import datetime
import json

# peeringdb url query
URL = "https://www.peeringdb.com/api/ix?country__in=ID&limit=250&depth=1"

# limit output sort
LIMIT = 5

# try request
try:
    # request
    r = requests.get(url=URL)

    # response as json
    responseJson = r.json()

    # check repsonse has data key
    if 'data' in responseJson:
        # store data in vars
        data = responseJson['data']

        # check data len > 0
        if len(data) > 1:
            # sort data by 'net_count' key using sorted and lambda
            sortedData = sorted(
                data, key=lambda x: x['net_count'], reverse=True)
            # limit data a.k.a slice
            slice = slice(LIMIT)

            # sliced data result
            slicedData = sortedData[slice]

            # array of final results
            results = []

            # loop and store ixp data in 'results'
            for ixp in slicedData:
                # only get 'name' and 'net_count'
                ixpData = {'name': ixp['name'],
                           'net_count': ixp['net_count']}

                # append to 'results'
                results.append(ixpData)

            # format file name DD_MM_YYYY.json
            fileName = datetime.today().strftime('%d_%m_%Y') + '.json'

            # write to json file in 'data' folder
            with open('data/' + fileName, 'w') as outfile:
                json.dump(results, outfile)

            # TODO:
            # Please list todo next
            ##################################
            ##################################
            ##################################
            ##################################

        else:
            SystemExit('No data provided from peeringdb query (data len 0)')
    else:
        SystemExit('No data provided from peeringdb query (no key data)')
except requests.exceptions.HTTPError as err:
    # raise request err
    raise SystemExit(err)
