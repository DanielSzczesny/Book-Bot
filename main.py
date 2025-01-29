
def count_words(text):
    result = text.split()
    return len(result)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

main()