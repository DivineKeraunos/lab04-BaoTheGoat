import pytest
from bank import BankAccount

@pytest.fixture
def account():
    
Zwe Naing Set@Divinity MINGW64 ~
$ cd lab04-BaoTheGoat

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ cat > .gitignore << 'EOF'
> venv/
> __pycache__/
> .pytest_cache/
> *.pyc
> EOF

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ cat > bank.py << 'PY'
> class BankAccount:
> def __init__(self, balance=0):
> self.balance = balance
>
> def deposit(self, amount):
> self.balance += amount
> return self.balance
>
> def withdraw(self, amount):
> if amount > self.balance:
> raise ValueError("Insufficient funds")
> self.balance -= amount
> return self.balance
> PY

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ git add .gitignore bank.py
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'bank.py', LF will be replaced by CRLF the next time Git touches it

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ git commit -m "chore: add gitignore and bank module"
[main a261237] chore: add gitignore and bank module
 2 files changed, 17 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 bank.py

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 523 bytes | 523.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/DivineKeraunos/lab04-BaoTheGoat.git
   e6daff9..a261237  main -> main

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ git log --oneline
a261237 (HEAD -> main, origin/main, origin/HEAD) chore: add gitignore and bank module
e6daff9 Update README.md
49564bc Initial commit

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ git remote -v
origin  https://github.com/DivineKeraunos/lab04-BaoTheGoat.git (fetch)
origin  https://github.com/DivineKeraunos/lab04-BaoTheGoat.git (push)

Zwe Naing Set@Divinity MINGW64 ~/lab04-BaoTheGoat (main)
$ cat > test_deposit.py << 'PY'
> import pytest
> from bank import BankAccount
>
> @pytest.fixture
> def account():
>     return BankAccount(100)


def test_deposit_positive(account):
    assert account.deposit(50) == 150

def test_deposit_zero(account):
    assert account.deposit(0) == 100
