import click

@click.command()
@click.option('--count', default=1, help='Number of Greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')

def hello(count, name): 
    '''Greets a input name for a count number of times'''
    for x in range(count): 
        click.echo('Hello %s!' % name)

if __name__ == '__main__': 
    hello()

