grab-cookies
============

Extract browser cookies into a Netscape-format cookies.txt file.
Prints out the path of a temporary file containing the cookies.

This CLI is a wrapper around [yt-dlp](https://github.com/yt-dlp/yt-dlp)'s
[`--cookies-from-browser` functionality](https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-pass-cookies-to-yt-dlp)
to expose it as a generic CLI command.

## Usage

```shell
nix run github:jeffbr13/grab-cookies -- <browser> <domain>
```

```$
nix run github:jeffbr13/grab-cookies -- --help
```

```
usage: grab-cookies [-h]
                    {brave,chrome,chromium,edge,firefox,opera,safari,vivaldi,whale}
                    domain

Extract browser cookies for a given website into a Netscape-format cookies.txt
file which e.g. gallery-dl or other programs can use to authenticate to a
website. Uses yt-dlp's cookies functionality to extract browser cookies.
Safari requires 'Full Disk Access' for the terminal you're running this script
in. Outputs path of cookies.txt file to stdout.

positional arguments:
  {brave,chrome,chromium,edge,firefox,opera,safari,vivaldi,whale}
                        The browser to extract cookies from
  domain                The domain to extract cookies for (e.g. patreon.com)

options:
  -h, --help            show this help message and exit
```

e.g.
```console
❯ nix run github:jeffbr13/grab-cookies -- safari patreon.com
/var/folders/pl/b80kgl_j0v5fq1ds49srk0d00000gn/T/tmpndg72mwi.txt
INFO: Cookies for patreon.com extracted from safari to: /var/folders/pl/b80kgl_j0v5fq1ds49srk0d00000gn/T/tmpndg72mwi.txt

Usage: gallery-dl --cookies '/var/folders/pl/b80kgl_j0v5fq1ds49srk0d00000gn/T/tmpndg72mwi.txt' <URL>
```


## Development

### devenv
Uses [Devenv](https://devenv.sh) and [direnv](https://direnv.net) to manage developer environment.
See [`devenv.nix`](devenv.nix) for definition.

### Run via local Nix Flake
```shell
nix run . -- --help
nix run . -- <browser> <domain>
```