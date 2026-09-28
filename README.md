# 1. Group Name: TeamX-Panda

## 2. Who Did What

| Team Member | GitHub Username | Contribution |
|---|---|---|
| Hein Zaw Lin - Hubert | 6705140038 | Deposit tests in `test_deposit.py` |
| Aye Than Tin - Aye | 6705140074-hash | Withdrawal tests in `test_withdraw.py` |
| Aung Myo Hlaing - Olary | 6705140040 | Teardown tests in `test_teardown.py` |
| Chan Myae Thaw Tar - Chan | 6705140048 | Shared tests in `test_shared.py` |
| Hein Thura Naung - Ivan | IvannCoder | Shared `funded_account` fixture in `conftest.py` |

## 3. Our Merge Conflict

During Round 3, all group members edited the `README.md` at around the same time and added their own information to the same section. The first team member successfully pushed their changes, while the other members received merge conflicts because they had also changed the same part of the file.

The conflict markers we encountered were:
# Ivan <<<<<<< HEAD

> 2b316d7e8bfcdeb7d8572c63f63839353e25adc6

> 1e8953e402c0c0b6eb1468792713a7036956b31a

# Chan Myae Thaw Tar <<<<<<< HEAD

> 792f52eb6da477b9d48769b200f20c73a2380f8e

> a52eab2ee7881a3976537cb39d13ff31c6594a9d

# Aung Myo Hlaing (6705140040) <<<<<<< HEAD

> 534ee35dff5c954408b98eaba42fb23b252b6107

> e82e67a6fc6fc2c8296f7707dd2b79e946b45754

After resolving the conflict, we kept the information for all group members and added each member's name to the final `README.md`.

### Final lines kept:
| Team Member | GitHub Username | Contribution |
|---|---|---|
| Hein Zaw Lin - Hubert | 6705140038 | Deposit tests in `test_deposit.py` |
| Aye Than Tin - Aye | 6705140074-hash | Withdrawal tests in `test_withdraw.py` |
| Aung Myo Hlaing - Olary | 6705140040 | Teardown tests in `test_teardown.py` |
| Chan Myae Thaw Tar - Chan | 6705140048 | Shared 2 tests in `test_shared.py` |
| Hein Thura Naung - Ivan | IvannCoder | Shared `funded_account` fixture in `conftest.py` |

Why Git Could Not Automatically Resolve the Conflict

Because multiple collaborators edited the exact same lines of README.md concurrently, Git could not safely determine which version to keep without risking data loss, requiring us to resolve it manually

## 4. Git Contribution Summary

Output of `git shortlog -sn`:

```text
	15  6705140040
	 5  Chan Myae Thaw Tar
	 4  Aye Than Tin
	 3  6705140038
	 6  Hein Thura Naung (Ivan)
```


## 5. Reflection Questions

### 1. Why was your push rejected, and how did you fix it?
My push was rejected because another team member had pushed new changes to GitHub. I used `git pull` to get the latest changes, merged them with my local work, and then pushed again.

### 2. Why could Git not resolve the README conflict automatically?
Git could not resolve the README conflict automatically because different team members changed the same part of the README. Git needed us to decide which changes to keep and combine.

### 3. What is the difference between committing and pushing?
Committing saves our changes in the local Git repository. Pushing sends those commits from the local repository to the shared GitHub repository.

### 4. How do fixtures reduce duplicated setup code in tests?
Fixtures provide the setup code that tests need, so we do not have to write the same setup repeatedly in every test. For example, the `funded_account` fixture creates a `BankAccount(1000)` that can be used by multiple tests.

## GitHub Repository

https://github.com/6705140040/lab04-TeamX-Panda
