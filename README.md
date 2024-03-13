## QVariableStyleSheet
QVariableStyleSheet is a small library that enables CSS-compliant variable processing in your Qt Stylesheets. 

## Usage (C++)
```
    //Include the header
    #include "QVariableSytleSheet/qvariablestylesheet.h"
    
    //Load QSS data from file or resource
    QString theme = file.readAll();

    /*
        Declare the variable style sheet.
        Data is set in the constructor or
            through the sheet.setStyleSheet() function
    */
    QVariableStyleSheet sheet(theme);
    QString processedTheme = sheet.process();
```

## Usage (QtStyleSheet)
```
    /*
        Declare variable data in the :root block.
        According to CSS: each variable MUST start with "--"
    */
    :root
    {
        --window-backgound-color: #141414;
        --widget-background-color: #242424;
        --widget-border-size: 2;
        --widget-border-color-1: #4b4b4b;
        --widget-border-color-2: #141414;
        --subwidget-border-color-1: #4b4b4b;
        --subwidget-border-color-2: #141414;
        --subwidget-background-color: #141414;
        --page-background-color: #111111; 
    }
    
    /*
        Use variables in your style blocks
    */
    QWidget
    {
        background-color: var(--widget-background-color);
        border-left: var(--widget-border-size) solid black;
        border-top: var(--widget-border-size) solid black;
        border-right: var(--widget-border-size) solid black;
        border-bottom: var(--widget-border-size) solid black;
        border-right-color: qlineargradient(x1:1, y1:0, x2:0, y2:0, stop: 0 var(--widget-border-color-1), stop: 1 var(--widget-border-color-2));
        border-left-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 var(--widget-border-color-1), stop: 1 var(--widget-border-color-2));
        border-top-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 var(--widget-border-color-1), stop: 1 var(--widget-border-color-2));
        border-bottom-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop: 0 var(--widget-border-color-1), stop: 1 var(--widget-border-color-2));
    }
```