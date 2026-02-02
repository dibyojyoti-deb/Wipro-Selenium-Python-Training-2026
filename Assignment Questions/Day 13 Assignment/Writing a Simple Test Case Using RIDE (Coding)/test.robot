*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***
Verify Page Load
    Open Browser               https://www.google.com    chrome
    Title Should Be            Google
    Capture Page Screenshot    google_page.png
    [Teardown]                 Close Browser