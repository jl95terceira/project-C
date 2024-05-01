Video game music webscraper / downloader

# Get started

Install:
<ul>
  <li>Python ≥ <b>3.12</b>
  <li>Python package <code>beautifulsoup4</code>, installed via <code>pip install beautifulsoup4</code></li>
</ul>


To run <code>music.py</code>, call

```
python music.py ...
```

or, if you set <code>.py</code> files to open with Python by default, simply call

```
music.py ...
```

The script takes positional and optional arguments. For help, call the script with option <code>-h</code> like so.

```
music.py -h
```

Help text:

```
usage: music.py [-h] [--dir DIR] url

Download music from https://downloads.khinsider.com/

Please, do NOT abuse this tool to mass-download content from the site. Be kind.

positional arguments:
  url         URL of the album to download

options:
  -h, --help  show this help message and exit
  --dir DIR   directory to which to download the album
              Defaults to C:\Users\jl95\Music\Video Game Music.
```
