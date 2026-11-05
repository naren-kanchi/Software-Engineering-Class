# Lab 2: Reflection

**1. Did your estimations reflect the actual effort?**

Mostly, in relative terms. The stories estimated at 8 points (2.2 booking,
3.1 telehealth session) are the ones with the most steps and outside
dependencies: booking has to avoid double-booking (UC-03 steps 4-7) and the
session depends on the telemedicine service. The 2-point stories are single
rules or screens. The weakest estimates are the privacy stories (1.1 pseudo-ID,
5.1 aggregated dashboard). Their size depends on how strictly "never
traceable" (FR-001, FR-006) is interpreted, and that uncertainty is why they
were rounded up. Because the sprint was simulated, no real development effort
was measured. What the lab tested was whether the estimates were consistent
with each other, and they were.

**2. Was your backlog well-prioritized?**

Yes. The High stories form the core flow from Lab 1: get an anonymous ID,
find a therapist, book, attend and record the effect. That flow can be
delivered in two sprints. Medium stories make that flow more reliable or
complete (login for staff, the "slot taken" alternate flow, confirmations).
Low stories are improvements the platform can work without, such as time
zones, which the SRS itself rates Low (NFR-002). One trade-off: 2.5
(reschedule/cancel) was left for a later sprint even though users would
expect it soon after booking. Booking first, then managing bookings, kept
Sprint 1 within capacity.

**3. How did your simulated sprint align with your plan?**

Both sprints contained exactly the planned stories: 27 points in Sprint 1
and 23 points in Sprint 2, against a total backlog of 82 points. The order of
work followed the backlog ranking: High-priority stories were moved to In
Progress first, and stories that depend on others (for example 2.2 booking
needs 1.1 pseudo-IDs and 2.4 availability) were moved after the stories they
depend on. All stories were completed, so nothing was carried over to the
next sprint. Since the sprint was simulated in minutes instead of over a
week, the timing does not reflect real work, only the order and scope.

**4. What insights did the burndown chart give about your team's capacity?**

The remaining-work line did not follow the grey guideline gradually. It
stayed flat and then dropped in steps, as each story was moved to Done in the
space of a few minutes. In a real sprint, a chart like this would point to
work being closed in batches near the end of the sprint, or stories being too
large to finish steadily. That is a sign to split stories (for example the
8-point booking story) so progress shows up day by day. Completing 27 and
then 23 points suggests a velocity of about 25 points per one-week sprint. At
that rate, the remaining 32 points need one to two more sprints.
