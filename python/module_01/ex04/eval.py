class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(coefs[i] * len(words[i]) for i in range(len(words)))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        total = 0
        for i, word in enumerate(words):
            total += coefs[i] * len(word)
        return total