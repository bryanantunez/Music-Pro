# El SDK apunta por defecto al ambiente de pruebas, no es necesario configurar lo siguiente
transbank.webpay.webpay_plus.webpay_plus_default_commerce_code = 597055555532
transbank.webpay.webpay_plus.default_api_key = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"
transbank.webpay.webpay_plus.default_integration_type = IntegrationType.TEST

response = transbank.webpay.webpay_plus.create(buy_order, session_id, amount, return_url)

response.url
response.token

response = transbank.webpay.webpay_plus.transaction.commit(token)

response.vci
response.amount
response.status
response.buy_order
response.session_id
response.card_detail
response.accounting_date
response.transaction_date
response.authorization_code
response.payment_type_code
response.response_code
response.installments_amount
response.installments_number
response.balance

response = transbank.webpay.webpay_plus.transaction.status(token)

response.vci
response.amount
response.status
response.buy_order
response.session_id
response.card_detail
response.accounting_date
response.transaction_date
response.authorization_code
response.payment_type_code
response.response_code
response.installments_amount
response.installments_number
response.balance

response = Transbank.webpay.webpay_plus.refund(token, amount)

response.authorization_code
response.authorization_date
response.balance
response.nullified_amount
response.response_code
response.type

response = DeferredTransaction.capture(
  token=token, buy_order=buy_order, authorization_code=authorization_code, capture_amount=amount
)

response.authorization_code
response.authorization_date
response.captured_amount
response.response_code

transaction_details = MallTransactionCreateDetails(
  amount_child_1, commerce_code_child_1, buy_order_child_1
).add(
  amount_child_2, commerce_code_child_2, buy_order_child_2
)

response = MallTransaction.create(
    buy_order=buy_order,
    session_id=session_id,
    return_url=return_url,
    details = transaction_details,
)

response.token
response.url

response = MallTransaction.commit(token)

response.accounting_date
response.buy_order
card_detail = response.card_detail
card_detail.card_number
response.session_id
response.transaction_date
response.vci
details = response.details
for detail in details:
  detail.amount
  detail.authorization_code
  detail.buy_order
  detail.commerce_code
  detail.installments_number
  detail.payment_type_code
  detail.response_code
  detail.status
  
  response = MallTransaction.status(token)
  
  response.accounting_date
response.buy_order
card_detail = response.card_detail
card_detail.card_number
response.session_id
response.transaction_date
response.vci
details = response.details
for detail in details:
  detail.amount
  detail.authorization_code
  detail.buy_order
  detail.commerce_code
  detail.installments_number
  detail.payment_type_code
  detail.response_code
  detail.status
  
  response = Transaction.refund(token, buy_order, commerce_code, amount)
  
  response.authorization_code
response.authorization_date
response.balance
response.nullified_amount
response.response_code
response.type

response = MallDeferredTransaction.capture(
  token=token, capture_amount=amount, commerce_code=commerce_code,
  buy_order=buy_order, authorization_code=authorization_code
)

response.authorization_code
response.authorization_date
response.captured_amount
response.response_code

{
  "error_message": "token is required"
}