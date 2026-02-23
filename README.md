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

e.g.
```console
❯ nix run github:jeffbr13/grab-cookies -- safari patreon.com
/var/folders/pl/b80kgl_j0v5fq1ds49srk0d00000gn/T/tmpndg72mwi.txt
INFO: Cookies for patreon.com extracted from safari to: /var/folders/pl/b80kgl_j0v5fq1ds49srk0d00000gn/T/tmpndg72mwi.txt

Usage: gallery-dl --cookies '/var/folders/pl/b80kgl_j0v5fq1ds49srk0d00000gn/T/tmpndg72mwi.txt' <URL>
```

## Development

### Run via local Nix Flake
```shell
nix run . -- --help
nix run . -- <browser> <domain>
```