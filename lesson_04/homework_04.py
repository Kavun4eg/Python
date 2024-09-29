adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked .... 
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. .... 
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# Task 01
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# Task 02
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# Task 03
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())

# Task 04
count_h = adwentures_of_tom_sawer.count('h')

# Task 05
count_capitalized_words = sum(1 for word in adwentures_of_tom_sawer.split() if word[0].isupper())

# Task 06
second_tom_position = adwentures_of_tom_sawer.find("Tom", adwentures_of_tom_sawer.find("Tom") + 1)

# Task 07
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')

# Task 08
fourth_sentence_lower = adwentures_of_tom_sawer_sentences[3].lower() if len(adwentures_of_tom_sawer_sentences) > 3 else None

# Task 09
starts_with_by_the_time = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)

# Task 10
last_sentence_word_count = len(adwentures_of_tom_sawer_sentences[-1].split()) if adwentures_of_tom_sawer_sentences else 0