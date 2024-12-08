def write_utf8_to_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Successfully wrote content to {filename}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

filename = input("Enter the filename to write to (including extension): ")
print("Enter the content to write (press Ctrl+D on Unix or Ctrl+Z on Windows and then Enter to finish):")
content_lines = []
while True:
    try:
        line = input()
        content_lines.append(line)
    except EOFError:
        break

content = '\n'.join(content_lines)

write_utf8_to_file(filename, content)