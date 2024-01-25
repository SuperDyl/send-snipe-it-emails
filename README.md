# send-snipe-it-emails

A simple Excel and VBA solution to automate sending emails while auditing assets on Snipe-IT.

## Setup

1. Download the zip of the code
2. Open the excel document
3. If a popup appears, choose "Enable Macros"
4. Follow the instructions on the first sheet to import data from Snipe-IT (it requires generating reports as csv files and copying the data into the spreadsheet)
5. Adjust the spreadsheet to fit the columns in your Snipe-IT configuration and have the correct email configuration

## Adjustments

Snipe-IT can have different columns for different organizations. You will need to adjust formulas to point to the correct columns. This spreadsheet also includes a Visual Basic script to send emails. The text of the email template will also need to be adjusted.

### Snipe-IT ASSETS

Column A:

```vba
=XLOOKUP(<username column>2,'Snipe-it USERS'!$<username column>,'Snipe-it USERS'!<email column>,"NOT FOUND")
```

Column B:

```vba
=XLOOKUP(<username column>2,'Snipe-it USERS'!$<username column>,'Snipe-it USERS'!<name column>,"NOT FOUND")
```

Conditional Formatting:

```vba
=$<Last Audit Column>1+DATE(1,0,0)>TODAY()
```

### Emails

This code is found in the VBA scripts

In `DraftHtmlEmail`:

```vba
Set oAccount = getOutlookAccount("your_sender_email@company.com")
```

You can find the rest of the email in the `generateHtml` function.

## Usage

1. Open the spreadsheet, making sure to `Enable Macros`
2. Follow the instructions on the Instructions tab to update the employee and assets data
3. Return to the Snipe-IT ASSETS sheet
4. Run the `Send Emails` macro
5. Go to Outlook and check your drafts folder
6. Check each of the generated emails before sending

## Python Script

The provided Python script creates fake data to insert into the sheet. Feel free to use the script to scrub important data from the sheet if sharing it with a colleague.
