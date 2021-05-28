import json
"""
This module does the below activity
1. Reads the input json file
2. Identify the fields that are missing or has invalid values
3. Identify the duplicate records
"""

raw_data = {}
invalid_record = []


def data_reader():
    '''
    Convets the data from json to python object
    '''
    global raw_data
    with open('data.json') as json_file:
        raw_data =json.load(json_file)

def identify_non_compliant_records():
    '''
    Identifies the non compliant which is empty or None or missing
    '''
    global invalid_record
    mandatory_field = {'name', 'address', 'zip'}
    
    for i in raw_data:
        if mandatory_field.issubset(set(i.keys())) and None not in i.values() and '' not in i.values() and len(i.get('zip','')) == 5 and i.get('zip','').isdigit():
            pass
        else:
            invalid_record.append(i.get('id'))

def identify_duplicate_record():
    '''
    Identify record which has duplicate address, zip, name
    '''
    data_converter = {}
    modified_record = {i['id'] : (i.get('address',''), i.get('zip', ''), i.get('name', '')) for i in raw_data}
    for k,v in modified_record.items():
        data_converter.setdefault(v,set()).add(k)
    duplicate_record = []
    [duplicate_record.extend(list(v)) for k,v in data_converter.items() if len(v)>1]

    invalid_record.extend(duplicate_record)
    print("************INVALID RECORDS**************")
    print("\n".join(set(invalid_record)))
    print("**************COMPLETED******************")

#Entry Point
if __name__ == '__main__':
    data_reader()
    if raw_data:
        identify_non_compliant_records()
        identify_duplicate_record()
    