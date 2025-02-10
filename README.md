# Document Intelligence

## Overview

This repository includes code that demonstrates how to implement a solution that can ingest data from forms into a structured data dataset. 

Manual data entry is a slow and intensive task and can be expensive, especially if you have thousands of forms to enter. Operators often make reading or typing errors that reduce the accuracy of your data.

Manual data entry was the only option because it was difficult for computers to recognise printed or hand-written text. Now, AI has become commonplace and has enabled computers to recognise patterns, such as letter shapes in a piece of text, with a high degree of accuracy. We can use AI as an alternative to manual data entry with lower costs and fewer errors in the extracted data.

Azure AI Document Intelligence is an Azure service that you can use to analyse forms completed by your customers, partners, employers, or others and extract the data that they contain. It's built on the lower level Azure AI Services, including Azure AI Vision. If you want to extract simple words and text from a picture of a form or document, without contextual information, Azure AI Vision OCR is an appropriate service to consider. You might want to use this service if you already have your own analysis code, for example. However, Azure AI Document Intelligence includes a more sophisticated analysis of documents. For example, it can identify key/value pairs, tables, and context-specific fields. If you want to deploy a complete document analysis solution that enables users to both extract and understand text, consider Azure AI Document Intelligence.

In Azure AI Document Intelligence, three of the prebuilt models are for general document analysis:

* Read:
  * Use this model to extract words and lines from both printed and hand-written documents.
  * It also detects the language used in the document and whether the document is hand-written or in printed text
  * It's if you want to extract words and lines from documents with no fixed or predictable structure
  * For multi-page PDF or TIFF files, you can use the pages parameter in your request to fix a page range for the analysis.
  * It is ideal if you want to extract words and lines from documents with no fixed or predictable structure
 
  
* General document:
  * Use this model to extract key-value pairs and tables in your documents
  * The general document model extends the functionality of the read model by adding the detection of key-value pairs, entities, selection marks, and tables. The model can extract these values from structured, semi-structured, and unstructured documents.
  * It is the only prebuilt model to support entity extraction such as 
    * `Person`. The name of a person.
    * `PersonType`. A job title or role.
    * `Location`. Buildings, geographical features, geopolitical entities.
    * `Organization`. Companies, government bodies, sports clubs, musical bands, and other groups.
    * `Event`. Social gatherings, historical events, anniversaries.
    * `Product`. Objects bought and sold.
    * `Skill`. A capability belonging to a person.
    * `Address`. Mailing address for a physical location.
    * `Phone number`. Dialing codes and numbers for mobile phones and landlines.
    * `Email`. Email addresses.
    * `URL`. Webpage addresses.
    * `IP Address`. Network addresses for computer hardware.
    * `DateTime`. Calendar dates and times of day.
    * `Quantity`. Numerical measurements with their units.
    
* Layout:
  * Use this model to extract text, tables, and structure information from forms. It can also recognise selection marks such as check boxes and radio buttons
  * As well as extracting text, the layout model returns selection marks and tables from the input image or PDF file. It's a good model to use when you need rich information about the structure of a document.
  * When you digitise a document, it can be at an odd angle. Tables can have complicated structures with or without headers, cells that span columns or rows, and incomplete columns or rows. The layout model can handle all of these difficulties to extract the complete document structure.
  * For example, each table cell is extracted with:
    * Its content text.
    * The size and position of its bounding box.
    * If it's part of a header column.
    * Indexes to indicate its row and column position in the table.
  * Selection marks are extracted with their bounding box, a confidence indicator, and whether they're selected or not.

The other prebuilt models expect a common type of form or document:

* Invoice: Use this model to extract key information from sales invoices in English and Spanish
* Receipt: Use this model to extract data from printed and handwritten receipts
* W-2 US tax declaration: Use this model to extract data from United States government's W-2 tax declaration form
* ID Document: Use this model to extract data from United States driver's licenses and international passports
* Business card: Use this model to extract names and contact details from business cards
* Health insurance card: Extracts common fields and their values from health insurance cards

The purpose of prebuilt models is to extract the data you need without traininjg yoiur own models.

## Python Environment Set-Up

In an integrated terminal in Visual Studio Code, set up your own virtual environment. Once done, install the following packages:

```python
pip3 install pandas python-dotenv azure-ai-formrecognizer==3.3.3
```



## Set Up

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


### How the code works 

Upon running `poller.result()` you get an `azure.ai.formrecognizer._models.AnalyzeResult` object with a few useful attributes and methods:

**Attributes:** 
* `api_version`
* `content`
* `documents`
* `languages`
* `model_id`
* `pages`
* `paragraphs`
* `styles`
* `tables`
* `key_value_pairs`

**Methods:**
* `from_dict`
* `to_dict`

## Resources
* [The `DocumentAnalysisClient` Class: Attributes and method calls](https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.documentanalysisclient?view=azure-python#azure-ai-formrecognizer-documentanalysisclient-begin-analyze-document)
* [The `AnalyzeResult` Class](https://learn.microsoft.com/en-us/python/api/azure-ai-formrecognizer/azure.ai.formrecognizer.analyzeresult?view=azure-python)
* [Document Intelligence invoice model](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/invoice?view=doc-intel-4.0.0)
* [Document Intelligence invoice model schema (e.g. "VendorName")](https://github.com/Azure-Samples/document-intelligence-code-samples/blob/main/schema/2024-11-30-ga/invoice.md)

