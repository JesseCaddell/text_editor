class TextOperation:
    def __init__(self, operation_type, character):
        self.operation_type = operation_type
        self.character = character

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []

    def addChar(self, character):
        self.text += character
        operation = TextOperation("add", character)
        self.undo_stack.append(operation)
        self.showText()


    def delLastChar(self):
        deletedChar = self.text[-1]
        operation = TextOperation("delete", deletedChar)
        self.undo_stack.append(operation)
        self.text = self.text[:-1]
        self.showText()


    def undo(self):
        if self.undo_stack:
            lastOperation = self.undo_stack.pop()
            if lastOperation.operation_type == "add":
                self.text = self.text[:-1]
            elif lastOperation.operation_type == "delete":
                self.text += lastOperation.character
            self.showText()

    def showText(self):
        print("Current Text:", self.text)

def main():
    editor = TextEditor()
    while True:
        print("\nOptions:")
        print("1. Add Text")
        print("2. Delete Last Character")
        print("3. Undo")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            character = input("Enter the character to add: ")
            editor.addChar(character)
        elif choice == "2":
            editor.delLastChar()
        elif choice == "3":
            editor.undo()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()