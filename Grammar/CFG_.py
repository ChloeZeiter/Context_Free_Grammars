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

    def to_grammar(self, filename : str):
        with open(filename, 'w', encoding='utf-8') as outfile:
            for axiom in self.grammar.keys():
                productions = self.grammar.get(axiom)
                for production in productions:
                    if not production: production = "EMPTY"
                    production_str = f"{axiom} -> {production}\n"
                    outfile.write(production_str)
            outfile.close()
        
    def from_dict(self, productions : dict):
        self.grammar = productions

    def transform(self, in_ : str, MAX_EPOCH : int)->str:
        epoch = 0
        while epoch < MAX_EPOCH:
            for axiom in self.grammar.keys():
                in_ = in_.replace(axiom, random.choice(self.grammar.get(axiom)), 1)
            epoch += 1
        return in_
