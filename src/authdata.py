import os
from sightengine.client import SightengineClient

#client = SightengineClient('{api_user}', '{api_secret}') # don't forget to add your credentials

seUser=os.environ.get('seUser')
seApiKey=os.environ.get('seAPIKey')
client = SightengineClient(seUser, seApiKey)


#OCR Space
ocrAPIKey = os.environ.get('ocrAPIKey')