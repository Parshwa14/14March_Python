import instaloader

name = input("Enter instagram ID : ")

instaloader.Instaloader().download_profile(name,profile_pic_only=False)

print("Download Successfully")