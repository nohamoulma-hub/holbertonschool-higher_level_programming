#!/usr/bin/env python3
""" Creation a basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """ Serialize and save """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """ load and deserialize """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
