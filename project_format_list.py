
def get_project_info(input_prompt):
    """
    Function to collect project names and descriptions from a client's project list from a spreadsheet.
    """
    values = []
    while True:
        user_input = input(input_prompt + ' (press return finish):\n')
        if not user_input:
            break
        values.append(user_input)
    return values

def projectlist_formatter(project_names, project_descriptions):
    """Format lists of project names/descriptions"""
    project_list = zip(project_names, project_descriptions)
    for project, desc in project_list:
        print(f"\n{project}: \n{desc}")

names_values = get_project_info('Enter project names')
descriptions_values = get_project_info('Enter project descriptions (multiline)')

projectlist_formatter(project_names=names_values, project_descriptions=descriptions_values)


# Test 