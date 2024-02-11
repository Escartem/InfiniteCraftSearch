# InfiniteCraftSearch
Automatically find every possible combination in Infinite Craft game

## How to use

Simply run the file `python infinite_craft.py`, and it will start trying every combination and writing them in a file called `craft_result.json` (the content in it is not actual json).
At line 28, you can change the variable to `True` if you want to include multiple combinations for the same result.

## Known issues

- You can get easily rate limited by the API, using a proxy list may be a workaround
- With the number of combinations it can take a lot of time to try everything, using threading may make this faster

---

### This is just a proof of concept, if you have any ideas, or if you want to propose updates you've made, just open an issue or do a pull request :)
