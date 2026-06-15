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

void splitSymptoms(const string& log, string symptoms[], int& count) {
    count = 0;
    string current = "";
    int len = stringLength(log);
    for (int i = 0; i < len; ++i) {
        if (log[i] == '-') {
            symptoms[count++] = current;
            current = "";
        } else {
            current += log[i];
        }
    }
    if (stringLength(current) > 0) {
        symptoms[count++] = current;
    }
}

bool searchSymptom(string symptoms[], int count, const string& target) {
    for (int i = 0; i < count; ++i) {
        if (symptoms[i] == target) return true;
    }
    return false;
}

string reverseSymptoms(string symptoms[], int count) {
    string reversed = "";
    for (int i = count - 1; i >= 0; --i) {
        reversed += symptoms[i];
        if (i > 0) reversed += "-";
    }
    return reversed;
}

bool checkRepeated(string symptoms[], int count) {
    for (int i = 0; i < count; ++i) {
        for (int j = i + 1; j < count; ++j) {
            if (symptoms[i] == symptoms[j]) return true;
        }
    }
    return false;
}

int main() {
    string log = "Fever-Cough-Fatigue-Headache-Fever";
    cout << "Original log: " << log << endl;
    
    string symptoms[100];
    int count = 0;
    splitSymptoms(log, symptoms, count);
    
    cout << "Total symptoms: " << count << endl;
    
    string critical = "Chest Pain";
    if (searchSymptom(symptoms, count, critical)) {
        cout << "Critical symptom " << critical << " found!" << endl;
    } else {
        cout << "Critical symptom " << critical << " not found." << endl;
    }
    
    cout << "Reversed order: " << reverseSymptoms(symptoms, count) << endl;
    
    if (checkRepeated(symptoms, count)) {
        cout << "There are repeated symptoms." << endl;
    } else {
        cout << "No repeated symptoms." << endl;
    }
    
    return 0;
}
