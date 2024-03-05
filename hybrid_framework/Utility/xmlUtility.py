import json

import xmltodict# install
import xmltojson# install
import pprint

# with open(r"C:\Users\user\PycharmProjects\pythonProject_WD_eve_jan2024\hybrid_framework\TestData\test_data_xml.xml",
#      mode="r") as fh:
with open(r"C:\Users\Dhipak\OneDrive\FITA\Hybrid\hybrid_framework-part5 -day34\hybrid_framework\TestData\customer_page.xml",mode="r") as fh:
     xml_content = fh.read()
     # print("*********************")
     # print(fh.read())
# dt1 = xmltodict.parse(xml_content)
# pprint.pprint(dt1["login_data"]["row1"]['user'])


# JSON
dt1 = xmltojson.parse(xml_content)
js1 = json.loads(dt1)# convert json to dic
# js1 = json.dumps(dt1)# convert dict  to json
# print(js1["login_data"]["row1"]['user'])
# dict1 = json.loads(xmltojson.parse(fh.read()))
# print(dict1["login_data"])


def load_test_data(file):
     with open(file,mode="r") as fh:
          xml_content = fh.read()

     return xmltodict.parse(xml_content)


def load_test_data_from_json(file):
     with open(file,mode="r") as fh:
          xml_content = fh.read()

     return json.loads(xmltojson.parse(xml_content))