PLACEHOLDER = '[name]'
with open('section 24/project 2/Input/Names/invited_names.txt') as list_name:
    names = list_name.readlines()

with open('section 24/project 2/Input/Letters/starting_letter.txt') as letter:
    letter_form = letter.read()
    for name in names:
        formatted_name = name.strip()
        new_letter = letter_form.replace(PLACEHOLDER, formatted_name)
        with open(f"section 24/project 2/Output/ReadyToSend/letter_for_{formatted_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)
