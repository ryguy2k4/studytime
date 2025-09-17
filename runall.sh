#!/bin/bash

docker run --rm \
  -v $(pwd):/project \
  -w /project \
  ghcr.io/ryguy2k4/studytime \
  snakemake --cores 1