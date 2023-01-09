import main
import requests
import os
import openai
openai.organization = "org-W83KL7qbGMKBZZvqPqLyPdmE"
openai.api_key = os.getenv("YOUR_API_KEY")
openai.Model.list()