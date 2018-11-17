import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\r\ncookie=\"1542466938/c0ded377-6d5d-4c9d-bd57-25b448a883d1\"\r\ninHierarchical=\"false\">\r\n    <inConfigs>\r\n<pair key=\"org-root/org-PythonMaster\">\r\n    <orgOrg\r\n    name=\"PythonMaster\"\r\n    dn=\"org-root/org-PythonMaster\"\r\n    \r\n    status=\"created\"\r\n    \r\n    sacl=\"addchild,del,mod\">\r\n    </orgOrg>\r\n</pair>\r\n    </inConfigs>\r\n</configConfMos>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
