def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def reverse_sequence(s):
    rev = ""
    length = string_length(s)
    for i in range(length - 1, -1, -1):
        rev += s[i]
    return rev

def count_nucleotides(s):
    a = t = g = c = 0
    for char in s:
        if char == 'A': a += 1
        elif char == 'T': t += 1
        elif char == 'G': g += 1
        elif char == 'C': c += 1
    print(f"A: {a}, T: {t}, G: {g}, C: {c}")

def is_palindrome(s):
    length = string_length(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

def find_codon(s, codon):
    s_len = string_length(s)
    c_len = string_length(codon)
    
    for i in range(s_len - c_len + 1):
        match = True
        for j in range(c_len):
            if s[i + j] != codon[j]:
                match = False
                break
        if match:
            return i
    return -1

if __name__ == "__main__":
    dna = "ATGCGTAATCGCAT"
    print(f"Original DNA: {dna}")
    
    print(f"Reversed DNA: {reverse_sequence(dna)}")
    
    count_nucleotides(dna)
    
    if is_palindrome(dna):
        print("Sequence is a palindrome.")
    else:
        print("Sequence is not a palindrome.")
        
    codon = "TAA"
    pos = find_codon(dna, codon)
    if pos != -1:
        print(f"Codon {codon} found at position: {pos}")
    else:
        print(f"Codon {codon} not found.")
