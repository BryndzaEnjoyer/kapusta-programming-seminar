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

print(listdir())

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
    seq_set = set(seq.upper())

    dna_set = set("ATCG")
    rna_set = set("AUCG")
    protein_set = set("ACDEFGHIKLMNPQRSTVWY")

    if seq_set.issubset(dna_set):
        return "DNA"
    elif seq_set.issubset(rna_set):
        return "RNA"
    elif seq_set.issubset(protein_set):
        return "Protein"
    else:
        return "Unknown"


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



# -----------------------------
# Local sequence alignment
# -----------------------------

def local_alignment(seq_a, seq_b, match=1, mismatch=-1, gap=-1):
    """
    Perform local sequence alignment (Smith–Waterman).

    Args:
        seq_a (str): First sequence
        seq_b (str): Second sequence

    Returns:
        tuple: best score, aligned seq_a, aligned seq_b
    """
    len_a = len(seq_a)
    len_b = len(seq_b)

    score = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    max_score = 0
    max_pos = (0, 0)

    # fill matrix
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            diag = score[i-1][j-1] + (match if seq_a[i-1] == seq_b[j-1] else mismatch)
            up = score[i-1][j] + gap
            left = score[i][j-1] + gap
            score[i][j] = max(0, diag, up, left)

            if score[i][j] > max_score:
                max_score = score[i][j]
                max_pos = (i, j)

    # traceback
    aligned_a = ""
    aligned_b = ""
    i, j = max_pos

    while score[i][j] != 0:
        if score[i][j] == score[i-1][j-1] + (match if seq_a[i-1] == seq_b[j-1] else mismatch):
            aligned_a = seq_a[i-1] + aligned_a
            aligned_b = seq_b[j-1] + aligned_b
            i -= 1
            j -= 1
        elif score[i][j] == score[i-1][j] + gap:
            aligned_a = seq_a[i-1] + aligned_a
            aligned_b = "-" + aligned_b
            i -= 1
        else:
            aligned_a = "-" + aligned_a
            aligned_b = seq_b[j-1] + aligned_b
            j -= 1

    return max_score, aligned_a, aligned_b

# -----------------------------
# Global sequence alignment
# -----------------------------


def global_alignment(seq_a, seq_b, match=1, mismatch=-1, gap=-1):
    """
    Perform global sequence alignment (Needleman–Wunsch).

    Args:
        seq_a (str): First sequence
        seq_b (str): Second sequence
        match (int): Score for a match
        mismatch (int): Score for a mismatch
        gap (int): Score for a gap

    Returns:
        tuple: alignment score, aligned seq_a, aligned seq_b
    """
    len_a = len(seq_a)
    len_b = len(seq_b)

    # scoring matrix
    score = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    # initialize first row and column
    for i in range(len_a + 1):
        score[i][0] = i * gap
    for j in range(len_b + 1):
        score[0][j] = j * gap

    # fill matrix
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            diag = score[i-1][j-1] + (match if seq_a[i-1] == seq_b[j-1] else mismatch)
            up = score[i-1][j] + gap
            left = score[i][j-1] + gap
            score[i][j] = max(diag, up, left)

    # traceback
    aligned_a = ""
    aligned_b = ""
    i, j = len_a, len_b

    while i > 0 or j > 0:
        current = score[i][j]
        if i > 0 and j > 0 and current == score[i-1][j-1] + (match if seq_a[i-1] == seq_b[j-1] else mismatch):
            aligned_a = seq_a[i-1] + aligned_a
            aligned_b = seq_b[j-1] + aligned_b
            i -= 1
            j -= 1
        elif i > 0 and current == score[i-1][j] + gap:
            aligned_a = seq_a[i-1] + aligned_a
            aligned_b = "-" + aligned_b
            i -= 1
        else:
            aligned_a = "-" + aligned_a
            aligned_b = seq_b[j-1] + aligned_b
            j -= 1

    return score[len_a][len_b], aligned_a, aligned_b

print("\nGLOBAL ALIGNMENT:")
g_score, g_a, g_b = global_alignment(seq_a, seq_b)
print("Score:", g_score)
print(g_a)
print(g_b)

print("\nLOCAL ALIGNMENT:")
l_score, l_a, l_b = local_alignment(seq_a, seq_b)
print("Score:", l_score)
print(l_a)
print(l_b)
