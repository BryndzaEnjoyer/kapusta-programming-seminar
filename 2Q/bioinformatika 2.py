from urllib.request import urlretrieve
#Save the looooong web address (url) of our data in a python string 
genome_url = 'https://cloud-9.edupage.org/cloud?z%3AlUKCQ408Z9xiCKqALXOfGpA6rU2teZRYyO4snphTty6VKCjFsZszvqL7rgmStRFVX98gR4ay0kvq2MapTqANWg%3D%3D'
genome_url2 =  "https://cloud-9.edupage.org/cloud?z%3A9wJf2ysqomhDFldrz8nkSEyqq1kbN4KZf8ZMIVJbxowuGfVHFBpAqrsVSg902xWbxxEVGINOIfvKXggt9pZWhA%3D%3D"
genome_url3 = "https://cloud-4.edupage.org/cloud?z%3AdJJBkScGEVK6wa5b%2B96Ocf0c8GpaEJLOqN4uxahRVyPrVvbF%2FqMxXIw5zWr2rJDQQQBZnRuKSqEyPi%2BljOVVlw%3D%3D"
#Set the name of the file where we want to save the data
genome_file_name = 'Human_FMR1_Protein_UniProt.fasta'

#Download the data 
result = urlretrieve(genome_url, genome_file_name)
infile = open('Human_FMR1_Protein_UniProt.fasta')
for line in infile:
    print(line)




def biomiofeo():
    species = {
    "species_one": "CACTACAGATGGTGAATATCTCCCTGCGAGTGTTGTCTCGACCCAATGCTCAGGAGCTTCCTAGCATGTACCAGCGCCTAGGGCTGGACTACGAGGAACGAGTGTTGCCGTCCATTGTCAACGAGGTGCTCAAGAGTGTGGTGGCCAAGTTCAATGCCTCACAGCTGATCACCCAGCGGGCCCAG",
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
    return check, species
def yucky(check ,species):
    catg={}
    count=0
    for x in check: 
        for i in species.values():
            count+=i.count(x)
        print(x,count)
check, species = biomiofeo()
yucky(check, species)