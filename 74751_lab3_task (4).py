def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def split_symptoms(log):
    symptoms = []
    current = ""
    for char in log:
        if char == '-':
            symptoms.append(current)
            current = ""
        else:
            current += char
    if string_length(current) > 0:
        symptoms.append(current)
    return symptoms

def search_symptom(symptoms, target):
    for sym in symptoms:
        if sym == target:
            return True
    return False

def reverse_symptoms(symptoms):
    reversed_log = ""
    count = string_length(symptoms)
    for i in range(count - 1, -1, -1):
        reversed_log += symptoms[i]
        if i > 0:
            reversed_log += "-"
    return reversed_log

def check_repeated(symptoms):
    count = string_length(symptoms)
    for i in range(count):
        for j in range(i + 1, count):
            if symptoms[i] == symptoms[j]:
                return True
    return False

if __name__ == "__main__":
    log = "Fever-Cough-Fatigue-Headache-Fever"
    print(f"Original log: {log}")
    
    symptoms = split_symptoms(log)
    print(f"Total symptoms: {string_length(symptoms)}")
    
    critical = "Chest Pain"
    if search_symptom(symptoms, critical):
        print(f"Critical symptom {critical} found!")
    else:
        print(f"Critical symptom {critical} not found.")
        
    print(f"Reversed order: {reverse_symptoms(symptoms)}")
    
    if check_repeated(symptoms):
        print("There are repeated symptoms.")
    else:
        print("No repeated symptoms.")
