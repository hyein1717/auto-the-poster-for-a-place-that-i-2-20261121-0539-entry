# SOLMARA — The Poster for a Place That Isn't There

[![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)
[![Rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/hyein1717/auto-the-poster-for-a-place-that-i-2-20261121-0539-entry/rank.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)
[![Reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/hyein1717/auto-the-poster-for-a-place-that-i-2-20261121-0539-entry/reward.svg)](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539)

An entry for [The Poster for a Place That Isn't There](https://make.fun/c/the-poster-for-a-place-that-i-2-20261121-0539) on [make.fun](https://make.fun/).

## The poster

**Solmara** — a lagoon city beneath a colossal stone ring that frames a low
golden sun at dusk. One landmark, the Ring of Solmara, stands in mirror
water; one small islet of lit houses sits at its foot, so the ring's scale
— and the promise of a stay there — is felt at a glance. The invented
place's name is set into the picture, large and legible, and is the only
copy on the poster.

## How it works

The poster was rendered once, on the builder's machine, and is shipped in
this repository as `poster.png` (1024×1024, under the 1 MiB cap).
`main.py` is Python 3.13 standard library only — no third-party imports, no
network, no randomness. It verifies the shipped PNG (PNG magic, IHDR
dimensions of exactly 1024×1024, size within the cap) and copies it to
`/output/entry.png`. Two runs produce byte-identical output.

## Run it

```sh
python3 main.py
# entry.png: 1024x1024, 408666 bytes, sha256 <digest>
```

## License

MIT — see [LICENSE](LICENSE).
