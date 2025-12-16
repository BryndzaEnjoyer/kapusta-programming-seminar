from urllib.request import urlretrieve
from collections import Counter
from os import listdir

# -----------------------------
# Download FASTA file
# -----------------------------
genome_url = (
    'https://cloud-4.edupage.org/cloud?z%3AdJJBkScGEVK6wa5b%2B96Ocf0c8GpaEJLOqN4uxahRVyPrVvbF%2FqMxXIw5zWr2rJDQQQBZnRuKSqEyPi%2BljOVVlw%3D%3D'
)
fasta_filename = 'sequences.fasta'
urlretrieve(genome_url, fasta_filename)

print(listdir()) # Check downloaded files

# -----------------------------
# FASTA reading
# -----------------------------
def load_fasta(file_path):
    """
    Read a FASTA file and store sequences in a dictionary.

    Args:
        file_path (str): Path to FASTA file.

    Returns:
        dict: Dictionary mapping headers to sequences.
    """
    sequences = {}
    current_header = None
    current_sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_header is not None:
                    sequences[current_header] = current_sequence
                current_header = line[1:]
                current_sequence = ""
            else:
                current_sequence += line

        if current_header is not None:
            sequences[current_header] = current_sequence

    return sequences


fasta_sequences = load_fasta(fasta_filename)
print(fasta_sequences.keys())

# -----------------------------
# Character counting
# -----------------------------
def count_sequence_characters(seq):
    """
    Count characters in a biological sequence.

    Args:
        seq (str): DNA, RNA, or protein sequence.

    Returns:
        tuple:
            - Counter of characters
            - Number of unique characters
    """
    char_counts = Counter(seq)
    unique_chars = len(char_counts)
    return char_counts, unique_chars


for header, sequence in fasta_sequences.items():
    counts, unique = count_sequence_characters(sequence)
    print("\n", header)
    print("Counts:", counts)
    print("Unique characters:", unique)

# -----------------------------
# Sequence type detection
# -----------------------------
def identify_sequence_type(seq):
    """
    Detect whether a biological sequence is DNA, RNA, or protein.

    Args:
        seq (str): Biological sequence.

    Returns:
        str: 'DNA', 'RNA', 'Protein', or 'Unknown'
    """

    seq = seq.upper()
  
    if set(seq) <= {"A", "T", "C", "G"}:
        return "DNA"
    elif set(seq) <= {"A", "U", "C", "G"}:
        return "RNA"
    elif set(seq) <=  {'S', 'L', 'D', 'W', 'V', 'M', 'Q', 'K', 'R', 'G', 'Y', 'A', 'T', 'N', 'P', 'C', 'H', 'F', 'E', 'I'}:
        return "Protein"
    else: 
        return "Unknown sequence type/incorect characters present"

for header, sequence in fasta_sequences.items():
    print(header, "→", identify_sequence_type(sequence))

# -----------------------------
# Sequence identity analysis
# -----------------------------
seq_a = "ATATCGCGGCGCGCTTACGATGCTACGTCGCGGCGGGGTATATTAGCGGGATTC"
seq_b = "ATATCGCGGCGCCCTTACGATGCTACGTCGCGGCGCGGTATATTAGCGGGATACA"

def sequence_identity(seq1, seq2):
    """
    Calculate sequence identity between two sequences.

    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.

    Returns:
        dict: Statistics about identity and mismatches.
    """
    same_count = 0
    diff_count = 0
    mismatch_pairs = []

    for a, b in zip(seq1, seq2):
        if a == b:
            same_count += 1
        else:
            diff_count += 1
            mismatch_pairs.append((a, b))

    identity_percent = same_count / min(len(seq1), len(seq2)) * 100

    pair_counter = Counter(mismatch_pairs)
    most_common_pair, count = pair_counter.most_common(1)[0]

    return {
        "same_nucleotides": same_count,
        "different_nucleotides": diff_count,
        "mismatch_pairs": mismatch_pairs,
        "identity_percentage": f"{identity_percent:.2f}%",
        "most_common_pair": f"{most_common_pair} occurs {count} times"
    }

# -----------------------------
# Dinucleotide analysis
# -----------------------------
def analyze_dinucleotides(seq):
    """
    Perform dinucleotide frequency analysis on a DNA sequence.

    Args:
        seq (str): DNA sequence.

    Returns:
        Counter: Dinucleotide counts.
    """
    seq = seq.upper()
    dinucleotide_list = []

    for i in range(len(seq) - 1):
        dinucleotide_list.append(seq[i:i+2])

    return Counter(dinucleotide_list)


for header, sequence in fasta_sequences.items():
    if identify_sequence_type(sequence) == "DNA":
        print("\nDinucleotide analysis for:", header)

        dinuc_counts = analyze_dinucleotides(sequence)
        print("Total dinucleotides:", sum(dinuc_counts.values()))
        print("Most common dinucleotides:", dinuc_counts.most_common(10))
        print("CG count:", dinuc_counts.get("CG", 0))

print("\nSeq1 dinucleotides:", analyze_dinucleotides(seq_a).most_common(5))
print("Seq2 dinucleotides:", analyze_dinucleotides(seq_b).most_common(5))

print("\nSequence identity results:")
print(sequence_identity(seq_a, seq_b))
