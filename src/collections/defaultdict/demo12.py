blacklist = {"bad_user1", "spammer", "bot123"}

USER_NAME = "bot123"
if USER_NAME in blacklist:
    print("Access denied.")
else:
    print("Access granted.")
