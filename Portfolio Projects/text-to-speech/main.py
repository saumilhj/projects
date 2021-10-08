from gtts import gTTS
import pdfplumber

full_text = ""
with pdfplumber.open('story.pdf') as pdf:
    pages = pdf.pages
    for page in pages:
        text = page.extract_text()
        full_text += text
# print(full_text)

audio = gTTS(full_text, lang='en', tld='co.uk', slow=False)
filename = input('Enter the name of the file: ')
print('Converting ...')
audio.save(f'{filename}.mp3')
print('Your file is ready!')