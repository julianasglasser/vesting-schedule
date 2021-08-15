# Vesting Schedule CL

This a command-line program that reads a file of vesting events and outputs a vesting schedule to `stdout`.

## How to set up

```bash
pip install -r requirements.txt
```

## How to run

Along with the command to run, you should input at `stdin` two arguments. The first is the `filename` (including relative path when not in the same folder) and the second is a `target date`, which is the last date of interest.

```bash
python3 vesting.py [filename.csv] [YYYY-MM-DD]
```

**OR**

```bash
./vesting.py [filename.csv] [YYYY-MM-DD]
```

### Example

```bash
./vesting example.csv 2020-01-01
```
