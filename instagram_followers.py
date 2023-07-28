# import instaloader
# from instaloader import Profile, Post
#
# insta = instaloader.Instaloader()
# insta.login(user="qnfrrpvlsmsshdmf", passwd="lonely1995")
#
# profile = instaloader.Profile.from_username(insta.context, "ara.dawn")
#
# follow_list = []
# count = 0
# for followee in profile.get_followers():
#     follow_list.append(followee.username)
#     print(f"{count} : {follow_list[count]}")
#     count = count + 1

result = 0
for value in range(1, 10):
    result = result + value

print(result)