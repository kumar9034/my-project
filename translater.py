from googletrans import Translator  # type: ignore
from gtts import gTTS  # type: ignore
import os
import pyttsx3
import PyPDF2

# Open the PDF file
try:
    book = open('amit.pdf', 'rb')
except FileNotFoundError:
    print("The file 'amit.pdf' was not found. Please check the file path.")
    exit()

# Initialize PDF reader
try:
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    print(f"Number of pages in the PDF: {pages}")
except Exception as e:
    print(f"An error occurred while reading the PDF: {e}")
    exit()

# Initialize the translator
translator = Translator()

# Choose the page to translate
page_number = 11


if page_number >= pages:
    print(f"The PDF only has {pages} pages, but you requested page {page_number + 1}.")
    exit()

# Extract text from a specific page
try:
    page = pdfReader.pages[page_number]
    text = page.extract_text()
    if not text:
        print(f"No text found on page {page_number + 1}.")
        exit()

    # Translate the text from English to Hindi
    translation = translator.translate(text, src='en', dest='hi')
    hindi_text = translation.text

    # Print the translated text
    print(f"Translated to Hindi: {hindi_text}")
except Exception as e:
    print(f"An error occurred while extracting or translating text: {e}")
    exit()

# Convert the translated text to speech using gTTS
try:
    tts = gTTS(text=hindi_text, lang='hi')
    audio_file = "translated_audio.mp3"
    tts.save(audio_file)

    # Play the audio file (adjust command based on OS)
    if os.name == 'nt':  # Windows
        os.system(f"start {audio_file}")
    elif os.name == 'posix':  # macOS or Linux
        os.system(f"open {audio_file}")
except Exception as e:
    print(f"An error occurred while generating or playing the audio: {e}")
    exit()
