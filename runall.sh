#!/bin/bash

docker run --rm \
  -v $(pwd):/project \
  -w /project \
  studytime \
  snakemake --cores 1