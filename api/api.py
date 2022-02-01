import requests
import json

def check(ele,  word):

    for data in range(len(ele)):
        if (isinstance(ele[data], list)):
            check(ele[data],  word+"["+str(data)+"]")
        elif (isinstance(ele[data], str)):
            printfield(ele[data],  word+"["+str(data)+"]")
        else:
            checkDict(ele[data],  word+"["+str(data)+"]")

def checkDict(jsonObject,  Word):

    for ele in jsonObject:
        if (isinstance(jsonObject[ele], dict)):
            checkDict(jsonObject[ele],  Word+"."+ele)

        elif (isinstance(jsonObject[ele], list)):
            check(jsonObject[ele],  Word+"."+ele)

        elif (isinstance(jsonObject[ele], str)):
            printfield(jsonObject[ele],   Word+"."+ele)

def printfield(ele, Word):
    print (Word, ":" , ele)


def Main(Store_Data):
    for element in Store_Data:
        if (isinstance(Store_Data[element], dict)):
            checkDict(Store_Data[element], element)
        elif (isinstance(Store_Data[element], list)):
            check(Store_Data[element], element)
        elif (isinstance(Store_Data[element], str)):
            printfield(Store_Data[element], element)


if __name__=="__main__":

    Api_Url = "https://api.modv.io/swagger/docs"
    Result = requests.get(Api_Url)
    Store_Data = Result.json()
    Main(Store_Data)
