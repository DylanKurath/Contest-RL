import tkinter as tk
import tkinter.ttk as ttk
from simulator import simulationWindow
from math import floor
from moves import listMoves

if __name__ == "__main__":
    rootWindow = tk.Tk()
    title = ttk.Label(rootWindow, text="Pokemon Contest Simulator")
    title.pack()

    contestType = tk.StringVar()
    typeSelector = ttk.Combobox(rootWindow, textvariable=contestType)
    typeSelector.values = listMoves()
    for i in range(4):
        playerFrame = ttk.Frame(rootWindow)
        playerFrame.grid(col=i%2, row=floor(i/2))
        playerLabel = ttk.Label(playerFrame, text="Player " + str(i+1))
        playerLabel.pack()

        ttk.Label(playerFrame, text="Move " + str(j+1)).grid(col=0,row=0, columnspan=2)
        moveEntry = ttk.Entry(rootWindow)
        moveEntry.pack()


    simulateButton = ttk.Button(rootWindow, text="Start Contest", command=simulationWindow)
    simulateButton.pack()

    rootWindow.mainloop()