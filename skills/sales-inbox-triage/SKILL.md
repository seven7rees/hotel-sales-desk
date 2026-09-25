---
name: sales-inbox-triage
description: Use to triage a hotel sales or catering inbox. Sorts the last day of mail into five buckets, drafts threaded replies in the property's voice with the correct font and signature, and files answered threads. Drafts only, never sends.
---

# Sales inbox triage

Read `.hotel-desk/property.yaml` (the `email:` section) first.

## 1. Pull
Search the inbox for the last 24 hours (or the window the user gives). Read bodies in batches of five.

## 2. Check before you draft
For every thread that looks like it needs a reply:
- **Sent Items (last 14 to 30 days):** match on the normalized subject. If the user already replied after the latest inbound message, it is answered.
- **Drafts:** if a draft already exists on the thread, do not create a second one. Report it.

## 3. Sort into five buckets
| Bucket | Meaning |
|---|---|
| Reply now | A client is waiting on a decision, a date or a contract |
| Reply today | Needs an answer, not urgent |
| Reply this week | Low stakes |
| File | No reply owed |
| Escalate | Complaint, legal, press, ownership, a pricing exception, or anything above the user's authority |

Escalations get no drafted reply. Name who should own it.

## 4. Draft
- Always a true threaded reply on the original message (`MailItem.Reply()` or `ReplyAll()`). Never a new email with "RE:" typed in. Keep the full quoted thread.
- Address the recipient by name in the first line. Lead with the answer. End with one clear next step.
- Use `email.font` at `email.font_size_pt` and append the `email.signature_file`. Graph-based draft tools strip inline styles, so finish every draft with an Outlook desktop (COM) pass: insert after `<body>`, then verify with the plain-text `.Body`.
- Remove every phrase in `email.banned_phrases`.
- Never commit to rates, dates, comps, upgrades or refunds that are not confirmed in Delphi.
- If `email.review_before_ready` is true, run a fresh-context review of the text BEFORE creating the draft.

## 5. File
- Answered client threads go to `email.folders.answered_groups`.
- No-reply-needed mail goes to `email.folders.no_reply_needed`.
- Meeting requests stay in the inbox.
- Run one COM script at a time. Use `.Move()`.

## 6. Report
Give the user a compact table: bucket, sender, subject, action taken, draft status. Nothing is sent.
