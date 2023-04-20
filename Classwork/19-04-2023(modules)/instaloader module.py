import instaloader

name = input("Enter instagram ID : ")

insta = instaloader.Instaloader()

insta.download_profile(name,profile_pic_only=True)
