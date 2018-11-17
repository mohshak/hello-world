import requests
import json

#aauthhenticatiioon

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"name\": \"admin\",\r\n\t\t\t\"pwd\": \"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)
##print(response.text)
##print(json_response['imdata'][0]['aaaLogin']['attributes']['token'])
tokenfromlogin =  (json_response['imdata'][0]['aaaLogin']['attributes']['token'])


#teenant aaccme



url = "http://192.168.10.1/api/node/mo/uni/tn-acme.json"

payload = "{\r\n\t\"totalCount\": \"1\",\r\n\t\"imdata\": [{\r\n\t\t\"fvTenant\": {\r\n\t\t\t\"attributes\": {\r\n\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\"dn\": \"uni/tn-acme\",\r\n\t\t\t\t\"name\": \"acme\",\r\n\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\"ownerTag\": \"\"\r\n\t\t\t},\r\n\t\t\t\"children\": [{\r\n\t\t\t\t\"vzBrCP\": {\r\n\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\"name\": \"Web\",\r\n\t\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\t\"ownerTag\": \"\",\r\n\t\t\t\t\t\t\"prio\": \"unspecified\",\r\n\t\t\t\t\t\t\"scope\": \"context\"\r\n\t\t\t\t\t},\r\n\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\"vzSubj\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"consMatchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\"name\": \"Web\",\r\n\t\t\t\t\t\t\t\t\"prio\": \"unspecified\",\r\n\t\t\t\t\t\t\t\t\"provMatchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\t\t\"revFltPorts\": \"yes\"\r\n\t\t\t\t\t\t\t},\r\n\t\t\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\t\t\"vzRsSubjFiltAtt\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"tnVzFilterName\": \"Web\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t}]\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}]\r\n\t\t\t\t}\r\n\t\t\t}, {\r\n\t\t\t\t\"drawCont\": {\r\n\t\t\t\t\t\"attributes\": {},\r\n\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\"drawInst\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"info\": \"{'epg-Payroll-undefined':{'x':700,'y':60},'epg-Bills-undefined':{'x':700,'y':60}}\",\r\n\t\t\t\t\t\t\t\t\"oDn\": \"uni/tn-acme/ap-Accounting\"\r\n\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}]\r\n\t\t\t\t}\r\n\t\t\t}, {\r\n\t\t\t\t\"fvRsTenantMonPol\": {\r\n\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\"tnMonEPGPolName\": \"\"\r\n\t\t\t\t\t}\r\n\t\t\t\t}\r\n\t\t\t}, {\r\n\t\t\t\t\"fvAp\": {\r\n\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\"name\": \"Accounting\",\r\n\t\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\t\"ownerTag\": \"\",\r\n\t\t\t\t\t\t\"prio\": \"unspecified\"\r\n\t\t\t\t\t},\r\n\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\"fvAEPg\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\t\t\"name\": \"Payroll\",\r\n\t\t\t\t\t\t\t\t\"prio\": \"unspecified\"\r\n\t\t\t\t\t\t\t},\r\n\t\t\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\t\t\"fvRsCustQosPol\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"tnQosCustomPolName\": \"\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\t\t\t\t\t\"ownerTag\": \"\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\t\t\"fvRsProv\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\t\t\t\t\"prio\": \"unspecified\",\r\n\t\t\t\t\t\t\t\t\t\t\"tnVzBrCPName\": \"Web\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t}]\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\"fvAEPg\": {\r\n\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\t\t\t\t\t\"name\": \"Bills\",\r\n\t\t\t\t\t\t\t\t\"prio\": \"unspecified\"\r\n\t\t\t\t\t\t\t},\r\n\t\t\t\t\t\t\t\"children\": [{\r\n\t\t\t\t\t\t\t\t\"fvRsCons\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"prio\": \"unspecified\",\r\n\t\t\t\t\t\t\t\t\t\t\"tnVzBrCPName\": \"Web\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t}, {\r\n\t\t\t\t\t\t\t\t\"fvRsCustQosPol\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"tnQosCustomPolName\": \"\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t},  {\r\n\t\t\t\t\t\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\t\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\t\t\t\t\t\"ownerTag\": \"\"\r\n\t\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t\t}\r\n\t\t\t\t\t\t\t}]\r\n\t\t\t\t\t\t}\r\n\t\t\t\t\t}]\r\n\t\t\t\t}\r\n\t\t\t}]\r\n\t\t}\r\n\t}]\r\n}"
cookie = {"APIC-cookie":tokenfromlogin}
#response = requests.request("POST", url, data=payload)
response = requests.request("POST", url, data=payload,  cookies=cookie)

print(response.text)



##payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme\",\r\n\t\t\t\"name\": \"acme\",\r\n\t\t\t\"rn\": \"tn-acme\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"





#appllication proofile accounnttingg

#url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant/ap-Accounting.json"

##payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme\",\r\n\t\t\t\"name\": \"acme\",\r\n\t\t\t\"rn\": \"tn-acme\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
#cookie = {"APIC-cookie":tokenfromlogin}

#response = requests.request("POST", url, data=payload,  cookies=cookie)

#print(response.text)
