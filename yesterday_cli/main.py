import argparse
import datetime


def cli():
    parser = argparse.ArgumentParser(description="Tell you what day was yesterday.")
    parser.add_argument("-d", "--date", action="store_true", help="print yesterday's full date")
    parser.add_argument("-q", "--quiet", action="store_true", help="just output the date, no text")
    args = parser.parse_args()

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

    output = []
    if not args.quiet:
        output.append("Yesterday was")
    if args.date:
        output.append(yesterday.strftime("%Y-%m-%d"))
    else:
        output.append(yesterday.strftime("%A"))

    print(" ".join(output))


if __name__ == "__main__":
    cli()
