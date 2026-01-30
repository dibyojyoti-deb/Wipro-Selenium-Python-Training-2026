*** Settings ***
Library           SeleniumLibrary

*** Test Cases ***


tc001.robot
    Open Application
    Title Should Be    Google
    Close Browser

*** Keywords ***


Open Application
    Open Browser    https://www.google.com    chrome
    Maximize Browser Window
