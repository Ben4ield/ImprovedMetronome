import tkinter as tk

start = False
count = 1

def alternate():
	global count
	global start
	count += 1
	
	if count % 2 == 0:
		start = True
	else:
		start = False

def metronome(bpm, bpb):
	metCount = 0
	milsecPerBeat = (60 / bpm) * 1000

	if start:
		if metCount % bpb:
			print("tick")
		else:
			print("TICK")
		metCount += 1


root = tk.Tk()
root.geometry("400x600")

switchButton = tk.Button(root, text = "Start / Stop", command = lambda: [alternate(), metronome(60,4)])
switchButton.pack()

root.mainloop()

