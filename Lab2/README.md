# Lab 2: Agile Backlog Creation & Sprint Simulation in Jira

Scenario: **Corporate Mental Wellness & Counseling Platform** (from Lab 1).

The Lab 1 functional requirements, actors and use cases were turned into
Epics and User Stories, then prioritised and estimated with story points.
These were used to run two one-week sprints in a company-managed Scrum project
in Jira.

## Files

| File | Description |
|------|-------------|
| `backlog.md` | Epics, user stories, priorities, story points, sprint plan and traceability to Lab 1 |
| `jira_import.csv` | The same backlog (5 epics, 20 stories) ready to import into Jira |
| `reflection.md` | Answers to the reflection questions |

## Backlog at a glance

| Epic | Stories | Points |
|------|---------|--------|
| E1 Anonymous Identity & Access | 4 | 13 |
| E2 Therapist Directory & Booking | 6 | 29 |
| E3 Counseling Sessions & Notifications | 4 | 15 |
| E4 Anonymous Wellbeing Tracking | 3 | 12 |
| E5 HR Wellness Programme | 3 | 13 |
| **Total** | **20** | **82** |

| Sprint | Goal | Points |
|--------|------|--------|
| Sprint 1 | An employee can sign in anonymously, find a therapist and book a session | 27 |
| Sprint 2 | Booked sessions can be attended online, confirmed and measured with check-ins | 23 |

## Importing the backlog into Jira

1. Create the project as in the handout: **Software development → Scrum →
   Company-managed**.
2. Go to **Settings (gear icon) → System → External system import → CSV**
   and upload `jira_import.csv`. You need to be a Jira admin, which you are on
   a site you created yourself.
3. Choose your project, then map the columns:

   | CSV column | Jira field |
   |------------|------------|
   | Issue Id | Issue ID (Work item ID) |
   | Parent Id | Parent ID (Parent) |
   | Issue Type | Issue Type (Work type) |
   | Summary | Summary |
   | Description | Description |
   | Priority | Priority |
   | Story Points | Story Points (or Story point estimate) |
   | Labels | Labels |

4. Run the import, then check in **Backlog** (press **E** for the epic panel)
   that every story sits under its epic.

The importer only creates the items. Creating the sprints, moving stories to
Done and completing the sprints still has to be done on the board, as in steps
6-7 of the handout.
