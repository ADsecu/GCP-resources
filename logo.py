
'''

Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file
that contains your service account key.
macOS = export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
Windows = $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

'''

import io # pip install --upgrade google-cloud-vision
import os
import wikipedia # pip install wikipedia

from google.cloud import vision
from google.cloud.vision import types


photo = 'photo.jpg' # Your photo name
this_folder = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(this_folder, photo)


result = []
def main(image_file):
    client = vision.ImageAnnotatorClient()
    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)

    responseLogos = client.logo_detection(image=image)
    logos = responseLogos.logo_annotations
    for logo in logos:
        result.append(logo.description)


if __name__ == '__main__':
    image_file = file_name
    main(image_file)
    count = 0
    for i in result:
        count = count + 1
        print('Logo Found! :  {}'.format(i))
    if count == 1:
        print(wikipedia.summary(result[0]))
    elif count > 1:
        print('\n More than one Logo , Please edit me :)')

    else:
        print('No Logo & Can not search on wikipedia :)')
