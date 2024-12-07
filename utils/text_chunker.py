"""
    Module for chunking text into smaller segments based on character or word limits.
    Provides classes for Latin text punctuation analysis and text breaking strategies.

    * Examples:
        from utils.text_chunker import chunk_text
        text: str = "This is a sample text. It has multiple sentences. We will chunk it."

        # Character-based chunking (limit=20)
        chunks: List[str] = chunk_text(text, method='char', limit=20)
        print(chunks)
        ['This is a sample', 'text.', 'It has multiple',
            'sentences.', 'We will chunk it.']

        # Word-based chunking (limit=3)
        chunks: List[str] = chunk_text(text, method='word', limit=3)
        print(chunks)
        ['This is', ' a', 'sample text', '.', 'It has',
            ' multiple', 'sentences.', 'We will', ' chunk', 'it.']
"""

import re
from typing import List, Dict, Optional, Pattern, Union


class LatinPunctuator:
    """
        Handles punctuation analysis and text segmentation for Latin script languages.
        Provides methods to break text into paragraphs, sentences, phrases and words.
    """

    def getParagraphs(self, text: str) -> List[str]:
        """
            Split text into paragraphs based on multiple newlines.

            Args:
                text: Input text to split into paragraphs

            Returns:
                List of paragraph strings
        """
        return self._recombine(re.split('((?:\r?\n\s*){2,})', text))

    def getSentences(self, text: str) -> List[str]:
        """
            Split text into sentences based on sentence-ending punctuation.
            Handles common abbreviations to avoid false splits.

            Args:
                text: Input text to split into sentences

            Returns:
                List of sentence strings
        """
        return self._recombine(re.split('([.!?]+[\s\u200b]+|…\s+)', text), r'\b(\w|[A-Z][a-z]|Assn|Ave|Capt|Col|Comdr|Corp|Cpl|Gen|Gov|Hon|Inc|Lieut|Ltd|Rev|Mr|Ms|Mrs|Dr|No|Univ|Jan|Feb|Mar|Apr|Aug|Sept|Oct|Nov|Dec|dept|ed|est|vol|vs)\.\s+$')

    def getPhrases(self, sentence: str) -> List[str]:
        """
            Split sentence into phrases based on phrase-separating punctuation.

            Args:
                sentence: Input sentence to split into phrases

            Returns:
                List of phrase strings
        """
        return self._recombine(re.split('([,;:]\s+|\s-+\s+|—\s*|『|』|「|」|„|"|«|»|〈|〉|\[|\]|\(|\)|\{|\}|"|\.\.\.\s+|\*\s+|\'\s+)', sentence))

    def getWords(self, sentence: str) -> List[str]:
        """
            Split sentence into words based on word boundaries and punctuation.

            Args:
                sentence: Input sentence to split into words

            Returns:
                List of word strings
        """
        tokens: List[str] = re.split(
            '([~@#%^*_+=<>|\[\](){}"『』「」„"«»〈〉\.\.\.\*\'\']|[\s\-—/]+|\.(?=\w{2,})|,(?=[0-9]))', sentence.strip())
        result: List[str] = []
        i: int = 0
        while i < len(tokens):
            if tokens[i]:
                result.append(tokens[i])
            if i+1 < len(tokens):
                if re.match(r'^[~@#%^*_+=<>|\[\](){}"『』「」„"«»〈〉...*\'\s]+$', tokens[i+1]):
                    result.append(tokens[i+1])
                elif result:
                    result[-1] += tokens[i+1]
            i += 2
        return result

    def _recombine(self, tokens: List[str], nonPunc: Optional[Pattern] = None) -> List[str]:
        """
            Recombine tokens while handling punctuation and abbreviations.

            Args:
                tokens: List of text tokens to recombine
                nonPunc: Regex pattern for non-punctuation sequences

            Returns:
                List of recombined text segments
        """
        result: List[str] = []
        for i in range(0, len(tokens), 2):
            part: str = tokens[i] + tokens[i+1] if i + \
                1 < len(tokens) else tokens[i]
            if part:
                if nonPunc and result and result[-1] in nonPunc:
                    result[-1] += part
                else:
                    result.append(part)
        return result


class WordBreaker:
    """
        Breaks text into chunks based on word count limits.
        Uses LatinPunctuator for text analysis and segmentation.
    """

    def __init__(self, wordLimit: int, punctuator: LatinPunctuator) -> None:
        """
            Initialize WordBreaker with word limit and punctuator.

            Args:
                wordLimit: Maximum number of words per chunk
                punctuator: LatinPunctuator instance for text analysis
        """
        self.wordLimit: int = wordLimit
        self.punctuator: LatinPunctuator = punctuator

    def breakText(self, text: str) -> List[str]:
        """
            Break full text into word-limited chunks.

            Args:
                text: Input text to break into chunks

            Returns:
                List of text chunks
        """
        return [phrase for sentence in self.punctuator.getSentences(text) for phrase in self.breakSentence(sentence)]

    def breakParagraph(self, text: str) -> List[str]:
        """
            Break paragraph into phrases.

            Args:
                text: Input paragraph text

            Returns:
                List of phrase chunks
        """
        return list(self.punctuator.getPhrases(text))

    def breakSentence(self, sentence: str) -> List[str]:
        """
            Break sentence into word-limited chunks.

            Args:
                sentence: Input sentence text

            Returns:
                List of sentence chunks
        """
        return self.merge(self.punctuator.getPhrases(sentence), self.breakPhrase)

    def breakPhrase(self, phrase: str) -> List[str]:
        """
            Break phrase into word-limited chunks.

            Args:
                phrase: Input phrase text

            Returns:
                List of phrase chunks
        """
        words: List[str] = self.punctuator.getWords(phrase)
        splitPoint: int = min(len(words) // 2, self.wordLimit)
        result: List[str] = []
        while words:
            result.append(''.join(words[:splitPoint]))
            words = words[splitPoint:]
        return result

    def merge(self, parts: List[str], breakPart: callable) -> List[str]:
        """
            Merge text parts into word-limited chunks.

            Args:
                parts: List of text parts to merge
                breakPart: Function to break oversized parts

            Returns:
                List of merged chunks
        """
        result: List[str] = []
        group: Dict[str, Union[List[str], int]] = {'parts': [], 'wordCount': 0}

        def flush() -> None:
            nonlocal group
            if group['parts']:
                result.append(''.join(group['parts']))
                group = {'parts': [], 'wordCount': 0}

        for part in parts:
            wordCount: int = len(self.punctuator.getWords(part))
            if wordCount > self.wordLimit:
                flush()
                subParts: List[str] = breakPart(part)
                result.extend(subParts)
            else:
                if group['wordCount'] + wordCount > self.wordLimit:
                    flush()
                group['parts'].append(part)
                group['wordCount'] += wordCount
        flush()
        return result


class CharBreaker:
    """
        Breaks text into chunks based on character count limits.
        Uses LatinPunctuator for text analysis and segmentation.
    """

    def __init__(self, charLimit: int, punctuator: LatinPunctuator, paragraphCombineThreshold: Optional[int] = None) -> None:
        """
            Initialize CharBreaker with character limit and punctuator.

            Args:
                charLimit: Maximum number of characters per chunk
                punctuator: LatinPunctuator instance for text analysis
                paragraphCombineThreshold: Optional threshold for combining paragraphs
        """
        self.charLimit: int = charLimit
        self.punctuator: LatinPunctuator = punctuator
        self.paragraphCombineThreshold: Optional[int] = paragraphCombineThreshold

    def breakText(self, text: str) -> List[str]:
        """
            Break full text into character-limited chunks.

            Args:
                text: Input text to break into chunks

            Returns:
                List of text chunks
        """
        return self.merge(self.punctuator.getParagraphs(text), self.breakParagraph, self.paragraphCombineThreshold)

    def breakParagraph(self, text: str) -> List[str]:
        """
            Break paragraph into character-limited chunks.

            Args:
                text: Input paragraph text

            Returns:
                List of paragraph chunks
        """
        return self.merge(self.punctuator.getSentences(text), self.breakSentence)

    def breakSentence(self, sentence: str) -> List[str]:
        """
            Break sentence into character-limited chunks.

            Args:
                sentence: Input sentence text

            Returns:
                List of sentence chunks
        """
        return self.merge(self.punctuator.getPhrases(sentence), self.breakPhrase)

    def breakPhrase(self, phrase: str) -> List[str]:
        """
            Break phrase into character-limited chunks.

            Args:
                phrase: Input phrase text

            Returns:
                List of phrase chunks
        """
        return self.merge(self.punctuator.getWords(phrase), self.breakWord)

    def breakWord(self, word: str) -> List[str]:
        """
            Break word into character-limited chunks.

            Args:
                word: Input word text

            Returns:
                List of word chunks
        """
        result: List[str] = []
        while word:
            result.append(word[:self.charLimit])
            word = word[self.charLimit:]
        return result

    def merge(self, parts: List[str], breakPart: callable, combineThreshold: Optional[int] = None) -> List[str]:
        """
            Merge text parts into character-limited chunks.

            Args:
                parts: List of text parts to merge
                breakPart: Function to break oversized parts
                combineThreshold: Optional threshold for combining chunks

            Returns:
                List of merged chunks
        """
        result: List[str] = []
        group: Dict[str, Union[List[str], int]] = {'parts': [], 'charCount': 0}

        def flush() -> None:
            if group['parts']:
                result.append(''.join(group['parts']))
                group['parts'] = []
                group['charCount'] = 0

        for part in parts:
            charCount: int = len(part)
            if charCount > self.charLimit:
                flush()
                subParts: List[str] = breakPart(part)
                for subPart in subParts:
                    result.append(subPart)
            else:
                if (group['charCount'] + charCount) > (combineThreshold or self.charLimit):
                    flush()
                group['parts'].append(part)
                group['charCount'] += charCount
        flush()
        return result


def chunk_text(text: str, method: str = 'char', limit: int = 750) -> List[str]:
    """
        Split text into chunks using either character or word count limits.

        Args:
            text: Input text to chunk
            method: Chunking method ('char' or 'word')
            limit: Maximum chunk size (in characters or words)

        Returns:
            List of text chunks

        Examples:
            >>> text = "This is a sample text. It has multiple sentences. We will chunk it."
            >>> chunks = chunk_text(text, method='char', limit=20)
            >>> print(chunks)
            ['This is a sample', 'text.', 'It has multiple',
                'sentences.', 'We will chunk it.']

            >>> chunks = chunk_text(text, method='word', limit=3)
            >>> print(chunks)
            ['This is', ' a', 'sample text', '.', 'It has',
                ' multiple', 'sentences.', 'We will', ' chunk', 'it.']
    """
    punctuator: LatinPunctuator = LatinPunctuator()
    if method == 'char':
        return CharBreaker(limit, punctuator).breakText(text)
    elif method == 'word':
        return WordBreaker(limit, punctuator).breakText(text)


def main() -> None:
    """
        Test chunk_text function with sample text
    """
    text: str = """This is a sample text. It has multiple sentences. We will chunk it."""
    test_1: List[str] = chunk_text(text, 'char', 20)
    for i, t in enumerate(test_1):
        print(f"Chunk {i+1}: {t}")
    print()
    test_2: List[str] = chunk_text(text, 'word', 3)
    for i, t in enumerate(test_2):
        print(f"Chunk {i+1}: {t}")


if __name__ == '__main__':
    main()
