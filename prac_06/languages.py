from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)


def main():
    """Create and print names of dynamically typed ProgrammingLanguage."""
    python_lang = ProgrammingLanguage('Python', 'Dynamic', True, 1991)
    ruby_lang = ProgrammingLanguage('Ruby', 'Dynamic', True, 1995)
    visual_basic_lang = ProgrammingLanguage('Visual Basic', 'Static', False, 1991)

    languages = [python_lang, ruby_lang, visual_basic_lang]

    print('The dynamically typed languages are:')
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
