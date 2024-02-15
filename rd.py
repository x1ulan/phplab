import secrets

for i in range(1,11):
    print(f"$php{i}_secret = \"flag{{{secrets.token_urlsafe(30)}}}\";")