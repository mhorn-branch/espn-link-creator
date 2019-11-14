import csv, io
from django.shortcuts import render
from django.contrib import messages
from espn.models import Link
from django.conf import settings
import requests
import json


def link_upload(request):
    template = "branchlinks_upload.html"
    branchendpoint = 'https://api2.branch.io/v1/url'

    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    reader = csv.reader(io_string, delimiter=",", quotechar="|")
    lines = list(reader)
    number = 0
    metadata_list = []
 
    for column in lines[1: ]:
        
        number += 1
        # update metadata to set key value pairs of the values in each column
        # set $marketing_title to set the title of link in Quick Links, remove if not intended to be updated in quick links dashboard
        metadata = {
            "mvp_code": column[0],
            "brand": column[1],
            "channel": column[2],
            "vendor": column[3],
            "placement_type": column[4],
            "audience": column[5],
            "placement_name": column[6],
            "$fallback_url": column[7],
            "$deeplink_path": column[8],
            "~channel": column[9],
            "~campaign": column[10],
            "$desktop_url": column[11],
            "$marketing_title": column[6]
        }
        # update branch_key to be the same as your client
        # set alias if you want to provide your app.link a custom alias otherwise remove
        # set type:2 so it can appear as a Quick Link and editable in the dashboard
        data = {
            "branch_key": "YOUR_BRANCH_KEY",
            "alias": column[6],
            "type": 2,
            "data": metadata,
        }

        # sending post request and saving response as response object
        r = requests.post(url = branchendpoint, data = json.dumps(data))

        try:
            jsonData = json.loads(r.text)
            if 'url' in jsonData:
                metadata['branch_link'] = jsonData['url']
                metadata['fallback_url'] = metadata['$fallback_url']
                metadata['deeplink_path'] = metadata['$deeplink_path']
                metadata['utm_source'] = metadata['~channel']
                metadata['utm_campaign'] = metadata['~campaign']
                metadata['desktop_url'] = metadata['$desktop_url']
                print(jsonData['url'])
            else:
                print(r.text)
        except ValueError:
            print ('Decoding JSON has failed')

        metadata_list.append(metadata)
        context = {'metadata_list': metadata_list}

    print(metadata_list)
    if number == len(lines[1: ]):
        return render(request, "created_branch_links.html", context)
