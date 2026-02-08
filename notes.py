notes = []
def add_note(text):
    notes.append(text)
def list_notes():
    return notes
if __name__ == "__main__":
    add_note("First note")
    print(list_notes())
