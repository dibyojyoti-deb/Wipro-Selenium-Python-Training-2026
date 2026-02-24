*** Settings ***
Documentation     Resource file for Capstone Project common keywords
Library           SeleniumLibrary
Library           ../keywords/StealthLib.py
Library           OperatingSystem
Library           Collections
Library           String

*** Variables ***
${LOG_FILE}         ${CURDIR}/../reports/robot_terminal_output.txt
${SCREENSHOT_DIR}    ${CURDIR}/../screenshots/Robot screenshots
${DATA}             ${EMPTY}
${BROWSER}          chrome

*** Keywords ***
Setup Everything
    [Arguments]    ${csv_path}    ${browser}=${BROWSER}
    Create Directory    ${SCREENSHOT_DIR}
    Create Directory    ${CURDIR}/../reports
    Set Screenshot Directory    ${SCREENSHOT_DIR}
    ${raw_dict}=    Get Csv Data    ${csv_path}
    Set Suite Variable    ${DATA}    ${raw_dict}
    ${start_url}=    Get From Dictionary    ${DATA}    base_url
    Open Stealth Browser    ${start_url}    ${browser}
    # FIX: Maximize window to prevent elements from collapsing into mobile view
    Maximize Browser Window
    Create File    ${LOG_FILE}    ROBOT EXECUTION LOG\n============================\n

Finalize Execution
    Close Stealth Browser
    ${suite_status}=    Get Variable Value    ${SUITE_STATUS}
    IF    '${suite_status}' == 'PASS'
        # FIX: Updated success message
        ${msg}=    Set Variable    \n============================ All 25 tests have passed =======================\n
    ELSE
        ${msg}=    Set Variable    \n[ROBOT EXECUTION END] SOME TESTS FAILED\n
    END
    Log To Console    ${msg}
    Append To File    ${LOG_FILE}    ${msg}

Log Test Result
    ${msg}=    Catenate    ${TEST STATUS}: ${TEST NAME}\n
    Append To File    ${LOG_FILE}    ${msg}

Ensure Home
    ${base}=    Get From Dictionary    ${DATA}    base_url
    Go To    ${base}
    # Pause if Cloudflare intercepts the initial page load
    ${title}=    Get Title
    IF    'Just a moment' in '${title}'
        Sleep    5s
    END
    # Increased wait to allow the logo to render after the bot-check
    Wait Until Element Is Visible    class:header-logo    25s
    
Clear Notification Bar
    ${present}=    Run Keyword And Return Status    Element Should Be Visible    class:bar-notification
    IF    ${present}
        Run Keyword And Ignore Error    Click Element    css:.bar-notification .close
        Wait Until Element Is Not Visible    class:bar-notification    10s
    END

Logout If Needed
    ${status}=    Run Keyword And Return Status    Element Should Be Visible    class:ico-logout
    IF    ${status}
        Click Element    class:ico-logout
        Wait Until Element Is Visible    class:ico-register    10s
    END

Generate Random Email
    ${random}=    Generate Random String    5    [LETTERS]
    ${email}=     Catenate    SEPARATOR=    ${DATA}[first_name]    ${random}    @example.com
    RETURN    ${email}

JS Click
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    15s
    ${element}=    Get WebElement    ${locator}
    Execute Javascript    arguments[0].scrollIntoView({block: 'center'});    ARGUMENTS    ${element}
    Sleep    0.5s
    Execute Javascript    arguments[0].click();    ARGUMENTS    ${element}