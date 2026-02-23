{
  description = "Extract browser cookies into a Netscape-format cookies.txt file";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python3;

        grab-cookies = python.pkgs.buildPythonApplication {
          pname = "grab-cookies";
          version = "0.1.0";
          pyproject = true;

          src = ./.;

          nativeBuildInputs = [
            python.pkgs.setuptools
          ];

          propagatedBuildInputs = [
            pkgs.yt-dlp
          ];

          meta = with pkgs.lib; {
            description = "Extract browser cookies for a given website into a Netscape-format cookies.txt file";
            homepage = "https://github.com/jeffbr13/grab-cookies";
            license = licenses.agpl3Plus;
            maintainers = [];
          };
        };
      in {
        packages.default = grab-cookies;
        apps.default = flake-utils.lib.mkApp {drv = grab-cookies;};

        devShells.default = pkgs.mkShell {
          inputsFrom = [grab-cookies];
          packages = [pkgs.uv];
        };
      }
    );
}
