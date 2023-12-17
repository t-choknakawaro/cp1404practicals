import datetime
from project import Project
FILENAME = 'projects.txt'
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    projects = load_file()
    print(MENU)
    choice = input('>>> ').lower()
    while choice != 'q':
        if choice == 'l':
            projects = load_file()
        elif choice == 's':
            saving_file(projects)
        elif choice == 'd':
            complete, incomplete = sorting_project(projects)
            display_project(complete, incomplete)
        elif choice == 'f':
            filter_dates = []
            filter_date = get_filter_date()
            process_filter_date(filter_date, filter_dates, projects)
            display_filter_date(filter_dates)
        elif choice == 'a':
            print("Let's add a new project")
            completion, cost, name, priority, start_date = get_project()
            adding_project(completion, cost, name, priority, projects, start_date)
        elif choice == 'u':
            display_projects_with_count(projects)
            updating_project(projects)
        choice = input('>>> ').lower()


def display_filter_date(filter_dates):
    for project in filter_dates:
        project = Project(project[0], project[1], project[2], project[3], project[4])
        print(project)


def process_filter_date(filter_date, filter_dates, projects):
    for project in projects:
        date = datetime.datetime.strptime(project[1], '%d/%m/%Y')
        if date > filter_date:
            filter_dates.append(project)


def get_filter_date():
    filter_date = datetime.datetime.strptime(input('Show projects that start after date (dd/mm/yy) '), '%d/%m/%Y')
    return filter_date


def saving_file(projects):
    with open(FILENAME, 'r+', encoding='utf-8-sig') as out_file:
        firstline = out_file.readline()
        out_file.seek(len(firstline) + 1)
        out_file.truncate()
        for project in projects:
            out_file.write(f'{project[0]}\t{project[1]}\t{project[2]}\t{project[3]}\t{project[4]}\n')


def updating_project(projects):
    project_choice = int(input('Project choice: '))
    new_percentage = input('New percentage: ') or projects[project_choice][4]
    new_priority = input('New priority: ') or projects[project_choice][2]
    projects[project_choice][4] = new_percentage
    projects[project_choice][2] = new_priority
    project = Project(projects[project_choice][0], projects[project_choice][1], projects[project_choice][2],
                      projects[project_choice][3], projects[project_choice][4])
    print(project)


def display_projects_with_count(projects):
    for count, project in enumerate(projects):
        project = Project(project[0], project[1], project[2], project[3], project[4])
        print(f'{count} {project}')


def display_project(complete, incomplete):
    print('Complete project:')
    for project in complete:
        print(project)
    print("Incomplete project:")
    for project in incomplete:
        print(project)


def sorting_project(projects):
    incomplete = []
    complete = []
    for project in projects:
        project = Project(project[0], project[1], project[2], project[3], project[4])
        if project.is_completion():
            complete.append(project)
        else:
            incomplete.append(project)
    return complete, incomplete


def load_file():
    projects = []
    with open(FILENAME, 'r', encoding='utf-8-sig') as in_file:
        for line in in_file:
            part = line.strip('\n').split('\t')
            projects.append(part)
        projects.pop(0)
    return projects


def adding_project(completion, cost, name, priority, projects, start_date):
    project = []
    project.extend([name, start_date.strftime("%d/%m/%Y"), cost, priority, completion])
    projects.append(project)


def get_project():
    name = check_blank_input("Name: ")
    start_date = datetime.datetime.strptime(input('Start date (dd/mm/yy) '), '%d/%m/%Y')
    cost = float(input('Cost: '))
    priority = check_valid_value('Priority: ')
    completion = check_valid_value('Completion rate: ')
    return completion, cost, name, priority, start_date


def check_blank_input(text):
    name = input(text)
    while name == '':
        print('Input cannot be blank')
        name = input(text)
    return name


def check_valid_value(text):
    is_valid_input = False
    while not is_valid_input:
        try:
            value = int(check_blank_input(text))
            is_valid_input = True
        except ValueError:
            print('Invalid input')
        return value

main()
