import logging

import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        provider = 'http://www.youtube.com/oembed' #To extend to other providers reference https://oembed.com/providers.json
        payload = {'url': url, 'format': 'json'}
        try:
            response = requests.get(provider, params=payload)
        except:
            return func.HttpResponse(
                f"Issue with the API Request to the provider: {provider}",
                status_code=500
            )
        return func.HttpResponse(response.text)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a url in the query string or in the request body for a oEmbed response.",
             status_code=200
        )
