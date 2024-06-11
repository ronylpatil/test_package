# now no need to import like "import test_package.add import addition" directly we can import "from test_package import addition"
# add full import here and we can use shorthands while actually importing as package
from test_package.add import addition, subtraction, division
from test_package.custom_exception import InvalidUserInput