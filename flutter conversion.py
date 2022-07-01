from tkinter import font


def which(ask):
	if ask[0] == "F":
		font = float(input("Enter font size in pixels: "))
		flutter = (72*font)/96
		return(print(f"{font} in flutter = {flutter}"))
	elif ask[0] == "E":
		element = float(input("Enter element size in pixel: "))
		flutter = (element/1.25)
		return(print(f"{element} in flutter = {flutter}"))
	else:
		return("Please re-run and enter a correct choice. Thank You !!")

print("This is a converter to convert pixels to flutter size.\n")
ask = input("Do you want to convert	font size or element size ? ").upper()
print(which(ask))