"""
    fråga 1: Iterera över projekten, kontrollera om Erik har arbetat på dem, 
    och spåra det projekt där han spenderat mest tid

    fråga 2: igen Iterera över projekten kontrollera om Lina har arbetat mer än 30 timmar,
    och om så är fallet, lägg till projektet i en ny dictionary
"""

projekt_data = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}
mest_tid = 0
best_project  = ""
lina_project = {}
#fråga 1:  iterate
for  project, employee in projekt_data.items():
    if("Erik" in employee):
        if(employee["Erik"] > mest_tid):
            mest_tid = employee["Erik"]
            best_project = project

print(best_project)
#fråga 2: 
for  project, employee in projekt_data.items():
    if("Lina" in employee and employee["Lina"] > 30):
        lina_project[project] = employee["Lina"]

print(lina_project)