for line in file1:

        line1 = line.split(':')

        fname = line1[1]
        lname = line1[2]

        username = fname[0] + lname

        if username in usedUsernames:
            username += str(random.randint(0, 9))
        usedUsernames.append(username)

        fileOutput.write(line1[0] + ":" + username.lower() + ":" +
                         line1[1] + ":" + line1[2] + ":" + line1[3])

    for line in file2:

        line1 = line.split(':')

        fname = line1[1]
        lname = line1[2]

        username = fname[0] + lname

        if username in usedUsernames:
            username += str(random.randint(0, 9))
        usedUsernames.append(username)

        fileOutput.write("\n" + line1[0] + ":" + username.lower() + ":" +
                         line1[1] + ":" + line1[2] + ":" + line1[3])

    for line in file3:

        line1 = line.split(':')

        fname = line1[1]
        lname = line1[2]

        username = fname[0] + lname

        if username in usedUsernames:
            username += str(random.randint(0, 9))
        usedUsernames.append(username)

        fileOutput.write("\n" + line1[0] + ":" + username.lower() + ":" +
                         line1[1] + ":" + line1[2] + ":" + line1[3])

