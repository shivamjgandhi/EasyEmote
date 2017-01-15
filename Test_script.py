#Python script for game

from PIL import Image
import os
import time 
import requests

def cycle(filepath):
    # Display images within Jupyter
    
    _url = 'https://api.projectoxford.ai/emotion/v1.0/recognize'
    _key = 'a5b5547007d54be7aa5bb75555376661'
    _maxNumRetries = 10
    
    ##############################################################
    
    def processRequest( json, data, headers, params ):
    
        """
        Helper function to process the request to Project Oxford
    
        Parameters:
        json: Used when processing images from its URL. See API Documentation
        data: Used when processing image read from disk. See API Documentation
        headers: Used to pass the key information and the data type request
        """
    
        retries = 0
        result = None
    
        while True:
    
            response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )
    
            if response.status_code == 429: 
    
                print( "Message: %s" % ( response.json()['error']['message'] ) )
    
                if retries <= _maxNumRetries: 
                    time.sleep(1) 
                    retries += 1
                    continue
                else: 
                    print( 'Error: failed after retrying!' )
                    break
    
            elif response.status_code == 200 or response.status_code == 201:
    
                if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                    result = None 
                elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                    if 'application/json' in response.headers['content-type'].lower(): 
                        result = response.json() if response.content else None 
                    elif 'image' in response.headers['content-type'].lower(): 
                        result = response.content
            else:
                print( "Error code: %d" % ( response.status_code ) )
                print( "Message: %s" % ( response.json()['error']['message'] ) )
    
            break
            
        return result
        
            
    ########################################################
    
    # URL direction to image
    with open( filepath, 'rb' ) as f:
        data = f.read()    
        
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    headers['Content-Type'] = 'application/octet-stream' 
    
    json = None
    params = None
    
    result = processRequest( json, data, headers, params )
    
    if result is not None:
        u1 = result[0]
        u1scores = u1['scores']
        maxnum = u1scores['sadness']
        maxemotion = 'sadness'
        if (maxnum < u1scores['neutral']):
            maxnum = u1scores['neutral']
            maxemotion = 'neutral'
            
        if (maxnum < u1scores['contempt']):
            maxnum = u1scores['contempt']
            maxemotion = 'contempt'
            
        if (maxnum < u1scores['disgust']):
            maxnum = u1scores['disgust']
            maxemotion = 'disgust'
            
        if (maxnum < u1scores['anger']):
            maxnum = u1scores['anger']
            maxemotion = 'anger'
            
        if (maxnum < u1scores['surprise']):
            maxnum = u1scores['surprise']
            maxemotion = 'surprise'
        
        if (maxnum < u1scores['fear']):
            maxnum = u1scores['fear']
            maxemotion = 'fear'
            
        if (maxnum < u1scores['happiness']):
            maxnum = u1scores['happiness']
            
        print(filepath)
        return maxemotion
        
#Select directory to take pictures from

total_pics = 0
total_correct = 0

#Go through each picture
for filename in os.listdir("C:\\Users\\shivam gandhi\\Tests\\"):
    
    #Display picture
#    image = Image.open("C:\\Users\\shivam gandhi\\Tests\\" + filename)
#    image.show()
    
    #Ask user what their answer is
    print("What is the emotion being shown? Answer in the following way:")
    print("1 for sadness")
    print("2 for neutral")
    print("3 for contempt")
    print("4 for disgust")
    print("5 for anger")
    print("6 for surprise")
    print("7 for fear")
    print("8 for happiness")
    response = input('Enter your answer: ')
    
    #Inform them whether they got the answer right or wrong
    emotion = cycle('C:\\Users\\shivam gandhi\\Tests\\' + filename)
    if (emotion == "sadness") and (response == 1):
        total_correct = total_correct + 1
    elif emotion == "neutral" and response == 2:
        total_correct = total_correct + 1
    elif emotion == "contempt" and response == 3:
        total_correct = total_correct + 1
    elif emotion == "disgust" and response == 4:
        total_correct = total_correct + 1
    elif emotion == "anger" and response == 5:
        total_correct = total_correct + 1
    elif emotion == "surprise" and response == 6:
        total_correct = total_correct + 1
    elif emotion == "fear" and response == 7:
        total_correct = total_correct + 1
    elif emotion == "happiness" and response == 8:
        total_correct = total_correct + 1
        
    total_pics = total_pics + 1
    
#Return final score 
print("Your total score was: " + str(total_correct) + " out of " + str(total_pics))