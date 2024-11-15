import click

import just_count.square as square


@click.command()
@click.argument("number", type=int)
def main(number):
    print(f"The square of {number} is {square.square(number)}")


if __name__ == "__main__":
    main()
# main()
