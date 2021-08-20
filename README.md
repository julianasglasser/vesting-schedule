# Vesting Schedule CL

This project is a solution to Carta's take home exercise, which was building a command-line program that reads a file of vesting events and outputs a vesting schedule to `stdout`.

For this part of the challenge I chose to do the set up manually.

Because the challenge criteria mentioned the code had to handle large data sets robustly, I figured it would be a good solution if I used [pandas](https://pandas.pydata.org/docs/). Pandas is a very powerfull library to use with large data sets, even though it has its limittions. For the proposed problem I thought it would be enough performatic, because our file has few columns. But if we had a much larger data set, let's say more than 2GB, I would have chosen to use [Dask](https://dask.org/) instead, once it provides parallelism.

## Set up

```bash
pip install -r requirements.txt
python3 setup.py install
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
