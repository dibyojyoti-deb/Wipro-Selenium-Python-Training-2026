*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://demoqa.com/automation-practice-form
${BROWSER}        chrome

*** Test Cases ***
Automate Browser Form
    [Documentation]    Interacts with Textbox, Radio, Checkbox, and Dropdown.
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    0.5 seconds

    # 1. Interaction: Text box
    Wait Until Element Is Visible    id:firstName    10s
    Input Text      id:firstName    Robot
    Input Text      id:lastName     User

    # 2. Interaction: Radio button (Gender)
    # Using Javascript click because this site has overlapping labels
    Execute Javascript    document.getElementById('gender-radio-1').click()

    # 3. Interaction: Check box (Hobbies)
    Execute Javascript    document.getElementById('hobbies-checkbox-1').click()

    # 4. Interaction: Drop-down (State)
    # Scrolling down to ensure element is in view
    Execute Javascript    window.scrollTo(0, 500)
    # Interaction with a modern div-based dropdown
    Click Element    id:state
    Wait Until Element Is Visible    xpath://div[text()='NCR']    5s
    Click Element    xpath://div[text()='NCR']

    # 5. Built-in: Sleep
    Sleep    2s

    # 6. Built-in: Should Be Equal (Validation)
    ${val}=    Get Element Attribute    id:firstName    value
    Should Be Equal    ${val}    Robot

    # 7. Built-in: Run Keyword If
    Run Keyword If    '${val}' == 'Robot'    Log To Console    \nValidation Successful!

    # 8. Close Browser
    [Teardown]    Close Browser