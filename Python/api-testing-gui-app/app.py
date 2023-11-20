from src import Model, View, Controller


def start_app():
    model = Model()
    view = View("API-Testing-App")
    controller = Controller(model, view)
    view.set_controller(controller)
    view.start_view()
    view.root.mainloop()


if __name__ == "__main__":
    start_app()
