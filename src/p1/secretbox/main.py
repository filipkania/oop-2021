from src.p1.secretbox.Password import Password
from src.p1.secretbox.SecretBox import SecretBox

if __name__ == "__main__":
    x = SecretBox()

    x.open("ABCDEF:^)")

    a = Password(website="Twitter", username="user219", password="aLhA2WJfkpz1q1Ry")
    x.store_secret(a)

    e = x.get_secret("Twitter")
    print(
        '\n'.join([f"UUID: {a.uuid}, Website: {a.website}, Username: {a.username}, Password: {a.password}" for a in e])
    )

    x.lock()