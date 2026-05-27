#!/usr/bin/env python3
""" Module who converting CSV Data to JSON Format """
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open(csv_filename, "w", encoding="utf-8") as data.json:
            json.dump(data, data.json)

    except FileNotFoundError:
        return False
