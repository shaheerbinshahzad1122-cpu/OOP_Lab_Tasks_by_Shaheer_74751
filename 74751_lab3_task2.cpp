#include <iostream>
#include <string>

using namespace std;

int stringLength(const string& str) {
    int len = 0;
    while (str[len] != '\0') {
        len++;
    }
    return len;
}

string reverseSequence(const string& str) {
    string rev = str;
    int len = stringLength(str);
    for (int i = 0; i < len / 2; ++i) {
        char temp = rev[i];
        rev[i] = rev[len - 1 - i];
        rev[len - 1 - i] = temp;
    }
    return rev;
}

void countNucleotides(const string& str) {
    int a = 0, t = 0, g = 0, c = 0;
    int len = stringLength(str);
    for (int i = 0; i < len; ++i) {
        if (str[i] == 'A') a++;
        else if (str[i] == 'T') t++;
        else if (str[i] == 'G') g++;
        else if (str[i] == 'C') c++;
    }
    cout << "A: " << a << ", T: " << t << ", G: " << g << ", C: " << c << endl;
}

bool isPalindrome(const string& str) {
    int len = stringLength(str);
    for (int i = 0; i < len / 2; ++i) {
        if (str[i] != str[len - 1 - i]) return false;
    }
    return true;
}

int findCodon(const string& str, const string& codon) {
    int strLen = stringLength(str);
    int codonLen = stringLength(codon);
    
    for (int i = 0; i <= strLen - codonLen; ++i) {
        bool match = true;
        for (int j = 0; j < codonLen; ++j) {
            if (str[i + j] != codon[j]) {
                match = false;
                break;
            }
        }
        if (match) return i;
    }
    return -1;
}

int main() {
    string dna = "ATGCGTAATCGCAT";
    cout << "Original DNA: " << dna << endl;
    
    cout << "Reversed DNA: " << reverseSequence(dna) << endl;
    
    countNucleotides(dna);
    
    if (isPalindrome(dna)) cout << "Sequence is a palindrome." << endl;
    else cout << "Sequence is not a palindrome." << endl;
    
    string codon = "TAA";
    int pos = findCodon(dna, codon);
    if (pos != -1) cout << "Codon " << codon << " found at position: " << pos << endl;
    else cout << "Codon " << codon << " not found." << endl;
    
    return 0;
}
