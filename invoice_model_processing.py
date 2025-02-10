# NR: February 2025

import os
import json
import pandas as pd
from dotenv import load_dotenv

# Azure SDK imports
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient, AnalyzeResult


def setup_client() -> DocumentAnalysisClient:
    """
    Set up and return a DocumentAnalysisClient.

    :return: A DocumentAnalysisClient object for interacting with Azure Document Intelligence.
    """
    load_dotenv()
    endpoint = os.getenv('ENDPOINT')
    key = os.getenv('KEY')
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )
    return document_analysis_client


def analyse_document(document_analysis_client: DocumentAnalysisClient) -> AnalyzeResult:
    """
    Analyse a document (invoice) from a specified URL using the prebuilt-invoice model.

    :param document_analysis_client: The client used to analyse documents.
    :type document_analysis_client: DocumentAnalysisClient
    :return: The analysis result containing the extracted data.
    """
    file_model_id = "prebuilt-invoice"  # Essential
    file_url = "https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/blob/main/Labfiles/01-prebuild-models/sample-invoice/sample-invoice.pdf?raw=true"
    file_locale = "en-US"

    poller = document_analysis_client.begin_analyze_document_from_url(
        model_id=file_model_id,
        document_url=file_url,
        locale=file_locale 
    )

    analysis_result = poller.result()
    return analysis_result


def populate_json(analysis_result: AnalyzeResult):
    """
    Extract fields from the analysis_result and write them to a JSON file.

    :param analysis_result: The result object from the document analysis.
    :type analysis_result: DocumentAnalysisResult
    :return: None
    """
    documents = analysis_result.documents
    print(f"Extracted document(s): {len(documents)}")

    # Prepare a list to store the data for all documents
    all_extracted_data = []

    # The fields we're especially interested in extracting
    fields_to_extract = [
        'AmountDue', 'BillingAddress', 'BillingAddressRecipient',
        'CustomerAddress', 'CustomerAddressRecipient',
        'CustomerId', 'CustomerName',
        'DueDate', 'InvoiceDate', 'InvoiceId', 'InvoiceTotal',
        'Items', 'PreviousUnpaidBalance', 'PurchaseOrder',
        'RemittanceAddress', 'RemittanceAddressRecipient',
        'ServiceAddress', 'ServiceAddressRecipient',
        'ShippingAddress', 'ShippingAddressRecipient',
        'SubTotal', 'TotalTax',
        'VendorAddress', 'VendorAddressRecipient',
        'VendorName'
    ]

    # Loop through each analysed document and capture relevant fields
    for doc_index, doc in enumerate(documents, start=1):
        # Create a dictionary for the data in this document
        extracted_data = {}

        # Store a reference to the document's number/index
        extracted_data["DocumentNumber"] = doc_index

        # For each desired field, collect content and confidence score
        for field_name in fields_to_extract:
            field_obj = doc.fields.get(field_name)
            if field_obj:
                extracted_data[field_name] = {
                    "content": field_obj.content,
                    "confidence": field_obj.confidence
                }
            else:
                extracted_data[field_name] = None

        # Append this document's data to our master list
        all_extracted_data.append(extracted_data)

    # Print a quick preview to the console
    # print("----- Extracted Data (Python) -----")
    # print(all_extracted_data)

    # Save everything to a JSON file
    output_filename = "invoices_extracted.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(all_extracted_data, f, indent=2, ensure_ascii=False)

    print(f"Saved {output_filename}")


def main() -> None:
    """
    Main function to set up the client, analyse the document,
    and generate the output JSON.
    """
    document_analysis_client = setup_client()
    analysis_result = analyse_document(document_analysis_client)
    populate_json(analysis_result)

    print('Analysis Complete!')


if __name__ == '__main__':
    main()

