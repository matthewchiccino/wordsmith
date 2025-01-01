def process_word_vectors(input_file, output_file):
    i = 0
    with open(input_file, "r", encoding="utf-8", errors="ignore") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            parts = line.split()

            word = parts[0]  # The word is the first item in the line
            vector = parts[1:]  # The rest are vector components

            # Exclude words that start with an integer or contain a hyphen
            if not word[0].isdigit() and '-' not in word: 
                # Write the word and its vector to the output file
                outfile.write(" ".join([word] + vector) + "\n")
                i += 1

            if i > 40000:
                break

# Specify the input and output file paths
input_file = "word_vecs_100d.txt"  # Replace with the actual input file path
output_file = "final_word_vecs_100d.txt"  # Replace with desired output file path

# Call the function to process the file
process_word_vectors(input_file, output_file)

print(f"Filtered file saved as: {output_file}")
