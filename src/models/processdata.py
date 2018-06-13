
from flask import json

from src.authdata import client, ocrAPIKey
import requests

class ImageDetect(object):
    def __init__(self ,t1):
        self. t1 =t1

    @classmethod
    def SightEngineCall(cls ,Img): female="Female"

        output = client.check('celebrities', 'face-attributes').set_file(Img)
        femaleProb=output[ "faces"][0]["attributes"]["female"]
        if femaleProb >=0.90:
            female = "Female"
        else:
            female = "Male"

        faceDet = output["faces"][0]['y2']
        noseDet = output["faces"][0]['features']['nose_tip']['y']
        if faceDet > 0 and noseDet > 0:
            face = "YES"
        else:
            face = "NO"

        return cls, female, face

    @classmethod
    def ocr_space_file(cls, Img, overlay=False):
        """ OCR.space API request with local file.
            Python3.5 - not tested on 2.7
        :param filename: Your file path & name.
        :param overlay: Is OCR.space overlay required in your response.
                        Defaults to False.
        :param language: Language code to be used in OCR.
                        List of available language codes can be found on https://ocr.space/OCRAPI
                        Defaults to 'en'.
        :return: Result in JSON format.
        """

        payload = {'isOverlayRequired': overlay,
                   'apikey': ocrAPIKey,
                   'language': 'eng',
                   }
        with open(Img, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                              files={Img: f},
                              data=payload,
                              )
        r1=r.content. decode()
        p = json.loads(r1)
        p1 = p["ParsedResults"]
        for item in p1:
            p2 = item["ParsedText"]
        p2 = p2.upper()

        # Check for DL
        if "DRIVER LICENSE" not in p2:
            dLicense = 'No'
        else:
            dLicense = 'Yes'


        return cls, p2, dLicense