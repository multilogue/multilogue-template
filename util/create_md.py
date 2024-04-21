# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
import jsonlines
from wireframes.continuous import simple_continuation, commented_continuation


def load_record(self):
    with jsonlines.open('./record.jsonl', 'r') as reader:
        record = [line for line in reader.iter()]


    return record


def create_md_text(template: dict, record: dict) -> str:
    for line in record:
        md_text = template.format(
            first_interlocutor_name=record['first_interlocutor_name'],
            first_interlocutor_utterance=record['first_interlocutor_utterance']
        )
        md_text += template['second_interlocutor'].format(
            second_interlocutor_utterance=record['second_interlocutor_utterance']
        )
    return md_text


if __name__ == "__main__":
    record = load_record()
    create_md_text(template=simple_continuation)