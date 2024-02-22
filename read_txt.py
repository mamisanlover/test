import re
checkpoint = r'[0-9][0-9]\.[0-9][0-9]\(.\)'
answer_candidate = ["◯", "△", "✕"]
with open("回答状況.txt", "r") as t:
	text = t.read()
raw = text.split("\n")[1:]
removed_raw = [r for r in raw if r not in ["次へ", "", "前へ"]]

month = int("".join(list(removed_raw[0])[0:2]))
days = []
answers_list = []
people_list = []
for sentence in removed_raw:
	if re.fullmatch(checkpoint, sentence) is not None:
		days.append(int("".join(list(sentence)[3:5])))
	elif sentence in answer_candidate:
		answers_list.append(sentence)
	else:
		if len(days) == 1:
			people_list.append(sentence)
input_lists = [[people] for people in people_list]
for i in range(len(answers_list)):
	input_lists[i % len(people_list)].append(answers_list[i])
need_people = [3 for i in range(len(days))]
people_num = len(people_list)


