# Farr.AI

This is my pelican static-site generation for Farr.AI

Of very _very_ minor note is the `publish.sample.py` that is used to build a deploy version and do an FTP sync.  It's not a great FTP sync in that it won't remove old files that are present on the remote server but not locally (i.e. you delete a file), but it works well enough for now.

It's best to rename `publish.sample.py` to `publish.py` since it's in the `.gitignore` and won't accidentally be added to your repo with credentials.