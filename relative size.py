print("This is a calculator ro find the relative size in flutter.\n")
ask = float(input("What is 'MediaQuery.of(context).size.width' of your screen? "))
size = float(input("Relative size of the size (in flutter unit) you want to find: "))
relativeSize = ask/size
print(f"\nSize relative to your screen width = 'MediaQuery.of(context).size.width'/{relativeSize}\n")