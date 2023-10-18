def payment_remainder(your_company_name, invoice_number, customer_name, due_date, current_date, amount, number_of_days, payent_methods, phone_no, email, your_name,your_position,rep1):
    print("Subject: URGENT: " + your_company_name +" - Final Notice - Overdue Payment - Invoice no."+invoice_number + "\n\nDear "+customer_name + ",\nThis is the final notice regarding the overdue payment for invoice " + invoice_number + ", which \nwas due on " +due_date+ ". As of today, "+current_date+", the outstanding balance is NPR."+amount+",\nincluding late payment fees and interest.\n\nWe have sent you several reminders and requests for payment, but we have not received \nany response from you. This is a serious breach of our contract and a violation of our \npayment terms.\n\nWe urge you to make the full payment as soon as possible to avoid further action. If we \ndo not receive the payment within " + number_of_days +" days from the date of this letter, we will have\nno choice but to take legal action against you. This may result in additional costs and \ndamages for you.\n\nPlease note that this is the last opportunity for you to settle this matter amicably. \nWe value your business and we hope to resolve this issue quickly and professionally.\n\nYou can make the payment by "+payent_methods+". Please find the original invoice and the statement of \naccount attached.\n\nIf you have any questions or concerns, please contact us immediately at "+phone_no+"\nor "+email+".\n\nWe appreciate your prompt attention to this matter.\n\nSincerely,\n"+your_name+"\n"+your_position+"\n"+rep1)
your_company_name = input("Your company name: ")
invoice_number = input("Invoice no. : ")
customer_name = input("Customer name: ")
due_date = input("Due date: ")
current_date = input("Current date: ")
amount = input("Amount: ")
number_of_days =input("Grace days: ")
payent_methods = input("Payment_methods: ")
phone_no = input("Phone no. : ")
email = input("Email ID: ")
your_name = input("Your name: ")
your_position = input("Your Position: ")
rep1=your_company_name

payment_remainder(your_company_name, invoice_number, customer_name, due_date, current_date, amount, number_of_days, payent_methods, phone_no, email, your_name,your_position,rep1)