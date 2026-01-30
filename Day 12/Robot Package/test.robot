*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
test
    Open Browser    https://www.google.com    chrome
    Title Should Be    Google
    Close Browser
