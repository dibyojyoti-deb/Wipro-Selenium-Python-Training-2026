*** Settings ***
Documentation     OrangeHRM Data-Driven Test
Library           SeleniumLibrary
# Adding explicit encoding and dialect to handle CSV formatting strictly
Library           DataDriver    file=users.csv    encoding=utf_8    dialect=unix
Test Setup        Open Browser To Login Page
Test Teardown     Close Browser
Test Template     Authenticate User And Verify Status

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}        chrome

*** Test Cases ***
# The name here must match the variable in the CSV for DataDriver to map it
Login with user ${username}    Default    Default    Default

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10 seconds

Authenticate User And Verify Status
    [Arguments]    ${username}    ${password}    ${expected_status}
    Input Text       name=username    ${username}
    Input Password   name=password    ${password}
    Click Button     tag=button
    Wait Until Page Contains    ${expected_status}