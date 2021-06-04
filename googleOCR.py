import os, io

def detect_text(table_num, max_num):    
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    file = open('sr/sample %d.txt'%(table_num),'w', encoding='UTF-8')
    
    for num in range(max_num):
        path = "sr/sample (%d)/sample %d-%d.jpg"%(table_num, table_num, num+1)
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        
        if len(texts) > 0:
            print(texts[0].description)
            file.write("<%d 번째> "%(num + 1))
            file.write("%s\n"%(texts[0].description))
