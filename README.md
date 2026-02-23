grab-cookies
============

Extract browser cookies into a Netscape-format cookies.txt file.

## Usage

```shell
nix run github:jeffbr13/grab-cookies -- <browser> <domain>
```
## Development

### Run via local Nix Flake
```shell
nix run . -- --help
nix run . -- <browser> <domain>
```