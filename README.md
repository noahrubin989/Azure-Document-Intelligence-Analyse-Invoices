# Document Intelligence - Invoice Model

## Objective

To demonstrate how to extract meaningful fields from an invoice using Microsoft Azure AI Document Intelligence. 

## Solution

This solution automates data entry from invoices. In the past, manual data entry was the only option because it was difficult for computers to recognise printed or hand-written text. Now, AI can be used as an alternative to manual data entry with lower costs and tends to result in fewer errors in the extracted data.

## Python Environment Set-Up

In an integrated terminal in Visual Studio Code, set up your own virtual environment. Once done, install the following packages:

```bash
pip3 install pandas python-dotenv azure-ai-formrecognizer==3.3.3
```

## Azure Set-Up

### Create an Azure AI Document Intelligence resource:
  1. In the Azure portal, select Create a resource.
  2. In the Search services and marketplace box, type Document Intelligence and then press Enter
  3. In the Document intelligence page, select **Create**
  4. In the Create Document intelligence page, under **Project Details**, select your **Subscription** and either select an existing **Resource group** or create a new one
  5. Under **Instance details**, select a **Region** of your choice (given you are able to deploy to the resource to that region)
  6. In the **Name** textbox, type a unique name for the resource. I called mine `doc-intel-nr`
  7. Select a **Pricing tier**. I used **Free FO** and then select Review + create
  8. If the validation tests pass, select **Create**. Azure deploys the new Azure AI Document Intelligence resource

### Connect to the resource
  1. In the Azure portal, navigate to the Azure AI Document Intelligence resource
  2. Retrive the endpoint and access key
  3. Store the details in a `.env` file for further use


### Running the Code

In an integrated terminal in Visual Studio Code, run the following snippet

```bash
python3 invoice_model_processing.py
```

## Resources
* [The `DocumentAnalysisClient` Class: Attributes and method calls](https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentanalysisclient?view=azure-python#azure-ai-formrecognizer-documentanalysisclient-begin-analyze-document)
* [The `AnalyzeResult` Class](https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.analyzeresult?view=azure-python)
* [Document Intelligence invoice model](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/invoice?view=doc-intel-4.0.0)
* [Document Intelligence invoice model schema (e.g. "VendorName")](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-11-30-ga/invoice.md)

