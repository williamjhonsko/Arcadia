
#### main.py

```python
#!/usr/bin/env python3
import random

ideas = [
    "Paint a surreal landscape inspired by dreams.",
    "Write a short story from the perspective of an inanimate object.",
    "Compose a piece of music using only natural sounds.",
    "Create a digital collage from vintage magazine clippings.",
    "Design a futuristic city using recycled materials."
]

def get_random_idea():
    return random.choice(ideas)

def main():
    print("Welcome to Arcadia Creative Ideas!")
    print("Here's a random creative idea for you:")
    print(get_random_idea())

if __name__ == "__main__":
    main()
