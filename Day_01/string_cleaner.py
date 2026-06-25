messy_inputs=["bhargvi !@#","Python@123_Pro@gram",""
"   Hello_World123"]
def clean_string(text: str)-> str:
    text=text.strip()
    cleaned_text =""
    for char in text:
        if char.isalpha():
            cleaned_text+=char
        elif char =='_':
            cleaned_text+=' '
        elif char == ' ':
            cleaned_text+=' '
    return cleaned_text.lower()
for item in messy_inputs:
    print(f"Original: {item}->cleaned: {clean_string(item)}")
