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


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_each_letter(file_contents))


main()
