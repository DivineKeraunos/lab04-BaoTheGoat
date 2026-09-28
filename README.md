# lab04-BaoTheGoat

# Who did what

| Member | Git Username | File |
|---|---|---|
| Zwe Naing Set | DivineKeraunos | test_deposit.py |
| Aung Thet Khine | AungThetKhine21 | conftest.py |
| Sai Lin That Maung | Sailinthant | test_withdraw.py |
| Shin Thant Aung | ShinnThanttAungg | test_teardown.py |
| Hein Naing Soe | ScottG619 | test_shared.py |

# Our Merge Conflict

## The Conflict Markers Encountered
When we ran into the merge conflict in README.md, Git added text markers directly inside the file to show us where our edits collided. The top section under <<<<<<< HEAD showed our local changes, the bottom section above >>>>>>> showed the remote edits pushed by another team member, and ======= separated the two competing versions.
## The Final Decision Made by the Team
After looking at both versions, our team decided the cleanest fix was to delete README.md completely. We staged the deletion, committed the change, and pushed it to GitHub so everyone on the team was back on the exact same page.
## Why Git Could Not Automatically Resolve the Conflict
Git couldn't automatically merge the file because multiple team members modified or removed the exact same lines at the same time. Since Git couldn't guess our team's intent or know whose changes were right, it stopped the process safely and left it to us to choose the final result.

#  Git Contribution Summary

$ git shortlog -sn
     7  DivineKeraunos
     7  Zwe Naing Set
     4  Aung Thet Khine
     4  ScottG619
     3  Hiruto shinn
     2  Makeat0
     1  Sailinthant
     1  ShinnThanttAungg

Zwe Naing Set - (DivineKeraunos + Zwe Naing Set)
Shin Thant Aung - (Makeat0 + ShinnThanttAungg)
Sai Lin Thant Maung - (Hirtuo + Sailinthant)
Hein Naing Soe - (ScottG619)
Aung Thet Khine - (Aung Thet Khine)

# Reflection Questions

1. Why was your push rejected, and how did you fix it?
   My push was rejected because another team member pushed changes to the GitHub repository before me. I fixed it by using git pull to get the latest changes and then git push again.

2. Why could Git not resolve the README conflict automatically?
   Git could not resolve the conflict because different team members changed the same part of the README.md at the same time. Git could not decide which version should be kept, so we resolved it manually.

3. What is the difference between committing and pushing?
   Committing saves the changes in the local Git repository on my computer. Pushing uploads those commits to the shared GitHub repository so other team members can see them.

4. How do fixtures reduce duplicated setup code in tests?
   Fixtures provide reusable setup code for tests, such as creating a BankAccount(100). This means multiple tests can use the same setup without writing the same code again.
   


