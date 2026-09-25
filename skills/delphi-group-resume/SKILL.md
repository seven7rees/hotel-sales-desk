---
name: delphi-group-resume
description: Use to produce a group resume (the operations handoff for a group's rooms and department logistics) from Delphi, using the property's native resume merge template, then complete the sections the template leaves blank.
---

# Group resume

Read `.hotel-desk/property.yaml` first.

## Scope
The resume covers **guest rooms and department logistics**: arrival pattern, housing method, room block by night, VIPs, billing, master account, parking, front desk, housekeeping, engineering, security and AV notes.
It does **not** repeat menus or covers. The team runs events off the BEO. Do not fail a resume for missing F&B detail.

## 1. Prepare the booking
Fill these in Delphi before merging, or the merge prints blanks:
- `HousingMethodName__c` (the text field, not the lookup)
- Guest room notes, the contact's phone and address, the event classification
Confirm any value you did not read from Delphi with the user.

## 2. Merge
1. The user is logged in. If you see a login page, stop and ask.
2. Merge page, select `templates.group_resume`, choose DOC output, Generate.
3. Download the new file from the new BookingDocument's attachments. Never reuse an older download.

## 3. Room grid
- Show **agreed** rooms by night unless the user asks for pickup. Label which one it is.
- Include every room type, zeros included, so operations can see what is not held.
- Wrap long stays at three nights per block for readability.

## 4. Complete the missing sections
Add what the template leaves out (VIPs, special requests, parking, payment method, master account routing, one row per department, footer date) with python-docx. MERGEFIELD instructions can be split across runs, so match field codes carefully.

## 5. Check and deliver
- Diff the merged text against the completed version. Nothing from the merge may be lost.
- Never add content that is not in Delphi or confirmed by the user.
- Convert to PDF (Word or LibreOffice) and save under `files.beo_root` with the property's naming convention.
