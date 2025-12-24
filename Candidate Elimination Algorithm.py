# Candidate Elimination Algorithm (Simple Version)

def candidate_elimination(data, labels):

    # Step 1: Initialize S and G
    S = ["Ø"] * len(data[0])          # Most specific hypothesis
    G = [["?"] * len(data[0])]        # Most general hypothesis

    # Step 2: Process each training example
    for i in range(len(data)):

        example = data[i]

        if labels[i] == "Yes":  # POSITIVE example
            for j in range(len(S)):
                if S[j] == "Ø":
                    S[j] = example[j]
                elif S[j] != example[j]:
                    S[j] = "?"

        else:  # NEGATIVE example
            new_G = []
            for g in G:
                for j in range(len(S)):
                    if g[j] == "?" and S[j] != example[j]:
                        temp = g.copy()
                        temp[j] = S[j]
                        new_G.append(temp)
            G = new_G

        # Display step-by-step result
        print(f"\nAfter example {i+1}")
        print("S =", S)
        print("G =", G)

    return S, G
data = [
    ["Sunny", "Warm", "Normal", "Strong"],
    ["Sunny", "Warm", "High", "Strong"],
    ["Rainy", "Cold", "High", "Strong"]
]

labels = ["Yes", "Yes", "No"]

S, G = candidate_elimination(data, labels)

print("\nFinal Result")
print("Specific Hypothesis (S):", S)
print("General Hypothesis (G):", G)
