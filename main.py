import os
import openai

import dataclasses
import logging
import math
import io
import sys
import time
import json
from typing import Optional, Sequence, Union

import tqdm
import copy
# Load your API key from an environment variable or secret management service
API_KEY = ''
openai.api_key = API_KEY


response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Tell me about OpenAI",
    temperature=1.0,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)


print(response)

