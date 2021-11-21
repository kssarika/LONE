#@author        :   K S SARIKA
#@team_members  :   ABISHA K B, GAYATHRI GIREESH, VISHNUPRIYA

###############################################################################
################################################################################

#@Aim           :   Creating a new Interpreted Programing Language Named as LONE [Language Of New Era]

#=======================================+++++++++++++++++=============================================
#=======================================+++++++++++++++++=============================================

#=================================Importing Modules===================================================

from str_arr import *
from Tokens import *
from Lexer import *
from Parser import *
from Interpreter import *

def run(fn, text):
		# Generate tokens
		lexer = Lexer(fn, text)
		
		tokens, error = lexer.make_tokens()
		print(tokens)
		if error: return None, error
		
		# Generate AST
		parser = Parser(tokens)
		ast = parser.parse()
		#print(ast)
		if ast.error: return None,ast.error

		#Run Program
		interpreter = Interpreter()
		#print(interpreter)
		context = Context('<program>')
		result = interpreter.visit(ast.node, context)
		return result.value, result.error