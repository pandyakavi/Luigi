import luigi
import os

class MyFirstTask(luigi.Task): # inherit from Luigi base class Task

    def run(self):
        os.system('python JupNb1.py.py')
            
    def output(self):
        return luigi.LocalTarget('JupNb1Content.txt')

class MySecondTask(luigi.Task):
    # MyFirstTask() needs to run first
    upstream_task = luigi.Parameter(default=MyFirstTask())
    def run(self):
        os.system('python JupNb2.py')

    def output(self):
        return luigi.LocalTarget('JupNb2Content.txt')


if __name__ == '__main__':

    # since we are setting MySecondTask to be the main task,
    # it will check for the requirements first, then run
    luigi.run(main_task_cls=MySecondTask)
