def combinations(username, password, idx, candiates):
    if idx>=len(candidates):
        print(f"{username}\t{password}")
        return
    
    skip = combinations(username, password, idx+1, candidates)
    password = password+candidates[idx]
    select = combinations(username, password, idx+1, candidates)


if __name__ == "__main__":
    username = "test123"
    candidates = "abcdefghijklmnopqrstuvwxyz0123456789"

    combinations(username, "", 0, candidates)

