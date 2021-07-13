#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys

args = sys.argv
input_file = args[1]

path_w = 'train.txt'

count_length = 0

with open(path_w, mode='w') as f_out:
  with open(input_file) as f_in:
    json_text = json.load(f_in)
    for v_result in json_text.values():
      for v_alternatives in v_result:
        for val_list in v_alternatives.values():
          if isinstance(val_list, list):
            for val in val_list:
              count_length += len(val.get('transcript'))
              f_out.write(val.get('transcript'))
              f_out.write('。\n')

print('文字数')
print(count_length)
