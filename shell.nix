with import <nixpkgs> {};

mkShell {
  buildInputs = [ python37 pipenv ];
}
