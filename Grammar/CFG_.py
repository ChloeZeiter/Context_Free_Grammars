import random

class Grammar(object):
    def __init__(self, rules : dict = None):
        self.grammar = rules

    def __str__(self):
        s = ""
        for rule in self.grammar.keys():
            s += f"{rule} => { ' | '.join(self.grammar.get(rule))}\n"

        return s

    def from_grammar_file(self, filename : str):
        file_text = open(filename, 'r', encoding = 'utf-8').read()
        productions = dict()
        
        for line in file_text.split("\n"):
            tokens = line.split()
            axiom = tokens[0]
            transformation = tokens[2]
            if transformation == "EMPTY": transformation = ""
            if axiom not in productions.keys():
                productions[axiom] = [transformation]
            else:
                productions[axiom].append(transformation)

        self.grammar = productions

    def from_dict(self, productions : dict):
        self.grammar = productions

    def parse_tokens(self, string : str)->list:
        max_substr_len = max([len(s) for s in self.grammar.keys()])
        tokens = []
        for ix in range(len(string)):
            for lookahead in range(max_substr_len):
                if string[ix : lookahead] in self.grammar.keys():
                    tokens.append(string[ix : lookahead])
                else:
                    tokens.append(string[ix])

        return tokens

    def transform(self, in_ : str, MAX_EPOCH : int)->str:
        epoch = 0
        while epoch < MAX_EPOCH:
            tokens = self.parse_tokens(in_)
            for token_ix in range(len(tokens)):
                token = tokens[token_ix]
                try:
                    production = random.choice(self.grammar.get(token))
                    tokens[token_ix] = production
                except TypeError:
                    continue
            in_ = "".join(tokens)
            epoch += 1

        return in_
