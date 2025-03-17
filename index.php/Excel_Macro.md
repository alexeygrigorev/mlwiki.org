---
title: "Excel Macro"
layout: default
permalink: /index.php/Excel_Macro
---

# Excel Macro


## Удаляет все пустые строки на всех листах

```tera term macro
Sub DeleteBlanks()

    Application.ScreenUpdating = False

    For Each s In Sheets
        TotalRows = s.UsedRange.Rows.Count
        For i = TotalRows To 1 Step -1
           If (s.Cells(i, 1) = "") Then
                s.Rows(i).Delete
           End If
        Next i
    Next

    Application.ScreenUpdating = True

End Sub
```

## Удалить все строки, содержащие выражение

```maple
Sub RemoveRowsWithSymbol()
    Application.ScreenUpdating = False

    Set r = ActiveSheet.UsedRange
    Set c = r.Find("}", LookIn:=xlValues)

    Do While Not c Is Nothing
        r.Rows(c.Row).Delete
        Set c = r.Find("}", LookIn:=xlValues)
    Loop

    Application.ScreenUpdating = True
End Sub
```

[Category:Scripts](Category_Scripts)
[Category:VBA](Category_VBA)
[Category:Snippets](Category_Snippets)