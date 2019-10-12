#!/usr/bin/python3

import argparse  # noqa: E402
import os
import sys
import yaml

# TODO: This should be consolidated in a single location with main.py, but due to imports - it's here again
parser = argparse.ArgumentParser(description='Process disc using ARM')
parser.add_argument('-d', '--devpath', help='Devpath', required=True)
args = parser.parse_args()

yamlfile = "/etc/arm/arm.yaml"

with open(yamlfile, "r") as f:
    cfg = yaml.load(f)
    
    # Add a convenience config for multi-DB setups
    # Note: This assumes the drive_id is simple like sr0, sr1, ... srN
    drive_id = args.devpath
    cfg['DRIVE_ID'] = drive_id

    db_path = cfg['DBFILE']
    filename, file_extension = os.path.splitext(db_path)
    cfg['DBFILE'] = f"{filename}.{drive_id}.db"
