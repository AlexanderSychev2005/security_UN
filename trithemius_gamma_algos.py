import string
import random

ALPHABET = string.ascii_uppercase
N = len(ALPHABET)

sentences = [
    "Hello Anna! I'm fine, thank you. Arrived in Stockholm yesterday. The weather is great, but it's a bit cold. Looking forward to exploring the city and trying some local cuisine. See you soon!",
    "The sites are really beautiful, and the people are very friendly. I can't wait to share my experiences with you when I get back. Take care and talk to you soon!",
    "Just wanted to let you know that I arrived safely in Stockholm. The city is amazing, and I'm having a great time exploring it. The weather is a bit chilly, but it's perfect for sightseeing. I'll keep you updated on my adventures here!",
]


def get_char_index(char):
    return ALPHABET.find(char.upper())


def trithemius_cipher_lab(text, key_type, params, mode="encrypt"):
    result_text = ""

    current_char_idx = 0

    for char in text.upper():
        if char in ALPHABET:
            x = get_char_index(char)
            k = 0

            i = current_char_idx

            if key_type == "linear":
                # K = A*i + B
                A, B = params
                k = A * i + B

            elif key_type == "nonlinear":
                # K = A*i^2 + B*i + C
                A, B, C = params
                k = A * (i**2) + B * i + C

            elif key_type == "motto":
                # K = index of the motto letter
                motto = params.upper()
                k = get_char_index(motto[i % len(motto)])

            if mode == "encrypt":
                y = (x + k) % N
            else:
                y = (x - k) % N

            result_text += ALPHABET[y]
            current_char_idx += 1
        else:
            result_text += char  # Does not cipher punctuation

    return result_text


def gamma_cipher_lab(text, seed, mode="encrypt"):
    # Pseudo random generator
    random.seed(seed)
    result_text = ""
    gamma_sequence = []

    for char in text.upper():
        if char in ALPHABET:
            x = get_char_index(char)
            k = random.randint(0, N - 1)  # Generate the shift (gamma)
            gamma_sequence.append(k)

            if mode == "encrypt":
                y = (x + k) % N
            else:
                y = (x - k) % N
            result_text += ALPHABET[y]
        else:
            result_text += char

    return result_text, gamma_sequence


linear_params = (3, 5)  # A=3, B=5
nonlinear_params = (1, 2, 3)  # A=1, B=2, C=3
motto_key = "SECRET"  # Motto
gamma_seed = 42  # Seed for the generator, gamma key


for i, sentence in enumerate(sentences):
    print(f"Sentence: {i + 1}")
    print("Original sentence:", sentence)

    enc_lin = trithemius_cipher_lab(sentence, "linear", linear_params, "encrypt")
    dec_lin = trithemius_cipher_lab(enc_lin, "linear", linear_params, "decrypt")
    print(f"[Trithemius Linear] Enc: {enc_lin}\n")
    print(f"[Trithemius Linear] Dec: {dec_lin}\n")

    enc_non = trithemius_cipher_lab(sentence, "nonlinear", nonlinear_params, "encrypt")
    dec_non = trithemius_cipher_lab(enc_non, "nonlinear", nonlinear_params, "decrypt")
    print(f"[Trithemius NonLin] Enc: {enc_lin}\n")
    print(f"[Trithemius NonLin] Dec: {dec_lin}\n")

    enc_motto = trithemius_cipher_lab(sentence, "motto", motto_key, "encrypt")
    dec_motto = trithemius_cipher_lab(enc_motto, "motto", motto_key, "decrypt")
    print(f"[Trithemius Motto ] Enc: {enc_motto}\n")
    print(f"[Trithemius Motto] Dec: {dec_motto}\n")

    enc_gamma, gamma_seq = gamma_cipher_lab(sentence, gamma_seed, "encrypt")
    dec_gamma, _ = gamma_cipher_lab(enc_gamma, gamma_seed, "decrypt")
    print(f"[Gamma Cipher] Enc: {enc_gamma}\n")
    print(f"[Gamma Cipher] Dec: {dec_gamma}\n")

    print("")
