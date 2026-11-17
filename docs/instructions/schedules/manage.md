# Managing and Editing Schedules

Open a schedule from the **Schedules** page. The editor has a **Schedule** panel and a **Manoeuvre** panel beside a 3D view of the template. If you are not allowed to edit the schedule the controls are disabled.

## Schedule panel

- **Schedule Properties** (expand to open): name, category, visibility, type and validity dates, with **Save** to keep changes, **Delete** (after confirmation) and **Edit manoeuvres**.
- **Save** writes the whole schedule to the database ("Schedule saved successfully!").
- **Clear** closes the schedule and returns to the schedule list.
- Administrators also see **Aresti** and **Definition** buttons that download the schedule as files.
- The manoeuvre list has **Add Manoeuvre** (adds an empty manoeuvre starting where the previous one ends) and **Read OLAN** (paste an OLAN string, then click **Read OLAN**). A bin icon deletes a manoeuvre.

## Manoeuvre panel

Select a manoeuvre in the list to edit it:

- **Short Name**, **Long Name** and **K Factor**.
- **Entry** and **Exit**: **Height**, **Direction**, **Orientation** and **Position** of the box location.
- **Elements**: the element list for the manoeuvre. You can append an element (or a centre point), insert one above an existing element, delete elements, and edit each element's required and optional parameters.
- **Combination Parameters** and **Comparison Parameters**: parameters shared between elements of the manoeuvre, used to compare elements with each other. Create, edit and delete them with the buttons beside each parameter.

Changed elements are marked **Updated** until you save. The 3D view redraws the template as you edit, and you can plot the whole schedule or one manoeuvre.

## Starting from a file

If no schedule is open the editor offers an **Input Mode**: **Open Aero** (OLAN), **Database**, **Manual** or **JSON**.
