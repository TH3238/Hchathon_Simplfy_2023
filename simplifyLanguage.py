import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
service = Service('C:\\Users\\Eliana\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe')  # Replace 'path_to_chromedriver' with the actual path to the chromedriver executable
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google Translate
driver.get("https://translate.google.com/")

# Find the input text box and enter Hebrew text
wait = WebDriverWait(driver, 20)  # Increase the timeout if needed
text_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.er8xn')))
text_box.clear()
text_box.send_keys("על בסיס הספרות התיאורטית הרלוונטית נוסחו שלוש השערות מחקר: ימצא קשר בין תחושת זלזול מצד בית החולים באם לבין אסקלציה בתוקפנותה, ימצא קשר בין עומס בבתי החולים לבין אסקלציה בתוקפנות האם והקמת מהומות יתפסו כחלק אינטגרלי מעבודת בית החולים. ממצאי המחקר אינם מאפשרים לאשש את השערת המחקר הראשונה, מאששים במלואם את השערת המחקר השנייה ומאששים באופן חלקי את השערת המחקר השלישית")  # Replace with your Hebrew text


######testing if it gets inputted
input_element = driver.find_element(By.CSS_SELECTOR, '.QFw9Te')
input_value = input_element.get_property('textContent')
if input_value:
    half_length = len(input_value) // 2
    first_half = input_value[:half_length]
    text_value = first_half
else:
    text_value = input_value
reversed_text1 = text_value[::-1]
print("Input complex text:", reversed_text1, '\n')
####end testing


# Wait for translation to appear
time.sleep(20)
translated_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ryNqvb')))
english_text = translated_text.text

# Print the translated text
print("Translated complex text:", english_text, '\n')

# Close the browser
driver.quit()



import os
import openai
openai.api_key = "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"
paragraph = "please rephrase the following text in vocabulary that will be understandable for 2nd grade children:" + english_text 

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": paragraph}
  ]
)
simplerEn = completion.choices[0].message.content

print("simplified english chatgpt version: ", simplerEn, '\n')

# Set up Selenium webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
service = Service('C:\\Users\\Eliana\\Desktop\\chromedriver_win32 (1)\\chromedriver.exe')  # Replace 'path_to_chromedriver' with the actual path to the chromedriver executable
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to Google Translate
driver.get("https://translate.google.com/?sl=en&tl=iw&text=h&op=translate/")

# Find the target language dropdown
wait = WebDriverWait(driver, 10)  # Create the wait variable before using it

# Find the input text box and enter Hebrew text
text_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.er8xn')))
text_box.clear()
text_box.send_keys(simplerEn)  # Replace with your Hebrew text


######testing if it gets inputted
input_element = driver.find_element(By.CSS_SELECTOR, '.QFw9Te')
input_value = input_element.get_property('textContent')
if input_value:
    half_length = len(input_value) // 2
    first_half = input_value[:half_length]
    text_value = first_half
else:
    text_value = input_value

print("Inputed simplified english text:", text_value, '\n')
####end testing


# Wait for translation to appear
time.sleep(20)
translated_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ryNqvb')))
hebrew_text = translated_text.text
reversed_text2 = hebrew_text[::-1]

# Print the translated text
print("Translated simplified text:", reversed_text2)
print("exacuted successfully!!!:)")
# Close the browser
driver.quit()

