C4 = 60
C5 = C4 + 12
def pitch_class(pitch):
	return pitch % 12
print (pitch_class(100))

def note_name(midi_number):
	

	chromatic_scale_sharps = ["C", "C#", "D", 
"D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

	return chromatic_scale_sharps[pitch_class(midi_number)]
	
	
print (note_name(69))


print (note_name(420))