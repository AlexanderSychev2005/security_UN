import string


def ceasar_cipher_lab(text, key, mode="encrypt"):
    # English alphabet (26 letters)
    alphabet = string.ascii_uppercase
    n = len(alphabet)
    result_text = ""

    shifter_alphabet = alphabet[key % n :] + alphabet[: key % n]

    print(f"Key: {key}")
    print(f"Original alphabet: {alphabet}")
    print(f"Shifter alphabet: {shifter_alphabet}")

    for char in text.upper():
        if char in alphabet:
            x = alphabet.find(char)
            if mode == "encrypt":
                y = (x + key) % n
            else:
                y = (x - key) % n
            result_text += alphabet[y]
        else:
            result_text += char
    return result_text


sentences = [
    "Hello Anna! I'm fine, thank you. Arrived in Stockholm yesterday. The weather is great, but it's a bit cold. Looking forward to exploring the city and trying some local cuisine. See you soon!",
    "The sites are really beautiful, and the people are very friendly. I can't wait to share my experiences with you when I get back. Take care and talk to you soon!",
    "Just wanted to let you know that I arrived safely in Stockholm. The city is amazing, and I'm having a great time exploring it. The weather is a bit chilly, but it's perfect for sightseeing. I'll keep you updated on my adventures here!",
]

key = 5

for i, sentence in enumerate(sentences):
    print(f"Sentence: {i + 1}")
    print("Original sentence:", sentence)

    encrypted = ceasar_cipher_lab(sentence, key, mode="encrypt")
    print("Encrypted sentence:", encrypted)

    decrypted = ceasar_cipher_lab(encrypted, key, mode="decrypt")
    print("Decrypted sentence:", decrypted)
    print("")
