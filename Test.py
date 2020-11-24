from req import request_body
import sys

def main()->None:
    header = {"Content-Type":"application/json","x-mnubo-username":"test","x-mnubo-namespace":"bdd_ai_import_file"}
    payload = {"name":"testproject","purpose":"2"}
    runcommand = request_body(url="http://hybrid-model-processor.hybridmodel.dev.mnubo.org/v1/workflow/projects", headers = header, payload=payload)
    runcommand.response = request_body.get(runcommand).json()
    print(runcommand.response)

if __name__ == '__main__':
  sys.exit(not main())