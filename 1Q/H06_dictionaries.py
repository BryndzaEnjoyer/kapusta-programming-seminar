def capital_excercise():
    capitals = {"India": "New delhi", "Pakistan": "Islamabad", "Albania" : "Tirana"}
    for key in capitals:
        print(key)
    for value in capitals:
        print(capitals[value])

    for key in capitals:
        if key == "Germany":
            print("Germany found")
    for key in capitals:
        print(f"The capital of {key} is {capitals[key]}.")
def students_excercise():
    students = {
    "Alice": {"age": 16, "grade": "A"},
    "Bob": {"age": 17, "grade": "B"}}
    print(students["Bob"]["grade"])
    students["Charlie"]={"age": 15, "grade": "A"}
    students["Alice"]["grade"] = "A+"
    for i in students:
        print(i,students[i]["grade"])
#students_excercise()
def counting():
    sen = "the cat and the dog"
    jozef = sen.split(" ")
    wordcounter = {}
    for i in jozef:
        wordcounter[i] = wordcounter.get(i, 0) + 1
    print(wordcounter)

#counting()
def biomiofeo():
    species = {
    "species_one": "ACCTACAGATGGTGAATATCTCCCTGCGAGTGTTGTCTCGACCCAATGCTCAGGAGCTTCCTAGCATGTACCAGCGCCTAGGGCTGGACTACGAGGAACGAGTGTTGCCGTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAATGCCTCACAGCTGATCACCCAGCGGGCCCAG",
    "species_two": "ATGGTGAACATCTCCCTGCGGGTGCTGTCCCGACCCAATGCCATGGAGCTGCCCAGCATGTACCAGCGCCTGGGGCTGGACTACGAGGAGCGAGTGCTGCCGTCCATTGTCAACGAGGTGCTCAAGAGCGTGGTGGCCAAGTTCAACGCCTCCCAGCTGATCACTCAACGGGCCCAG",
    "species_three": "ACCTGCAGATGGTGAACATCTCCCTGCGGGTGCTGTCCCGACCCAACGCCATGGAGCTGCCCAGCATGTACCAGCGCCTGGGGCTGGACTATGAGGAGCGAGTGCTGCCCTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAACGCCTCCCAGCTGATCACCCAGCGGGCCCAG",
    "species_four": "ACCTGCAGATGGTGAACATCTCCCTGCGCGTCCTCACCCGCCCCAATGCTGCAGAGCTGCCCAGCATGTATCAGCGCCTGGGCCTGGACTACGAGGAGCGAGTCCTGCCCTCCATCGTCAACGAGGTGCTCAAGAGCGTGGTGGCCAAATTCAACGCCTCGCAGCTCATCACACAGAGAGCCCAG"}
    check=[]
    for i in species:
        r=species[i]
        for q in r:
            if q not in check:
                check.append(q)
    print(check)
    def yucky():
        catg={}
        for i in species:
            catg[i] = catg.get(i, 0) + 1
        print(catg)
        #fuck you(just do it, jump of the bridge)
biomiofeo()          