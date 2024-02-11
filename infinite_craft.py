import requests
import json
import itertools

def combine(elem):
	url = "https://neal.fun/api/infinite-craft/pair"
	params = {
		"first": elem[0],
		"second": elem[1]
	}
	headers = {
		"Referer": "https://neal.fun/infinite-craft/",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
	}

	response = requests.get(url, params=params, headers=headers)

	if response.status_code == 200:
		output = json.loads(response.text)
		return output
	else:
		print(response.status_code)
		return None

def main():
	print("Starting, press CTRL+C to stop")
	cycle = 0
	includeDuplicates = False

	emojis = {"Water": "💧", "Fire": "🔥", "Wind": "🌬️", "Earth": "🌍"}

	with open("craft_result.json", "w+", encoding="utf-8") as f:
		current = ["Water", "Fire", "Wind", "Earth"]
		while True:
			cycle += 1

			combinations = list(itertools.combinations_with_replacement(current, 2))
			print(f"Cycle {cycle} ({len(combinations)} combinations)")
			for combination in combinations:
				print(f"[{combinations.index(combination)+1}/{len(combinations)}]", end="\r")
				result = combine(combination)
				if result is None:
					print("skip")
					continue
				presence = result["result"] not in current
				
				if includeDuplicates or presence:
					emojis[result["result"]] = result["emoji"]
					text = f"{emojis[combination[0]]} {combination[0]} + {emojis[combination[1]]} {combination[1]} -> {result['emoji']} {result['result']}{' (NEW)' if result['isNew'] else ''}\n"
					f.write(text)

				if presence:
					current.append(result["result"])

if __name__ == "__main__":
	main()
