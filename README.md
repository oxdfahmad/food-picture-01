# Steaming Tonkotsu Ramen — food-picture-01

A steaming bowl of tonkotsu ramen: chopsticks lifting glossy noodles,
a soft-boiled egg, chashu and spring onions in warm window light.

## Entry

- `main.py` — Python 3.13, standard library only. Copies `entry.png`
  byte for byte to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`
  in the grader container). Deterministic: both runs write identical bytes.
- `entry.png` — the picture (JPEG bytes, 1024×1024, 354,173 bytes;
  under the 1 MiB / 1024×1024 gate limits).
- `LICENSE` — MIT.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Source image

The original 1600×1600 render is kept beside the entry as
`media-generation-entry-0-5ffa099d-297d-48b1-9ab9-324b96e90495.png`
for reference; only `entry.png` is shipped by the program.
