*** Variables ***
@{USERS}    admin    user
@{PWDS}     admin123    user123

*** Test Cases ***
FOR Loop Zip
    # Use $ instead of @ to pass the lists themselves
    FOR    ${u}    ${p}    IN ZIP    ${USERS}    ${PWDS}
        Log    ${u} / ${p}
    END