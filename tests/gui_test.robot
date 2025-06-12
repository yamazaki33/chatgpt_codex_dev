*** Settings ***
Library    ../gui_test_utils.py

*** Test Cases ***
Sample GUI Comparison
    # このテストはサンプルです。HMI を起動してスクリーンショットを取得し、
    # 期待画像との比較を行います。
    ${actual}=    Capture    sample
    ${result}=    Compare Screenshots    expected/sample.png    ${actual}    diff.png    threshold=10
    Should Be True    ${result}

