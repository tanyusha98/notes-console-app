from notes import add_note, list_notes

def test_add_note():
    add_note("Test")
    assert "Test" in list_notes()
