# oEmbed-Provider-Azure-Functions

## oEmbed Provider Implementation for Azure Functions

The oEmbed function offers a simple example of implementing a oEmbed endpoint that takes a YouTube video URL and retrieves the videos oEmbed response from the YouTube oEmbed API endpoint.

## Building out to Support Multiple Providers
At https://oembed.com/providers.json you'll find a list of some of the available oEmbed providers and their APIs.  This can be used as a starting point to match passed in URLs against a greater number of providers and returning appropriate oEmbed responses from their respective endpoints.

## Deployment
This function can be deployed to Azure Functions using VS Code.
You can find instructions on how to install the Azure Functions extension for VS Code and how to run and publish your functions to Azure here: https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code?pivots=programming-language-python