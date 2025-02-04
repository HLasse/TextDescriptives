import random
import string
import numpy as np
import spacy


def simple_fuzzer(max_length: int = 100) -> str:
  """
  Generates a random string with potential spaces to create multiple tokens.

  Args:
    max_length: The maximum length of the string.

  Returns:
    A randomly generated string.
  """
  letters = string.ascii_letters
  # Introduce spaces with a probability
  chars = letters + " " 
  return ''.join(random.choice(chars) for _ in range(random.randint(0, max_length)))

def test_token_length_with_fuzzer(nlp, num_tests: int = 1000):
    """
    Tests the token_length function using randomized inputs.

    Args:
        nlp: A spaCy language object.
        num_tests: Number of fuzzing tests to perform.
    """
    for _ in range(num_tests):
        fuzzed_input = simple_fuzzer()  # Generate a random string using the simple_fuzzer
        doc = nlp(fuzzed_input)
        try:
            token_lengths = [len(token) for token in doc]  # Simplified token_length calculation
            mean_length = np.mean(token_lengths)
            median_length = np.median(token_lengths)
            std_dev = np.std(token_lengths)
            print(f"Input: {fuzzed_input}")
            print(f"Mean Token Length: {mean_length}")
            print(f"Median Token Length: {median_length}")
            print(f"Standard Deviation: {std_dev}\n")
        except Exception as e:
            print(f"Error processing input: {fuzzed_input}\nException: {e}\n")

if __name__ == "__main__":
    # Load your spaCy model here
    nlp = spacy.load("en_core_web_sm")  # Example: Load a spaCy model
    nlp.add_pipe("sentencizer")
    test_token_length_with_fuzzer(nlp)  # Pass the nlp object to the function
