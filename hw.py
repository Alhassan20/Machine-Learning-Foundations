selected_words = ["awesome", "great", "fantastic", "amazing",
                  "love", "horrible", "bad", "terrible", "awful", "wow", "hate"]


def awesome_count:
  if "awesome" in products["word_count"]:
    return products["word_count"]["awesome"]
  else:
    return 0

products["awesome"] = products["word_count"].apply(awesome_count)
products["awesome"].sum()
