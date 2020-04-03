import tkinter as tk


class Metronome:

	def __init__(self, bpm, bpb):

		self.bpm = bpm
		self.bpb = bpb
		self.millisecPerBeep = int(60 / bpm * 1000)
		self.start = False
		self.count = 0
		self.root = tk.Tk()
		self.effectLabel = tk.Label(self.root, text = self.count)


	def starter(self):
		if self.start:
			self.start = False
		else:
			self.start = True

	def counter(self):	

		if self.start:
			if self.count % self.bpb == 0:
				print("BEEP")
				
			else:
				print("beep")

			self.effectLabel = tk.Label(self.root, text = self.count % self.bpb + 1)
			self.effectLabel.pack()			

			self.count += 1
			self.root.after(self.millisecPerBeep, self.counter)


	def interface(self):
		self.root.title("Metronome")
		self.root.geometry("800x800")

		actionButton = tk.Button(self.root, text = "Start / Stop", command = lambda: [self.starter(), self.counter()])
		actionButton.pack()


		self.root.mainloop()
		

met604 = Metronome(80, 4).interface()
