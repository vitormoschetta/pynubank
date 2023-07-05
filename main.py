from pynubank import Nubank, MockHttpClient

nu = Nubank()
# nu.authenticate_with_cert("96332824204", "Aewk2680*", "cert.p12")
refresh_token = nu.authenticate_with_cert('CPF', 'Pass', 'cert.p12')
nu.authenticate_with_refresh_token(refresh_token, 'cert.p12')

# # Imprime o saldo da conta
print("balance: " + str(nu.get_account_balance()))

# # Lista de dicionários contendo todas as faturas do seu cartão de crédito
# Temos a informação sobre período da fatura, que vai ser importante para selecionar as transações que queremos para cada fatura
bills = nu.get_bills()
print("bills: " + str(bills))

# # Lista de dicionários contendo todas as transações de seu cartão de crédito
card_statements = nu.get_card_statements()
print("card_statements: " + str(card_statements))

# # Retorna um dicionário contendo os detalhes de uma transação retornada por get_card_statements()
# # Contém as parcelas da transação
card_statement_details = nu.get_card_statement_details(card_statements[0])
print("card_statement_details: " + str(card_statement_details))




# # Soma de todas as compras
print(sum([t['amount'] for t in card_statements]))

# # Retorna um dicionário contendo os detalhes de uma fatura retornada por get_bills()
# bill_details = nu.get_bill_details(bills[1])
# print("bill_details: " + str(bill_details))

# # Imprime os dados
# print("bill_details: " + str(bill_details['summary']))