"""
This answer needs to be completed. It if there are subset words, it skips the parent.
Additionally, it returns an extra sentence... A copy of the most recent.
"""

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    temp = ""
    sentences = []
    sentences_in_list = 0
    a_sentence_was_added = True

    while a_sentence_was_added:
        a_sentence_was_added = False
        for i in s:
            temp = temp + i
            if temp in wordDict:
                try:
                    sentences[sentences_in_list] = sentences[sentences_in_list] + temp + " "
                except:
                    sentences.insert(sentences_in_list, (temp + " "))
                temp = ""
                a_sentence_was_added = True
        if sentences.count(sentences[sentences_in_list]) > 1:
            a_sentence_was_added = False
        if a_sentence_was_added:
            sentences_in_list = sentences_in_list + 1
    for st in range(len(sentences)):
        sentences[st] = sentences[st][0:-1]
    return sentences

print wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])