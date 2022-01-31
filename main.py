import turtle
snowflake = turtle.Turtle()
for i in range(10):
  for i in range(2):
    snowflake.forward(100)
    snowflake.right(60)
    snowflake.forward(100)
    snowflake.right(120)
  snowflake.right(36)