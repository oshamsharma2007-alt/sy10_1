


def report_decorator(func):

    # Wrapper function accepts any number of positional
    # and keyword arguments.
    # *args -> positional arguments
    # **kwargs -> keyword arguments
    def wrapper(*args, **kwargs):

        # Print report header
        print("=" * 60)
        print("           DYNAMIC REPORT GENERATOR")
        print("=" * 60)

        # Call the original function
        func(*args, **kwargs)

        # Print report footer
        print("=" * 60)
        print("             END OF REPORT")
        print("=" * 60)

    # Return the wrapper function
    return wrapper


# ----------------------------------------------------------
# Report Class
# ----------------------------------------------------------
# This class represents a report.
# A class is a blueprint for creating objects.
# ----------------------------------------------------------

class Report:

    # ------------------------------------------------------
    # Class Variable
    # ------------------------------------------------------
    # Shared by every object of this class.
    # If changed once, it changes for all objects.
    # ------------------------------------------------------
    company_name = "ABC Technologies Pvt. Ltd."


    # ------------------------------------------------------
    # Constructor (Magic Method)
    # ------------------------------------------------------
    # Automatically executes when an object is created.
    # Used to initialize object variables.
    # ------------------------------------------------------
    def __init__(self, title, author):

        # Instance Variable
        # Stores report title
        self.title = title

        # Instance Variable
        # Stores author name
        self.author = author

        # Empty list to store report contents
        self.contents = []


    # ------------------------------------------------------
    # Instance Method
    # ------------------------------------------------------
    # Adds one section into the report.
    # Every object has its own contents list.
    # ------------------------------------------------------
    def add_content(self, text):

        # Append new content into the list
        self.contents.append(text)


    # ------------------------------------------------------
    # Class Method
    # ------------------------------------------------------
    # Works with class variables.
    # Uses cls instead of self.
    # ------------------------------------------------------
    @classmethod
    def change_company(cls, new_company):

        # Update company name for all objects
        cls.company_name = new_company


    # ------------------------------------------------------
    # Static Method
    # ------------------------------------------------------
    # Doesn't use self or cls.
    # Just a helper utility function.
    # ------------------------------------------------------
    @staticmethod
    def line():

        # Print separator line
        print("-" * 60)


    # ------------------------------------------------------
    # Magic Method : __str__
    # ------------------------------------------------------
    # Automatically called when print(object) is used.
    # Gives a readable representation of the object.
    # ------------------------------------------------------
    def __str__(self):

        return (
            f"Report Title : {self.title}\n"
            f"Author       : {self.author}"
        )


    # ------------------------------------------------------
    # Magic Method : __len__
    # ------------------------------------------------------
    # Automatically called when len(object) is used.
    # Returns number of sections in the report.
    # ------------------------------------------------------
    def __len__(self):

        return len(self.contents)


    # ------------------------------------------------------
    # Decorated Display Function
    # ------------------------------------------------------
    # @report_decorator means that before executing this
    # function, Python first executes the decorator.
    # ------------------------------------------------------
    @report_decorator
    def display_report(self):

        # Display company name
        print("Company :", Report.company_name)

        # Automatically calls __str__()
        print(self)

        # Print separator line
        Report.line()

        print("Report Contents:")

        # enumerate() automatically creates numbering
        for i, item in enumerate(self.contents, start=1):

            print(f"{i}. {item}")

        # Print separator line
        Report.line()

        # Automatically calls __len__()
        print("Total Sections :", len(self))


# ==========================================================
# Main Program Starts Here
# ==========================================================

# ----------------------------------------------------------
# Create First Object
# ----------------------------------------------------------

r1 = Report(
    "Advanced Python Practical Report",
    "Mandar Joshi"
)

# Add report sections

r1.add_content("Completed Experiment No. 2 successfully.")

r1.add_content(
    "Implemented Decorators, Class Methods, Static Methods and Magic Methods."
)

r1.add_content(
    "Learned Object-Oriented Programming concepts."
)

r1.add_content(
    "Report prepared by Mandar Joshi."
)

# Display first report
r1.display_report()


# ----------------------------------------------------------
# Change Company Name
# ----------------------------------------------------------

print("\nChanging Company Name...\n")

# Change class variable using class method
Report.change_company("MIT ADT University")


# ----------------------------------------------------------
# Create Second Object
# ----------------------------------------------------------

r2 = Report(
    "Faculty Practical Demonstration",
    "Mandar Joshi"
)

# Add contents

r2.add_content("Practical demonstrated successfully.")

r2.add_content("Students understood decorators.")

r2.add_content("Students understood class methods.")

r2.add_content("Students understood magic methods.")

r2.add_content("Students performed the practical successfully.")

# Display second report
r2.display_report()


# ==========================================================
# End of Program
# ==========================================================

