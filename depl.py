from os import system

msg = input("Enter a commit message: ")
system("git add .")
system(f"git commit -m \"{msg}\"")
system("git push origin main")
