<h1> Word-Predictor (Python Project) </h1>
        <p><strong>Overview:</strong> This Python project is a simple word-predictor that reads a text file and builds a vocabulary from its contents. When a particular word is given as input and that word is not present in the preogram's vocabulary, it predicts a word from its vocabulary that is most likely the "required word", along with a probability score.</p>
        <h2>How it Works</h2>
        <ol>
            <li><strong>Reading a Text File:</strong> The program starts by reading a text file provided by the user. This text file should contain a list of words to build the program's vocabulary.</li>
            <li><strong>Building the Vocabulary:</strong> The program analyzes the text file, tokenizes it into words, and creates a vocabulary from these words. It keeps track of the frequency of each word in the text, which helps determine the probability of a word being correct.</li>
            <li><strong>Input Word Check:</strong> When the user provides an input word, the program checks if it exists in the vocabulary. If the word is present, no suggestions are provided as it is considered correct.</li>
            <li><strong>Finding Suggestions:</strong> If the input word is not in the vocabulary, the program looks for similar words within the vocabulary. It calculates the probability of each word being the correct suggestion based on factors like edit distance (how similar the word is in terms of character edits) and word frequency in the vocabulary.</li>
            <li><strong>Displaying Suggestions:</strong> The program presents the user with the word from the vocabulary that has the highest probability of being the correct replacement for the input word. It also displays the calculated probability score.</li>
        </ol>
        <p>Feel free to use this overview as a reference for your Python word-predictor project.</p>

