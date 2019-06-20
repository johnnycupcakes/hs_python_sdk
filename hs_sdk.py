from hellosign_sdk import HSClient

client = HSClient(api_key="KEY")
client.send_signature_request(
    test_mode=True,
    title="NDA with Acme Co.",
    subject="The NDA we talked about",
    message="Please sign this NDA and then we can discuss more. Let me know if you have any questions.",
    signers=[
        { 'email_address': 'nicholas.boutte@hellosign.com', 'name': 'Jack', 'order': 0 }
    ],
    cc_email_addresses=[],
    files=['NDA.pdf'],
    metadata={
        'client_id' : '1234',
        'custom_text' : 'NDA #9'
    }
)