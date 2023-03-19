import sys
import difflib
import subprocess

def compare_files(file_path_1, file_path_2):
    with open(file_path_1, 'r') as file_1, open(file_path_2, 'r') as file_2:
        file_1_contents = file_1.read()
        file_2_contents = file_2.read()
        if file_1_contents == file_2_contents:
            return True
        else:
            return False
        

def display_file_diff(file_path_1, file_path_2):
    with open(file_path_1, 'r') as file_1, open(file_path_2, 'r') as file_2:
        file_1_contents = file_1.readlines()
        file_2_contents = file_2.readlines()

    diff = difflib.unified_diff(file_1_contents, file_2_contents)

    print(''.join(diff))

def execute_command_in_directory(command, directory):
    output = subprocess.run(command, shell=True, cwd=directory, capture_output=True, text=True)
    return output

if __name__ == '__main__':
    fp = sys.argv[1]
    arr = {chr(i): chr(i) for i in range(ord('A'), ord('I')+1)}
    arr['A'] = "Priority Scheduler 1 - Given Test Case"
    arr['B'] = "Priority Scheduler 2 - Multiple Processes Same Priority"
    arr['C'] = "Priority Scheduler 3 - Duplicate Resource Names"
    arr['D'] = "Priority Scheduler 4 - Long Boy"
    arr['E'] = "FCFS 1 - Given Test Case"
    arr['F'] = "FCFS 2 - Long Test Case"
    arr['G'] = 'Deadlock 1 (Priority Scheduler) - Multiple Deadlocks'
    arr['H'] = "Priority Scheduler 5 - Longer Boy"
    arr['I'] = "FCFS 3 - Longer Test Case"
    arr['J'] = 'Deadlock 2 (Priority Scheduler) - Two Proccesses Locked'

    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

    for i in arr:
        execute_command_in_directory('make clean', fp)
        execute_command_in_directory('make', fp)
        if arr[i].startswith("Priority") == True or arr[i].startswith("Deadlock"):
            execute_command_in_directory('./schedule_processes ../../../TestSuiteProcMan/TestIn/process' + i + '1.list ../../../TestSuiteProcMan/TestIn/process' + i + '2.list 0 2', fp)
        else: 
            execute_command_in_directory('./schedule_processes ../../../TestSuiteProcMan/TestIn/process' + i + '1.list ../../../TestSuiteProcMan/TestIn/process' + i + '2.list 2 2', fp)

        if compare_files(fp + "scheduler.log", "TestOut/" + i+ ".log"): 
            print(f'{GREEN}[PASSED]{END} {arr[i]}')    
        else: 
            print(f'{RED}[FAILED]{END} {arr[i]}')
            print(f'{RED}Differences:{END} \n')
            display_file_diff(fp + "scheduler.log", "TestOut/A.log")
