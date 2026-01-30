*** Settings ***
Documentation     Environment Validation Suite (Final Version)
Library           SeleniumLibrary
Library           Collections

*** Test Cases ***
Validate Automation Environment
    [Documentation]    Verifies Python, Robot, and Selenium via internal modules.
    
    # 1. Verify Python version
    ${py_version} =    Evaluate    sys.version    modules=sys
    Log To Console    \nPython Version: ${py_version}

    # 2. Verify Robot Framework version via the version module
    ${rf_version} =    Evaluate    robot.version.get_full_version()    modules=robot.version
    Log To Console    Robot Framework Version: ${rf_version}

    # 3. Verify SeleniumLibrary Version
    ${sel_version} =    Evaluate    selenium.__version__    modules=selenium
    Log To Console    SeleniumLibrary Version: ${sel_version}
    
    Log To Console    \n--- ALL DEPENDENCIES VERIFIED ---
    Log To Console    Status: READY FOR AUTOMATION