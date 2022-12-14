class AnonymousSurvey:
    """Сбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит опрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ на вопрос."""
        self.responses.append(new_response)

    def show_results(self):
        """Выводит все полученные ответы."""
        print("Survey result: ")
        for response in self.responses:
            print(f"- {response}")

