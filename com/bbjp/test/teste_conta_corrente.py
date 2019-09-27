import pytest
from com.bbjp.conta_corrente import ContaCorrente

conta_correntee = ContaCorrente(1,'eu', 1.0)

def alterarNome_test():
    conta_correntee.alterarNome('tu')
    assert conta_correntee.nomeCorrentista == 'tu'
