from hellosign_sdk import HSClient
import yaml
#put this in the ignore files for github so it is never checkedin!
creds = yaml.load(open('creds.yml'))

print(creds)

global apikey
apikey = creds['nicAPIKEY']
client = HSClient(api_key=apikey)
clientID = creds['nicClientID']

#_mySigRequest = "a2049f71e6806c28f0605c8829cde4c930d396d3"
#_mySigRequest2 = '483967e35219c9e08dd9791bc83395c601300866'
#_mySignID_ToCancel = ''
#_myRecentSigRequest = '' #set in exploreSignatureRequestResponseObject
listOfSignRequests = []

_templateID = 'tbd'
_templateIDHardCode = ''

menu_item = 'tom'

def exploreTemplateResponseObject(templateResponseObject):
    print("********************************************BEGIN exploreTemplateResponseObject********************")
    print(templateResponseObject.template_id)
    print(" = template ID \n")
    print(templateResponseObject.template_id)
    print(" = template ID \n")
    print(templateResponseObject.custom_fields)
    print(" = custom_fields")


    print("********************************************END exploreTemplateResponseObject********************")



def exploreUnclaimedDraftResponseObject(responseObject):
    print("********************************************BEGIN exploreTemplateResponseObject********************")
    print(responseObject)
    print(" = responseObject\n")
    print(responseObject.claim_url)
    print(" = claim_url\n")
    print(responseObject.signing_redirect_url)
    print(" = signing_redirect_url\n")
    print(responseObject.expires_at)
    print(" = expires_at\n")
    print(responseObject.test_mode)
    print(" = test_mode\n")
    print(responseObject.signature_request_id)
    print(" = signature_request_id")
    print("********************************************END exploreTemplateResponseObject********************")


def exploreSignatureRequestResponseObject(responseObject):
    print("********************************************BEGIN exploreSignatureRequestResponseObject********************")
    print(responseObject.files_url)
    print(" = files_url\n")
    print(responseObject.signing_url)
    print(" = signing_url")
    print(responseObject.details_url)
    print(" = details_url")

    print(responseObject.test_mode)
    print(" =TEST MODE\n")
    print(responseObject.requester_email_address + " =Requester_email_address\n")
    print(responseObject.title)
    print(" =title\n")
    print(responseObject.message + " =message\n")
    print(responseObject.has_error)
    print(" =has_error\n")
    print(responseObject.final_copy_uri + " = final_copy_uri\n")
    print(responseObject.subject + " =subject\n")
    print(responseObject.is_complete)
    print(" = is_complete\n")
    print(responseObject.response_data)
    print(" = response_data\n")
    print(responseObject.signatures)
    global _myRecentSigRequest
    for x in responseObject.signatures:
        print(x)
        print(" = x\n")
        print(x.signature_id)
        _myRecentSigRequest = x.signature_id
        print(" = x.signature_id\n")
        listOfSignRequests.append(x.signature_id)
        print(x.signer_email_address)
        print(" = x.signer_email_address\n")
        print(x.signer_name)
        print(" = x.signer_name\n")
        print(x.status_code)
        print(" = x.status_code\n")

        print("--------Begin last reminded at")
        print(x.last_reminded_at)
        print(" = x.last_reminded_at")
        #print(convertUTCtoLocal(x.last_reminded_at))
        print("--------END last reminded at")
        print("--------Begin last signed at")
        print(x.signed_at)
        print(" = x.signed_at")
        #print(convertUTCtoLocal(x.signed_at))
        print("--------END last signed at")
        print("--------BEGIN last viewed at")
        print(x.last_viewed_at)
        print(" = x.last_viewed_at")
        #print(convertUTCtoLocal(x.last_viewed_at))
        print("--------END last viewed at")
    print("********************************************END exploreSignatureRequestResponseObject********************")


    #print(responseObject.signatures[0])

    #_myRecentSigRequest = responseObject.signatures[0]
    #print(responseObject.signatures[1])
    print(" = signatures\n")
    print(type(responseObject))
    print("The above is the type of response object just explored\n")
    #To find things I can pump out, just go to the documentation and look at response.
    print("****************************************************exploreSignatureRequestResponseObject********************")


while (menu_item is not 111):
    print("\n")
    print("\n")
    print("MENU\n")
    print("")

    print("1 -  ")
    print("2 -  ")
    print("3 -  ")
    print("4 -  ")
    print("5 -  ")
    print("6 -  ")
    print("7 -  ")

    print("8 -  ")
    print("9 -  ")
    print("10 -  ")



    print("11 -  ")
    print("12 -  ")
    print("13 -  ")
    print("14:  ")
    print("15:  ")

    print("16:  ")
    print("17:  ")

    print("18:   ")
    print("19 -  ")
    print("20 -  ")
    print("21 -  ")
    print("22 -  ")

    print("23 -  ")
    print("24 -   ")
    print("25 -  ")
    print("26 -  ")

    print("28  -   ")

    print("111: EXIT because these go to 11!!!!\n")
    menu_item = input()

    if menu_item is 1:




        print("****************************************************1 - client.get_signature_request_file END**********")
    elif menu_item is 2:
        print(
        "****************************************************2 GET signature_request - START**********************")
        client = HSClient(api_key=apikey)
        response = client.get_signature_request('246f6a69429d33809efbefc7d64de8476b38a8fd')
        print(response)
        print(type(client))
        print("****************************************************2 GET signature_request - END**********************")
    elif menu_item is 3:
        print("****************************************************3 - client.send_signature_request START************")




        print("****************************************************3 - client.send_signature_request END**************")

    elif menu_item is 4:
        print("****************************************************4 - client.send_with_template - START***************")




        print("****************************************************4 - client.send_with_template - END*****************")

    elif menu_item is 5:
        print("****************************************************5 Embedded requesting - START**********************")




        print("****************************************************5 Embedded requesting - END**********************")
    elif menu_item is 6:
        print("****************************6 - Embedded Signature request with template - START**********************")


        print("****************************6 - Embedded Signature request with template - END**********************")
    elif menu_item is 7:
        print("HI")

    elif menu_item is 8:

        print("*************8 - Delete all unsigned documents that are out for signature - START**********************")




        print("*************8 - Delete all unsigned documents that are out for signature - END**********************")
    elif menu_item is 9:

        print("****************************************************Delete a sign request - START**********************")

        print("****************************************************Delete a sign request - END**********************")
    elif menu_item is 10:

        print("****************************************************Embedded Request - START**********************")


        print("****************************************************Embedded Request - END**********************")
    elif menu_item is 11:

        print("****************************************************11 Get a link to download the document - START**********************")



        print("****************************************************11 Get a link to download the document - END**********************")

    elif menu_item is 12:

        print("**********************12 Create embedded unclaimed draft - START**********************")


        print("**********************12 Create embedded unclaimed draft - END**********************")
        print("A change")
    elif menu_item is 13:

        print("***********************13 non embedded signature request - START**********************")

        print("******************************13 non embedded signature request - END**********************")
    elif menu_item is 14:

        print("***************14 embeded request with template - START**********************")


        print("*************14 embedded request with template - END**********************")

    elif menu_item is 15:

        print("****************************************************15 Account info - START**********************")


        print("****************************************************15 Account info - END**********************")

    elif menu_item is 16:

        print("***************************************16 Send Reminder Request- START**********************")

        print("****************************************16 Send Reminder Request - END**********************")

    elif menu_item is 17:

        print("***************************************17 Cancel a signature request START**********************")

        print("****************************************17 Cancel a signature request END**********************")
    elif menu_item is 18:

        print("***************************************18 Get template info**********************")



        print("****************************************18 Get template info*****************")

    elif menu_item is 19:
        print("***************************************19 create URL over and over PART 2**********************")

        print("***************************************9 create URL over and over PART 2**********************")

    elif menu_item is 20:
        print("************************************20 Make an oAUTH call************************************")




    elif menu_item is 21:

        print("***************************************21 Unclaimed Draft Edit and Resend- START**********************")



        print("***************************************21 Unclaimed Draft Enit and Resend - END**********************")
        print("A change")

    elif menu_item is 22:

        print("****************************************************22 - START**********************")


        print("****************************************************22 - END**********************")
        print("A change")


    elif menu_item is 23:





        print("********23 Embedded Template Walkthrough STEP 1 - Create a template draft (create embedded draft) - END**********************")


        #29b4dbf9da701bdc4e374106ed07a729b84bd6ff
        #https://www.hellosign.com/editor/embeddedTemplate?token=4b2691572b0e1bbdbcf3523295887b01&root_snapshot_guids%5B0%5D=93f918a13205562dd39f3d983f74ef02987a5c6c&snapshot_access_guids%5B0%5D=79eeb37e&guid=29b4dbf9da701bdc4e374106ed07a729b84bd6ff
    elif menu_item is 24:

        print("********Embedded signing With the template created from embedded template - START**********************")




    elif menu_item is 25:

        print("*****************GET TEMPLATE - START**********************")



        print("*****************GET TEMPLATE - END**********************")
    elif menu_item is 26:

        print("********26 - Previewing a signature request - part of embedded template walkthrough - START************")



        print("********26 - Previewing a signature request - part of embedded template walkthrough  - END*************")
        print("A change")
    elif menu_item is 27:

        print("***************************27 - Generate embedded signining from template draft - START****************")

        print("***************************27 - Generate embedded signing from template draft - END********************")

    elif menu_item is 28:

        print("*******************************28 Template ordering ticket - START**********************")





        print("*******************************28 Template ordering ticket - END**********************")
        print("A change")


    #print("28  - template ordering ticket ")


    elif menu_item is 123:

        print("HI")



    elif menu_item is 11111:

        print("****************************************************X - START**********************")
        print("****************************************************X - END**********************")
        print("A change")


    elif menu_item is 111:
        continue


