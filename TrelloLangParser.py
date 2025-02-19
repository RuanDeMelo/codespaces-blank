# Generated from TrelloLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,50,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,42,8,1,11,
        1,12,1,43,1,1,1,1,3,1,48,8,1,1,1,0,0,2,0,2,0,0,55,0,4,1,0,0,0,2,
        47,1,0,0,0,4,5,5,12,0,0,5,6,5,17,0,0,6,7,5,13,0,0,7,9,5,17,0,0,8,
        10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,
        12,1,1,0,0,0,13,14,5,1,0,0,14,15,5,4,0,0,15,48,5,18,0,0,16,17,5,
        1,0,0,17,18,5,6,0,0,18,19,5,18,0,0,19,20,5,11,0,0,20,48,5,17,0,0,
        21,22,5,1,0,0,22,23,5,8,0,0,23,24,5,18,0,0,24,25,5,11,0,0,25,48,
        5,17,0,0,26,27,5,3,0,0,27,28,5,8,0,0,28,29,5,17,0,0,29,30,5,10,0,
        0,30,48,5,17,0,0,31,32,5,2,0,0,32,48,5,5,0,0,33,34,5,2,0,0,34,35,
        5,7,0,0,35,36,5,11,0,0,36,48,5,17,0,0,37,38,5,9,0,0,38,39,5,16,0,
        0,39,41,5,14,0,0,40,42,3,2,1,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,
        1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,15,0,0,46,48,1,0,0,0,
        47,13,1,0,0,0,47,16,1,0,0,0,47,21,1,0,0,0,47,26,1,0,0,0,47,31,1,
        0,0,0,47,33,1,0,0,0,47,37,1,0,0,0,48,3,1,0,0,0,3,11,43,47
    ]

class TrelloLangParser ( Parser ):

    grammarFileName = "TrelloLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CRIAR'", "'MOSTRAR'", "'MOVER'", "'BOARD'", 
                     "'BOARDS'", "'LISTA'", "'LISTAS'", "'CARD'", "'REPITA'", 
                     "'AO'", "'NO'", "'KEY'", "'TOKEN'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "CRIAR", "MOSTRAR", "MOVER", "BOARD", 
                      "BOARDS", "LISTA", "LISTAS", "CARD", "REPITA", "AO", 
                      "NO", "KEY", "TOKEN", "APAR", "FPAR", "NUM", "ID", 
                      "STRING", "PULAR" ]

    RULE_prog = 0
    RULE_comando = 1

    ruleNames =  [ "prog", "comando" ]

    EOF = Token.EOF
    CRIAR=1
    MOSTRAR=2
    MOVER=3
    BOARD=4
    BOARDS=5
    LISTA=6
    LISTAS=7
    CARD=8
    REPITA=9
    AO=10
    NO=11
    KEY=12
    TOKEN=13
    APAR=14
    FPAR=15
    NUM=16
    ID=17
    STRING=18
    PULAR=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(TrelloLangParser.KEY, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TrelloLangParser.ID)
            else:
                return self.getToken(TrelloLangParser.ID, i)

        def TOKEN(self):
            return self.getToken(TrelloLangParser.TOKEN, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrelloLangParser.ComandoContext)
            else:
                return self.getTypedRuleContext(TrelloLangParser.ComandoContext,i)


        def getRuleIndex(self):
            return TrelloLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = TrelloLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(TrelloLangParser.KEY)
            self.state = 5
            self.match(TrelloLangParser.ID)
            self.state = 6
            self.match(TrelloLangParser.TOKEN)
            self.state = 7
            self.match(TrelloLangParser.ID)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.comando()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 526) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CRIAR(self):
            return self.getToken(TrelloLangParser.CRIAR, 0)

        def BOARD(self):
            return self.getToken(TrelloLangParser.BOARD, 0)

        def STRING(self):
            return self.getToken(TrelloLangParser.STRING, 0)

        def LISTA(self):
            return self.getToken(TrelloLangParser.LISTA, 0)

        def NO(self):
            return self.getToken(TrelloLangParser.NO, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TrelloLangParser.ID)
            else:
                return self.getToken(TrelloLangParser.ID, i)

        def CARD(self):
            return self.getToken(TrelloLangParser.CARD, 0)

        def MOVER(self):
            return self.getToken(TrelloLangParser.MOVER, 0)

        def AO(self):
            return self.getToken(TrelloLangParser.AO, 0)

        def MOSTRAR(self):
            return self.getToken(TrelloLangParser.MOSTRAR, 0)

        def BOARDS(self):
            return self.getToken(TrelloLangParser.BOARDS, 0)

        def LISTAS(self):
            return self.getToken(TrelloLangParser.LISTAS, 0)

        def REPITA(self):
            return self.getToken(TrelloLangParser.REPITA, 0)

        def NUM(self):
            return self.getToken(TrelloLangParser.NUM, 0)

        def APAR(self):
            return self.getToken(TrelloLangParser.APAR, 0)

        def FPAR(self):
            return self.getToken(TrelloLangParser.FPAR, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TrelloLangParser.ComandoContext)
            else:
                return self.getTypedRuleContext(TrelloLangParser.ComandoContext,i)


        def getRuleIndex(self):
            return TrelloLangParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = TrelloLangParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(TrelloLangParser.CRIAR)
                self.state = 14
                self.match(TrelloLangParser.BOARD)
                self.state = 15
                self.match(TrelloLangParser.STRING)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(TrelloLangParser.CRIAR)
                self.state = 17
                self.match(TrelloLangParser.LISTA)
                self.state = 18
                self.match(TrelloLangParser.STRING)
                self.state = 19
                self.match(TrelloLangParser.NO)
                self.state = 20
                self.match(TrelloLangParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(TrelloLangParser.CRIAR)
                self.state = 22
                self.match(TrelloLangParser.CARD)
                self.state = 23
                self.match(TrelloLangParser.STRING)
                self.state = 24
                self.match(TrelloLangParser.NO)
                self.state = 25
                self.match(TrelloLangParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(TrelloLangParser.MOVER)
                self.state = 27
                self.match(TrelloLangParser.CARD)
                self.state = 28
                self.match(TrelloLangParser.ID)
                self.state = 29
                self.match(TrelloLangParser.AO)
                self.state = 30
                self.match(TrelloLangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(TrelloLangParser.MOSTRAR)
                self.state = 32
                self.match(TrelloLangParser.BOARDS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.match(TrelloLangParser.MOSTRAR)
                self.state = 34
                self.match(TrelloLangParser.LISTAS)
                self.state = 35
                self.match(TrelloLangParser.NO)
                self.state = 36
                self.match(TrelloLangParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 37
                self.match(TrelloLangParser.REPITA)
                self.state = 38
                self.match(TrelloLangParser.NUM)
                self.state = 39
                self.match(TrelloLangParser.APAR)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 40
                    self.comando()
                    self.state = 43 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 526) != 0)):
                        break

                self.state = 45
                self.match(TrelloLangParser.FPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





