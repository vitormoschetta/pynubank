from pynubank import Nubank, MockHttpClient

# Nota: O QRCode é válido apenas para consulta de transações do cartão de crédito

nu = Nubank()
uuid, qr_code = nu.get_qr_code()

# Nesse momento será printado o QRCode no console
# Você precisa escanear pelo o seu app do celular
# Esse menu fica em NU > Perfil > Acesso pelo site
qr_code.print_ascii(invert=True)

input('Após escanear o QRCode pressione enter para continuar')
# Somente após escanear o QRCode você pode chamar a linha abaixo
nu.authenticate_with_qr_code('CPF', 'Pass', uuid)

# # Lista de dicionários contendo todas as faturas do seu cartão de crédito
# Temos a informação sobre período da fatura, que vai ser importante para selecionar as transações que queremos para cada fatura
bills = nu.get_bills()
print("bills: " + str(bills))
