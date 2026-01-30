*** Settings ***
Library    SeleniumLibrary
# BuiltIn library is automatically available

*** Variables ***
${URL}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}      chrome
@{NAMES}        Alice    Bob    Charlie

*** Test Cases ***
Test Case 1 - Logging And Variables
    Log To Console    Starting Test Case 1
    Log    Opening browser using BuiltIn keywords
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    OrangeHRM
    Log    Browser title verified successfully
    Close Browser
    Log To Console    Test Case 1 Completed

Test Case 2 - List Variable Usage
    Log To Console    Starting Test Case 2
    Log    Printing list values
    FOR    ${name}    IN    @{NAMES}
        Log To Console    User: ${name}
    END
    Log To Console    Test Case 2 Completed
