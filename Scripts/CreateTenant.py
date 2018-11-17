import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
cookie = {"APIC-cookie":"modhZDl5iAxYXusbmgQlttHMjndtb5X4p/MY2bjAGtn70sKGSiREOSfqYzdFv4iuoxPddWRw25nXT0r1lp94e3dVzj13J9ut8euk0VC0x55dsfavI704N+XKP1RtunesIOkcBlEJlUcVBMOhm9W30P8cZ1WY66Un1x9gF0S4bFk="}

response = requests.request("POST", url, data=payload,  cookies=cookie)

print(response.text)