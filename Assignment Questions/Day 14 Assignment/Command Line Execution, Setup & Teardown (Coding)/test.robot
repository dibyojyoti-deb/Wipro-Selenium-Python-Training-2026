*** Settings ***
Documentation     A complete example of Setup, Teardown, and Tagging.
Suite Setup       Log To Console    --- INITIALIZING ENTIRE SUITE ---
Suite Teardown    Log To Console    --- TEARING DOWN ENTIRE SUITE ---
Test Setup        Log To Console    Step: Preparing Test Environment
Test Teardown     Log To Console    Step: Cleaning Up After Test

*** Variables ***
${MESSAGE}       Hello, Robot Framework!

*** Test Cases ***
Verify System Health
    [Tags]    Critical
    Log To Console    Executing: ${MESSAGE}
    Should Be Equal As Strings    ${MESSAGE}    Hello, Robot Framework!

Check Optional Feature
    [Tags]    Secondary
    Log To Console    Executing: Optional Feature Check
    No Operation