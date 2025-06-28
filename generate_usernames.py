#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description="A tool to generate potential AD usernames based on 'firstname lastname' combinations")
    parser.add_argument('userfile', help="A file containing 'firstname lastname' combinations")
    parser.add_argument('--domain', help="Append a domain to the output")
    args = parser.parse_args()

    file = open(args.userfile)

    if not file:
        print(f'Could not open {args.userfile}. Exiting...')
        exit(1)

    # add some default usernames
    usernames = [
        'admin', 'administrator', 'guest', 'user',
        'test', 'testing', 'anonymous', 'root',
        'toor', 'client', 'server', 'srv', 'srvc',
        'service', 'office', 'info', 'backup'
    ]

    for line in file:
        line = line.strip()
        if line and len(line.split(' ')) > 1:
            fname = line.split(' ')[0]
            lname = line.split(' ')[-1]
            usernames.append(fname)
            usernames.append(lname)
            delimiters = [ '', '.', '_', '-' ]
            for i in range(2):
                for delimiter in delimiters:
                    usernames.append(fname[0] + delimiter + lname)
                    usernames.append(fname[0:2] + delimiter + lname)
                    usernames.append(fname[0:3] + delimiter + lname)
                    usernames.append(fname[0:2] + delimiter + lname[0:2])
                    usernames.append(fname[0:3] + delimiter + lname[0:3])
                    usernames.append(fname + delimiter + lname)
                lname, fname = fname, lname
        elif line:
            usernames.append(line)
    file.close()

    for username in set(usernames):
        if args.domain:
            print(f'{username.lower()}@{args.domain.lower()}')
        else:
            print(username.lower())

if __name__ == "__main__":
    main()
