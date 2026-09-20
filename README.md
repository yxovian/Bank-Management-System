# Bank Management System (Python)

A simple command-line Bank Management System built in Python. It lets you create accounts, view them, search using binary search, deposit, withdraw, and delete accounts — all through an interactive text menu.

## Features

- **Create Account** — add a new account with ID, holder name, and initial balance
- **View Accounts** — list all stored accounts
- **Search Account** — binary search by account ID (accounts are sorted first)
- **Deposit** — add funds to an existing account
- **Withdraw** — remove funds, with an insufficient-balance check
- **Delete Account** — remove an account by ID

## Requirements

- Python 3.10 or later (the menu uses `match`/`case`, introduced in 3.10)

## How to Run

```bash
python BankSystem.py
```

Then follow the on-screen menu:

```
1. Create Account
2. View Accounts
3. Search Account
4. Deposit
5. Withdraw
6. Delete Account
7. Exit
```

## Notes & Known Limitations

- **No persistence**: all data is stored in memory and is lost when the program exits. Adding file or database storage (e.g. JSON, SQLite) would let data survive between runs.
- **No "not found" feedback**: searching, depositing, withdrawing, or deleting with an ID that doesn't exist fails silently instead of printing a message.
- **No duplicate ID check**: `create_account` doesn't verify that an ID isn't already in use.
- **No input validation**: entering non-numeric text for ID/amount fields will raise an exception and crash the program.
- **Inconsistent lookup strategy**: `search_account` uses binary search, while `deposit`, `withdraw`, and `delete_account` use a linear scan.

## Possible Improvements

- Wrap accounts in an `Account` class (and a `Bank` class to manage them) instead of plain dictionaries
- Add persistent storage (JSON file or SQLite database)
- Add try/except blocks around user input
- Add unit tests

## License

This project is currently unlicensed. Add a `LICENSE` file if you'd like to make reuse terms explicit.
