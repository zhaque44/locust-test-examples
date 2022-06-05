from locust import HttpLocust, TaskSet, task, between


class SomeTest(TaskSet):
    """
    A locust class takes in TaskSet as an argument: which is defining a set of tasks that a Locust script will execute
    During run time a TaskSet will pick a task from the @task decorator, execute it, and then sleep for the
    number of seconds returned by it’s wait_time function.
    """

    _scopes = [
    "experiments:read",
    "experiments:write",
    ]

    def on_start(self):
        """During run time the on_start method is invoked by the Locust script executor, before any Locust task starts.
        A good example would be either authenticating the user, or making sure a location is eligible for an
        experiment.
        :param self represents its instance within this function
        example:
        self.client.post(
        "https://pitukia.com",
        data={
        "grant_type": "password",
        "username": username,
        "password": password,
        "scope": " ".join(_scopes),
        },
        headers={"x-caller-id": "aws-caller"},
        """
    pass

    def on_stop(self):
        """
        During run time the on_stop method is used for cleanup, after all tasks have been run. A good example of that
        would be deleting recommended seedProducts from rec-cab-sync.
        :param self represents its instance within this function
        example:
        self.client.delete(
        f"{utils.base_url}/v1/internal/agronomicPortfolioProducts/sync/{product}",
        headers=headers,)
        """
    pass

    @task(1)
    def profile(self):
        """
        @task: to declare the flow of your tests use the @task decorator which should be inline to the class that has
        the TaskSet subclass passed in.
        requests: Locust is using the requests library under the hood to make http POST/GET/PUT/DELETE requests.
        """
    self.client.get(
    url="http://baseurl/endpoint"
    )


class WebsiteUser(HttpLocust):
    """
    The HttpLocust subclass allows you to specify the wait time between
    the execution of tasks.
    task_set: The task_set attribute will point to a TaskSet class which defines the script that is going to run.
    wait_time: used to determine for how long a virtual user will wait between executing tasks.
    between: between(min_wait, max_wait)
    example:
    wait between 3 and 6 seconds after executing each task
    """

  task_set = SomeTest
  wait_time = between(3, 6)
