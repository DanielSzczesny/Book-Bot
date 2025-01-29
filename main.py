def count_words(text):
    result = text.split()
    return len(result)


def count_each_letter(text):
    text_lowercase = text.lower()
    result = {}
    for i in range(0, len(text_lowercase)):
        if text_lowercase[i] in result:
            result[text_lowercase[i]] += 1
        else:
            result[text_lowercase[i]] = 1
    return result


def sort_on(dictionary):
    return dictionary["num"]


def count_each_alpha_char(text):
    text_lowercase = text.lower()
    result = []
    for i in range(0, len(text_lowercase)):
        if text_lowercase[i].isalpha():
            if len(result) == 0:
                result.append({"letter": text_lowercase[i], "num": 1})
            else:
                added = False
                for j in range(0, len(result)):
                    if text_lowercase[i] == result[j]["letter"]:
                        result[j]["num"] += 1
                        added = True
                        break
                if not added:
                    result.append({"letter": text_lowercase[i], "num": 1})
    return result


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        sorted_dict = count_each_alpha_char(file_contents)
        sorted_dict.sort(reverse=True, key=sort_on)
        print(sorted_dict)


main()
