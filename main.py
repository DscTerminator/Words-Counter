def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path of the file: ")
    word_count = count_words(file_path)
    
    if word_count is not None:
        print(f"The file '{file_path}' contains {word_count} words.")

if __name__ == "__main__":
    main()
