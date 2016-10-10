def standardVersion(mail):
    login, domain = tuple(map(str.lower, mail.split("@")))

    if domain == "bmail.com":
        login = login.replace(".", "").split("+")[0]

    return login + "@" + domain


def main():
    n = int(input())
    mails = [input() for _ in range(n)]
    groups = dict()

    for mail in mails:
        standard = standardVersion(mail)
        try:
            groups[standard].append(mail)
        except:
            groups[standard] = [mail]

    print(len(list(groups)))

    for group in groups:
        print(len(groups[group]), " ".join(groups[group]))


if __name__ == '__main__':
    main()
