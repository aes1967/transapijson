import os
from google.cloud import translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\USER\Desktop\api\TranslationAPI\crypto-plexus-354512-b8f9acb812ce.json"

translate_client = translate.Client()

text = 'hello world'
target = 'tr'

output = translate_client.translate(
    text,
    target_language=target
)
print(output)