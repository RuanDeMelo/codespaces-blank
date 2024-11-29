# Generated from TrelloLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TrelloLangParser import TrelloLangParser
else:
    from TrelloLangParser import TrelloLangParser

# This class defines a complete listener for a parse tree produced by TrelloLangParser.
class TrelloLangListener(ParseTreeListener):

    # Enter a parse tree produced by TrelloLangParser#prog.
    def enterProg(self, ctx:TrelloLangParser.ProgContext):
        pass

    # Exit a parse tree produced by TrelloLangParser#prog.
    def exitProg(self, ctx:TrelloLangParser.ProgContext):
        pass


    # Enter a parse tree produced by TrelloLangParser#comando.
    def enterComando(self, ctx:TrelloLangParser.ComandoContext):
        pass

    # Exit a parse tree produced by TrelloLangParser#comando.
    def exitComando(self, ctx:TrelloLangParser.ComandoContext):
        pass



del TrelloLangParser