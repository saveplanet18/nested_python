import json 
import re

Url_path = "JsonFile\data .json"
with open(Url_path, 'r') as j:
     contents = json.loads(j.read())
Details = contents['ocrInfomation']

zip_code = re.findall(r'',Details)
print(zip_code)


def getUrl(string):  
    regex = r"""(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"""
    url = re.findall(regex,string)
    string = [x[0] for x in url]      
    return "".join(string)


def get_phone_number(lst):    
            phoneNums = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
            pattern = phoneNums.finditer(lst)
            string_pattern = [x[0] for x in pattern]
            return ",".join(string_pattern)

def get_email(lst): # email
        mail = re.compile("([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", re.IGNORECASE) 
        pattern = mail.finditer(lst)
        string = [x[0] for x in pattern]
        return  "".join(string)

def get_Name(lst):
    re_pattern = "EB/EastBridge The Science of Strategic"
    regex = re.compile(re_pattern)
    for name in regex.finditer(lst):
        return(name.group(0))

def get_Address(lst):
    re_pattern =  re.compile('(Eva Hu Suite 1206|Center|No.22 Shishan Road|District|Jiangsu|China)\W?(?=\s|$)', re.IGNORECASE)
    result = re_pattern.finditer(lst)
    string = [x[0] for x in result]
    return "".join(string)
        

def Get_Zip_Code(lst):
    zip_code = re.compile(r'^\d\d\d\d\d\d$')
    result = zip_code.finditer(lst)
    string = [x[0] for x in result]
    return "".join(string)

def Main():

    mail = get_email(Details)
    result = getUrl(Details)
    phone_number = get_phone_number(Details)
    company_name = get_Name(Details)
    company_address = get_Address(Details)
    zip_code = Get_Zip_Code(Details)

    Final_text = {
        "Company_url": result,
        "Company_phoneNumber":phone_number,
        "Company_mail":mail,
        "Company_Name":company_name,
        "Company_Address":company_address,
        "Zip_Code":zip_code,
    }
    print(Final_text)


if __name__=="__main__":
    Main()


