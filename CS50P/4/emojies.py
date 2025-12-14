import emoji 
emoji_dict = emoji.EMOJI_DATA
x=input("Enter a string: ")
for alias, data in emoji_dict.items():
    if alias in x:
        x = x.replace(alias, data['emoji'])

print(f"Converted string: {x}")