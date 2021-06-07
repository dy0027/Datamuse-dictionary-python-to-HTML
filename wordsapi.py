import requests
import json

def reverse_word_search(search):
    href = "https://api.datamuse.com/words?ml="+ search
    search = search.replace(" ","+")
    result = requests.get(href).text
    result = json.loads(result)
    if result == None:
        return("No words found")
    toReturn = ""
    if len(result)<10:
        for i in range(len(result)):
            toReturn += ("<h6>")
            toReturn += (result[i]['word'])
            toReturn += ("</h6>")
            toReturn += ("\n")
    else:
        for i in range(10):
            toReturn += ("<h6>")
            toReturn += (result[i]['word'])
            toReturn += ("</h6>")
            toReturn += ("\n")
    return toReturn

def word_search2(search):
    href = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+search
    result = requests.get(href).text
    result = json.loads(result)
    
    res = result[0]['meanings']
    print(result[0]['word'])
    for i in range(len(res)):
        print("type :" + res[i]['partOfSpeech'])
        for j in range(len(res[i]['definitions'])):
            print("definition " + str(j) + ": " + res[i]['definitions'][j]['definition'])
            #print("example: " + res[i]['definitions'][j]['example'])
            print("Example: " + res[i]['definitions'][j].get('example', "No example found!!!!!! "))
        print("\n")

#Uses the API JSON response to build a string
def word_search(search):
    href = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+search
    result = requests.get(href).text
    result = json.loads(result)
    if 'title' in result:
        if result['title'] == "No Definitions Found":
            return "No definitions found"
    toReturn = ""
    res = result[0].get('meanings', "No Meanings found!!!!!! ")
    toReturn += ("<h3>")
    toReturn += result[0]['word']
    toReturn += ("<h3>")
    toReturn += ("\n")
    toReturn += ("<div>")
    for i in range(len(res)):
        toReturn += ("<ul>")
        toReturn += ("<h3>")
        toReturn += ("type: " + res[i]['partOfSpeech'])
        toReturn += ("</h3>")
        toReturn+=("\n")
        for j in range(len(res[i]['definitions'])):
            toReturn += ("<ul>")
            toReturn += ("<h5>")
            toReturn += ("definition"+ ": " + res[i]['definitions'][j]['definition'])
            toReturn += ("</h5>")
            toReturn+=("\n")
            #print("example: " + res[i]['definitions'][j]['example'])
            toReturn += ("<h6>")
            toReturn += ("Example: " + res[i]['definitions'][j].get('example', "No example found!!!!!! "))
            toReturn += ("</h6>")
            toReturn+=("\n")
            toReturn += ("</ul>")
        toReturn += ("</ul>")
        toReturn+=("\n")
        toReturn+=("\n")
        print(toReturn)
    toReturn += ("</div>")
    return toReturn
