import requests


url = "https://api.dhl.com/dgff/transportation/shipment-status"


querystring = {"housebill": "SOME_STRING_VALUE"}


headers = {
	"content-type": "application/json",
	"DHL-API-Key": "Mv6am6ilUqbvuOksTWpX4vX4zPYyjOy5"
}


response = requests.request("GET", url, headers=headers, params=querystring)


print(response.text)