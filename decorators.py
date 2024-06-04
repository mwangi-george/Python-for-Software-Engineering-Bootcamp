def show_available_books(func):
    def wrapper():
        print("We don't have any books yet!")
        func()

    return wrapper


@show_available_books
def respond_to_reader():
    """The @ symbol ensures that this function is passed as input to show_available_books function

    When we call response_to_reader, show_available_books is also called with response_to_reader as input
    """
    print("Return in a week or two!")


respond_to_reader()


@show_available_books
def notify_reader():
    print("You can enlist and we'll call you when we have books")


notify_reader()


def show_enlisted_members(func):
    def wrapper(*args, **kwargs):
        print("No enlisted members yet!")
        func(*args, **kwargs)


@show_enlisted_members
def enlist_member(first_name: str, last_name: str):
    print(f"Hi {first_name}👋, You are our first member")
    return first_name, last_name


enlist_member("George", "Mwangi")
