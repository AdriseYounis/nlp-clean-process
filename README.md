# Cleaning & Processing Text for NLP

This project demonstrates how to clean and process text for Natural Language Processing (NLP) tasks. It covers text preprocessing techniques such as stemming, lemmatization, and part-of-speech (POS) tagging.

## Key Differences Between Stemming and Lemmatization

### Stemming

**What is it?**  
Stemming is the process of reducing a word to its base or root form by chopping off prefixes or suffixes.

**How does it work?**  
It uses rule-based heuristics, such as removing common suffixes like -ing, -ed, -s, etc. This process is faster but can sometimes produce non-dictionary words.

**Examples in Your Output:**  
- "experience" → "experi" (suffix -ence removed)
- "software" → "softwar" (suffix -e removed)
- "building" → "build" (suffix -ing removed)

**When to use:**  
Stemming is useful when speed is more important than precision, such as in search engines where exact grammar isn't required.

### Lemmatization

**What is it?**  
Lemmatization is the process of reducing words to their dictionary or canonical (root) form, considering the context and part of speech of the word.

**How does it work?**  
It uses a vocabulary and linguistic rules to ensure that the transformed word is valid in the language. For instance:
- Verbs are converted to their infinitive form (e.g., "running" → "run").
- Nouns are converted to singular (e.g., "applications" → "application").

**Examples in Your Output:**  
- "experience" → "experience" (unchanged; already in base form)
- "software" → "software" (unchanged; already in base form)
- "building" → "building" (unchanged; depends on context)
- "involved" → "involve" (converted to infinitive form)

**When to use:**  
Lemmatization is better when precision matters, such as in NLP applications requiring grammatical correctness (e.g., chatbots or text summarization).

| **Aspect**             | **Stemming**                   | **Lemmatization**                 |
|------------------------|---------------------------------|-----------------------------------|
| **Approach**           | Rule-based, heuristic chopping | Vocabulary + grammatical rules    |
| **Speed**              | Faster                         | Slower                            |
| **Output Words**       | May not be actual words        | Valid dictionary words           |
| **Context Consideration** | No                            | Yes (requires part-of-speech info)|
| **Examples**           | "experi", "develop", "softwar" | "experience", "development", "software" |

---

## POS Tags

### What are POS Tags?

**POS (Part-of-Speech) tags** are labels assigned to words in a text to indicate their grammatical role in a sentence. These tags help identify whether a word is a noun, verb, adjective, adverb, etc., based on its usage and context.

**Example Sentence:**

"The cat sleeps on the mat."

- The → Determiner (DT)
- cat → Noun (NN)
- sleeps → Verb (VBZ)
- on → Preposition (IN)
- the → Determiner (DT)
- mat → Noun (NN)

### Why are POS Tags Important?

POS tags provide essential context for NLP tasks. They allow algorithms to:

- **Understand Sentence Structure:** Identify the subject, verb, and object.
- **Disambiguate Word Meanings:** Words like "bank" (as a financial institution or a riverbank) can be interpreted correctly based on context.
- **Improve Text Preprocessing:** Tasks like lemmatization and parsing use POS tags to make informed decisions about word transformations.

| **Tag** | **Part of Speech**                | **Example**                          |
|---------|-----------------------------------|--------------------------------------|
| NN      | Noun, singular                   | dog, car, flower                    |
| NNS     | Noun, plural                     | dogs, cars, flowers                 |
| VB      | Verb, base form                  | run, eat, jump                      |
| VBD     | Verb, past tense                 | ran, ate, jumped                    |
| VBG     | Verb, gerund/present participle  | running, eating, jumping            |
| VBN     | Verb, past participle            | eaten, driven                       |
| JJ      | Adjective                         | big, small, beautiful               |
| RB      | Adverb                            | quickly, silently                   |
| DT      | Determiner                        | the, a, an                          |
| IN      | Preposition                       | on, at, by                          |

---

## Running the Script

To execute the script, run the following command in your terminal:

```bash
python3 src/text_preprocessing.py   
```

### Python Environment Trusts SSL Certificates

If you're encountering SSL certificate errors while running the script, you can fix this by running the following command to ensure that your Python environment trusts SSL certificates:

```bash
open /Applications/Python*/Install\ Certificates.command
