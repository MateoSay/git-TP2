from service_gmail import obtener_servicio
import base64
import pickle
servicio=obtener_servicio()
# Call the Gmail API
#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages 

#results = servicio.users().messages().list(userId='me').execute()
#messages = results.get('messages', id)
#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{id}
#results_2 = servicio.users().messages().get(userId='me',id='17acfd7eb7e88a4b').execute()
#https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/{messageId}/attachments/{id}
results_3:servicio.users().messages().attachments().get(userId='me',messageId='17acfd7eb7e88a4b',id='ANGjdJ8ChyRcSA3P7B2OHct-MvQidKyLWg93yFSkEG8LsDB5fjInATYBCIfHyoL18FwwyRhLH6gZssBuHEgRN4qz6DT7hu5drb_4fSFoqapeYkxMxAFSqCXnu-Otim9wYdsNnuzf7Yv0nbarf9CljJ_g-nW0_ecr3oY6TAZxL0NJQMJTj9_wUh63_9njEYjx3Es2x6dAJyuKgqHjhrpBx5YsPLPu3OeJxYTlQW1Q4PIwyQvBvVSqVis1tZMSiwcdOMqFed5qaP05MGvgqG-rZZ9K4r6JqoE9tAOnEA7oQNmS00mFzUEuBOvMJJ5TC9-Ep3d0PvpgG8R84YRIE_Z8vWWUzz5M27VU_xwEK-DGdlJz44hqSJ4665WYSWMyL361WLOaDkkekah-8NNvWzB6').execute()
with open("dni.png","wb") as jpg:
        jpg.write(base64.urlsafe_b64decode(imagen))


'''
if not messages:
    print('No labels found.')
else:
    print('Messages:')
    for i in messages:
        print(messages)
'''