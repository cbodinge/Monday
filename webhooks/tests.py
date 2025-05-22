# from tools.emails import send, text, pdf
# from sample_testing.reports.label import Label, Accession
#
# # send_to = 'carter.bodinger@pinpointtesting.com'
# #
# # order = '25-02-21-16-32-55'
# #
# # subject = f'The requisition form and label for your recent order: {order}'
# # message = f'Your order id: {order}. \n \n \t Find the attached requisition form and sample label.'
# # message = text(message)
# #
# # with open('1234.pdf', 'rb') as f:
# #     req_form = pdf(f.read(), 'requisition form.pdf')
# #
# # with open('1234.pdf', 'rb') as f:
# #     label = pdf(f.read(), 'sample label.pdf')
# #
# # send(send_to, subject, [message, req_form, label])
#
# accession = Accession('25-02-21-16-32-55', 'Carter', 'B')
# l = Label(accession)
# l.code()
#
#
# with open('test.svg', 'wb') as f:
#     f.write(l.construct().encode('utf-8'))