from midi2audio import FluidSynth

audio = 'Prelude1.mid'
FluidSynth().play_midi(audio)
fs = FluidSynth()
fs.midi_to_audio('input.mid', 'output.wav')
