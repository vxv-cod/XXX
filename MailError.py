import win32com.client as win32
outlook = win32.Dispatch('Outlook.Application')
mail = outlook.CreateItem(0)
mail.To = 'To address'
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

# To attach a file to the email (optional):
attachment  = "Path to the attachment"
mail.Attachments.Add(attachment)

mail.Send()