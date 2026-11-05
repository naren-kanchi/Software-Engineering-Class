# Lab 2: Product Backlog — Corporate Mental Wellness & Counseling Platform

The backlog is built from the Lab 1 work in [`../Lab1`](../Lab1): the SRS
requirements (FR-001 to FR-006, NFR-001, NFR-002), the actors and use cases
(UC-01 to UC-08) and the UC-03 "Find & Book Counseling Session" flow.

## Summary

| Priority | Stories | Points |
|----------|---------|--------|
| High | 8 | 40 |
| Medium | 7 | 28 |
| Low | 5 | 14 |
| **Total** | **20** | **82** |

## Epics and User Stories

### Epic 1: Anonymous Identity & Access

**Description:** Let employees use the platform under a random pseudo-ID that can never be traced back to their corporate identity, and let therapists and admins sign in securely.  
**Lab 1 source:** FR-001, FR-006, NFR-001, UC-01  
**Total:** 4 stories, 13 story points

| Story | As a | I want | So that | Priority | Points | Lab 1 source |
|-------|------|-----------|---------|----------|--------|--------------|
| **1.1** Anonymous pseudo-ID on sign in | employee | the platform to give me a random pseudo-ID when I enter it | I can use counseling services without my corporate email or employee ID being revealed | High | 5 | FR-001, FR-006, NFR-001 |
| **1.2** Continue with my existing pseudo-ID | employee | to choose to continue with a pseudo-ID I used before | my session history and progress stay together | High | 3 | NFR-001, FR-003 |
| **1.3** Therapist sees pseudo-ID only | therapist | to see only the client's pseudo-ID on my dashboard | the employee's identity stays confidential | High | 3 | FR-001 |
| **1.4** Therapist and admin login | therapist or HR admin | to log in with my own account | only authorised staff can manage availability and the programme | Medium | 2 | UC-01 |

Acceptance criteria:

- **1.1:** A new random ID is generated in a few milliseconds; no corporate identifier is stored with it.
- **1.2:** Entering a previously issued ID restores its history; nothing else links it to the employee.
- **1.3:** Therapist dashboard and appointment details show the pseudo-ID and no other identifier.
- **1.4:** Login required for therapist and admin pages; wrong credentials are rejected.

### Epic 2: Therapist Directory & Booking

**Description:** Let employees find a licensed therapist by speciality and book, reschedule or cancel a session, while therapists manage their own availability.  
**Lab 1 source:** FR-002, NFR-002, UC-03, UC-05, UC-07  
**Total:** 6 stories, 29 story points

| Story | As a | I want | So that | Priority | Points | Lab 1 source |
|-------|------|-----------|---------|----------|--------|--------------|
| **2.1** Browse therapists by speciality | employee | to browse licensed therapists filtered by speciality and availability | I can pick someone suited to what I need | High | 3 | FR-002, UC-03 (step 2) |
| **2.2** Book an available session | employee | to choose a therapist, date, time and session mode and confirm the booking | I have a confirmed counseling appointment | High | 8 | UC-03 (steps 1-9) |
| **2.3** Handle a slot that was just taken | employee | to be told when my chosen slot is no longer free and see the latest slots | I can quickly pick another time instead of getting an error | Medium | 3 | UC-03 (alternate flow 3a) |
| **2.4** Manage my availability | therapist | to add, change and remove my available time slots | employees can only book times when I can actually take sessions | High | 5 | UC-05 |
| **2.5** Reschedule or cancel an appointment | employee | to reschedule or cancel a booked appointment | I can fit counseling around my work | Medium | 5 | UC-07 |
| **2.6** Show times in my own time zone | employee in a global office | appointment times to be shown in my local time zone | I don't miss sessions because of time zone differences | Low | 5 | NFR-002 |

Acceptance criteria:

- **2.1:** List shows speciality, availability and contact options; filter by speciality works.
- **2.2:** Booking is recorded, the slot is removed from availability and booking details are shown.
- **2.3:** If the slot is taken during booking, a message is shown and the slot list refreshes.
- **2.4:** Changes appear in the booking list immediately; booked slots cannot be deleted.
- **2.5:** Cancelled slots return to the therapist's availability; both sides see the change.
- **2.6:** Times are stored in UTC and shown in the viewer's time zone for employee and therapist.

### Epic 3: Counseling Sessions & Notifications

**Description:** Run telehealth counseling sessions and keep employees informed about their appointments through confirmations and reminders.  
**Lab 1 source:** UC-04, UC-08, UC-03 (step 8 / 8a)  
**Total:** 4 stories, 15 story points

| Story | As a | I want | So that | Priority | Points | Lab 1 source |
|-------|------|-----------|---------|----------|--------|--------------|
| **3.1** Join a telehealth session | employee | to join my counseling session online from the platform | I can attend from wherever I am | High | 8 | UC-04 |
| **3.2** Booking confirmation notification | employee | to get a confirmation when my booking is made | I know the appointment went through and have the details | Medium | 3 | UC-08, UC-03 (step 8) |
| **3.3** Retry failed notifications | employee | my booking to stay active and be shown in the portal if the notification fails | a notification outage never loses my appointment | Low | 2 | UC-03 (alternate flow 8a) |
| **3.4** Session reminders | employee | a reminder before my session starts | I don't forget my appointment | Low | 2 | UC-08 |

Acceptance criteria:

- **3.1:** Join link is active at the booked time for both participants via the telemedicine service.
- **3.2:** Confirmation is sent through the notification service right after booking.
- **3.3:** Failed notifications are marked for retry; booking details stay visible in the portal.
- **3.4:** Reminder is sent a set time before the session.

### Epic 4: Anonymous Wellbeing Tracking

**Description:** Record how an employee feels before and after each session against their pseudo-ID only, so they can follow their own progress without ever being identified.  
**Lab 1 source:** FR-003, FR-004, FR-005  
**Total:** 3 stories, 12 story points

| Story | As a | I want | So that | Priority | Points | Lab 1 source |
|-------|------|-----------|---------|----------|--------|--------------|
| **4.1** Pre- and post-session check-in | employee | to rate how I feel before and after each session | the effect of each session can be measured | High | 5 | FR-004 |
| **4.2** View my progress over time | employee | to see my check-in results over time under my pseudo-ID | I can follow my own long-term wellbeing | Medium | 5 | FR-003 |
| **4.3** Optional questions, no pressure | employee | every wellbeing question to be optional | I am never pressured into sharing more than I want to | Medium | 2 | FR-005 |

Acceptance criteria:

- **4.1:** Check-in is stored against the pseudo-ID only and is linked to the session.
- **4.2:** Progress chart shows only data for the current pseudo-ID.
- **4.3:** Every question can be skipped; skipping never blocks booking or sessions.

### Epic 5: HR Wellness Programme

**Description:** Give HR an aggregated, non-identifying view of the pilot's effect on the workforce and a place to share wellness resources.  
**Lab 1 source:** FR-004, UC-06  
**Total:** 3 stories, 13 story points

| Story | As a | I want | So that | Priority | Points | Lab 1 source |
|-------|------|-----------|---------|----------|--------|--------------|
| **5.1** Aggregated wellbeing dashboard | HR / wellness admin | to see aggregated pilot results and overall workforce wellbeing trends | I can judge the programme without singling out any employee | Medium | 8 | FR-004 |
| **5.2** Publish wellness resources | HR / wellness admin | to publish articles and self-help resources | employees have support between sessions | Low | 3 | UC-06 |
| **5.3** Read wellness resources | employee | to browse wellness resources anonymously | I can get help without booking a session | Low | 2 | UC-06 |

Acceptance criteria:

- **5.1:** Only aggregates are shown, and only for groups above a minimum size.
- **5.2:** Admin can add, edit and remove resources.
- **5.3:** Resources can be read without any identifying information being recorded.

## Prioritisation

Priorities follow user impact and the Lab 1 SRS priorities:

- **High:** without these stories the platform cannot do its core job, an
  employee booking and attending counseling anonymously. They cover the
  privacy requirements (FR-001, FR-006), the therapist directory (FR-002), the
  main booking flow (UC-03), therapist availability (UC-05), the session itself
  (UC-04) and measuring its effect (FR-004).
- **Medium:** these stories make the core flow reliable or complete it: staff
  login, the "slot already taken" alternate flow, confirmations, rescheduling,
  optional questions (FR-005), personal progress (FR-003) and the HR dashboard.
- **Low:** useful, but the platform works without them: time zones (NFR-002 is
  Low in the SRS), notification retries, reminders and wellness resources.

The backlog in Jira is ranked High → Medium → Low, and by dependency within
each level (for example a pseudo-ID must exist before anything can be booked
against it).

## Story points

Story points use the Fibonacci scale (1, 2, 3, 5, 8, 13). They are relative:
a story is compared with the others for complexity, amount of work and
uncertainty, not converted from hours. The estimates are meant to be checked
with Planning Poker: discuss each story briefly, everyone shows a card at the
same time, and if the cards differ the highest and lowest voters explain their
reasoning before voting again.

| Points | Meaning | Examples |
|--------|---------|----------|
| 2 | Small, well understood, one screen or rule | 1.4 Login, 4.3 Optional questions, 3.3 Retry notifications |
| 3 | Small feature with some logic | 1.3 Pseudo-ID on therapist dashboard, 2.1 Browse therapists, 3.2 Confirmation |
| 5 | Several parts, or a privacy rule that must be exactly right | 1.1 Pseudo-ID generation, 2.4 Availability, 4.1 Check-ins, 2.6 Time zones |
| 8 | Complex, touches several parts of the system or an external service | 2.2 Booking flow, 3.1 Telehealth session, 5.1 Aggregated dashboard |

The stories that were hardest to estimate:

- **2.2 Book an available session (8, not 5):** booking has to validate the
  slot, create a provisional appointment, confirm it and update availability
  without double-booking (UC-03 steps 4-7).
- **1.1 Anonymous pseudo-ID (5, not 3):** generating a random ID is simple,
  but making sure nothing links it back to the employee (FR-001, FR-006) adds
  uncertainty.
- **5.1 Aggregated dashboard (8):** the reporting itself is straightforward,
  but guaranteeing that no individual can be singled out (minimum group sizes)
  makes it the riskiest story.

## Sprint plan

Both sprints are 1 week long. Sprint 1 takes the highest-priority stories that
make up the anonymous booking flow. Sprint 2 builds on it with sessions,
notifications and check-ins.

### Sprint 1 (1 week)

**Sprint goal:** An employee can sign in anonymously, find a therapist and book a session.

| Story | Priority | Points |
|-------|----------|--------|
| 1.1 Anonymous pseudo-ID on sign in | High | 5 |
| 1.2 Continue with my existing pseudo-ID | High | 3 |
| 1.3 Therapist sees pseudo-ID only | High | 3 |
| 2.1 Browse therapists by speciality | High | 3 |
| 2.2 Book an available session | High | 8 |
| 2.4 Manage my availability | High | 5 |
| **Total** | | **27** |

### Sprint 2 (1 week)

**Sprint goal:** Booked sessions can be attended online, confirmed and measured with check-ins.

| Story | Priority | Points |
|-------|----------|--------|
| 3.1 Join a telehealth session | High | 8 |
| 4.1 Pre- and post-session check-in | High | 5 |
| 1.4 Therapist and admin login | Medium | 2 |
| 2.3 Handle a slot that was just taken | Medium | 3 |
| 3.2 Booking confirmation notification | Medium | 3 |
| 4.3 Optional questions, no pressure | Medium | 2 |
| **Total** | | **23** |

### Left in the backlog

| Story | Priority | Points |
|-------|----------|--------|
| 2.5 Reschedule or cancel an appointment | Medium | 5 |
| 4.2 View my progress over time | Medium | 5 |
| 5.1 Aggregated wellbeing dashboard | Medium | 8 |
| 2.6 Show times in my own time zone | Low | 5 |
| 3.3 Retry failed notifications | Low | 2 |
| 3.4 Session reminders | Low | 2 |
| 5.2 Publish wellness resources | Low | 3 |
| 5.3 Read wellness resources | Low | 2 |
| **Total** | | **32** |

## Traceability to Lab 1

| Lab 1 item | Stories |
|------------|---------|
| FR-001 Anonymised pseudo-ID, therapist sees pseudo-ID only | 1.1, 1.3 |
| FR-002 Therapist list by speciality | 2.1 |
| FR-003 Anonymous long-term tracking | 1.2, 4.2 |
| FR-004 Before/after session feelings, workforce trends | 4.1, 5.1 |
| FR-005 No coercion of information | 4.3 |
| FR-006 Untraceable random ID | 1.1 |
| NFR-001 New ID each visit, option to keep the old one | 1.1, 1.2 |
| NFR-002 Time zone conversions | 2.6 |
| UC-01 Register / Login | 1.4 |
| UC-03 Find & Book Counseling Session | 2.1, 2.2, 2.3 (flow 3a), 3.2, 3.3 (flow 8a) |
| UC-04 Conduct Telehealth Session | 3.1 |
| UC-05 Manage Therapist Availability | 2.4 |
| UC-06 Access Wellness Resources | 5.2, 5.3 |
| UC-07 Manage Appointments | 2.5 |
| UC-08 Send Notifications | 3.2, 3.4 |

UC-02 (Manage Wellness Profile) is not a separate story: the only profile the
platform keeps is the anonymous pseudo-ID profile covered by 1.2 and 4.2.
