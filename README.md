# Vesting Schedule CL

This project is a solution to Carta's take home exercise, which was building a command-line program that reads a file of vesting events and outputs a vesting schedule to `stdout`.

For this part of the challenge I chose to do the set up manually.

Because the challenge criteria mentioned the code had to handle large data sets robustly, I figured it would be a good solution if I used [pandas](https://pandas.pydata.org/docs/). Pandas is a very powerfull library to use with large data sets, even though it has its limittions. For the proposed problem I thought it would be enough performatic, because our file has few columns. But if we had a much larger data set, let's say more than 2GB, I would have chosen to use [Dask](https://dask.org/) instead, once it provides parallelism.

Since the project is very simple, and also because of the time constraints, I didn't see the need to use a `venv` nor `docker`. It has few dependencies and the set up is very simple.

## Set up

Before running you should make sure you have `python3` and `pip` installed.

```bash
pip install -r requirements.txt
python3 setup.py install
```

## Available Scripts

### To run tests

```bash
pip install -r requirements.txt
python3 tests/tests.py
```

### To run the app

Along with the command to run, you should input at `stdin` two arguments. The first is the `filename` (including relative path when not in the same folder) and the second is a `target date`, which is the last date of interest.

```bash
python3 setup.py install
python3 vesting.py [filename.csv] [YYYY-MM-DD]
```

## Example

This is an example of how to run:

```bash
python3 vesting.py vesting_events.csv 2021-04-01
```

This is an example of response:

```bash
E001,Alice Smith,ISO-001,2000
E001,Alice Smith,ISO-002,800
E002,Bobby Jones,NSO-001,600
E003,Cat Helms,NSO-002,0
```

## License

Distributed under the MIT license. See `LICENSE` for more information.

## Contributing

1. Fork it (https://github.com/yourname/yourproject/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request
