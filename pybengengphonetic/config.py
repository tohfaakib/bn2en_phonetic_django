#!/usr/bin/env python

import os
import simplejson as json
import codecs


# Constants
# -- Path to current directory
BASE_PATH = os.path.dirname(__file__)
# -- path to avrodict.json
# AVRO_DICT_FILE = BASE_PATH+r"\resources\avrodict.json"
AVRO_DICT_FILE = "pybengengphonetic/resources/avrodict.json"
NAMES_DICT_FILE = "pybengengphonetic/resources/namesdict.json"
# -- Loads json data from avrodict.json
AVRO_DICT = json.load(codecs.open(AVRO_DICT_FILE, encoding='utf-8'))
NAMES_DICT = json.load(codecs.open(NAMES_DICT_FILE, encoding='utf-8'))
# -- Shortcut to vowels
AVRO_VOWELS = set(AVRO_DICT['data']['vowel'])
# -- Shortcut to consonants
AVRO_CONSONANTS = set(AVRO_DICT['data']['consonant'])
# -- Shortcut to case-sensitives
AVRO_CASESENSITIVES = set(AVRO_DICT['data']['casesensitive'])
# -- Shortcut to number
AVRO_NUMBERS = set(AVRO_DICT['data']['number'])
