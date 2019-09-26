import pytest
import converte_hora

def test_converte_hora_none():
	converte_hora = converteHora()
	assert converte_hora.converteHora(24,70) == None, "should be none"

def teste_converte_hora_zero():
	converte_hora = converteHora()
	assert converte_hora.converteHora(0,22) == 12, "should be 12"

def teste_converte_hora_12():
	converte_hora = converteHora()
	assert converte_hora.converteHora(10,30) == "10:30 AM", "should be 10:30 AM"

def teste_converte_hora_24():
	converte_hora = converteHora()
	assert converte_hora.converteHora(13,13) == "13:13 PM", "should be 12"

