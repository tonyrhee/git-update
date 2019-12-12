#!/usr/bin/python
import git
from git.refs.tag import TagReference
import os
# from sendemail import send_email
import time

while True:
    repo = git.Repo(os.getcwd())
    remote = repo.remotes.origin
    remote.fetch()
    print(repo.head.commit == remote.refs.master.commit)
    if repo.head.commit != remote.refs.master.commit:
        tagref = ''
        if TagReference.list_items(repo):
            tagref = TagReference.list_items(repo)[-1]
            print(tagref.tag.message)
        remote.pull()
        with open('status.txt', 'a+') as f:
            f.write(f'{repo.head.commit.authored_datetime} {remote.refs.master.commit} {repo.head.commit.message} {tagref.tag.message}\n')
            print('pulled')
            f.close()
    else:
        print('Not pulled')
    print(repo.head.commit == remote.refs.master.commit)
    # print(remote.refs.master.commit)
    # print(repo.head.commit)
    # print(repo.head.commit.message)
    time.sleep(60*5)
