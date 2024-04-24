file = str(input("File name: ")).strip().lower()
if ".jpg" in file:
    print("image/jpeg")
elif ".jpeg" in file:
    print("image/jpeg")
elif ".gif" in file:
    print("image/gif")
elif ".pdf" in file:
    print("application/pdf")
elif ".png" in file:
    print("image/png")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
