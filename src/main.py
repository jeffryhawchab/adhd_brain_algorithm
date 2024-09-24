import random
import time
from collections import deque

class ADHDBrain:
    def __init__(self, max_memory_size=10, switch_prob=0.5, impulsivity_threshold=0.7, hyperfocus_chance=0.2):
        # Working memory retains only older memories
        self.memory = deque(maxlen=max_memory_size)
        self.switch_prob = switch_prob  # Probability of switching tasks
        self.impulsivity_threshold = impulsivity_threshold  # Threshold for impulsive actions
        self.hyperfocus_chance = hyperfocus_chance  # Probability of entering hyperfocus
        
        # Sleep-related properties
        self.energy_level = 100  # Starts fully rested
        self.sleep_deprivation_threshold = 40  # Energy level where sleep deprivation impacts behavior
        
        self.current_task = None
        self.tasks = ['Study', 'Clean', 'Code', 'Exercise', 'Eat', 'Sleep', 'Social Media', 'Video Games']
        
        # Addiction (develop a strong preference for certain tasks)
        self.addiction_task = 'Social Media'  # Preferred task when addicted
        self.addiction_prob = 0.3  # Likelihood of prioritizing addictive tasks
        
        # Track task performance for simulation
        self.completed_tasks = []
        self.interrupted_tasks = []
    
    def remember(self, info):
        """ Store information in memory. Remembers old info but forgets new info quickly. """
        print(f"Remembering: {info}")
        self.memory.append(info)
    
    def forget_recent(self):
        """ Forgets new memories but keeps older ones. """
        if len(self.memory) > 5:  # Arbitrary threshold for forgetting new things
            forgotten = self.memory.pop()  # Forget the newest item
            print(f"Forgot: {forgotten}")
    
    def impulsive_action(self):
        """ Impulsively act on a task, or start a new one without planning. """
        if random.random() > self.impulsivity_threshold:
            new_task = random.choice(self.tasks)
            print(f"Impulsively switching to a new task: {new_task}")
            self.interrupted_tasks.append(self.current_task)  # Current task interrupted
            self.current_task = new_task
            self.perform_task(self.current_task)
    
    def perform_task(self, task):
        """ Perform the current task, but frequently gets distracted. """
        print(f"Starting task: {task}")
        
        # If energy is too low, suffer from sleep deprivation
        if self.energy_level < self.sleep_deprivation_threshold:
            print("Suffering from sleep deprivation!")
            self.switch_prob *= 1.5  # Increase chance of switching tasks due to tiredness
        
        # Hyperfocus - Occasionally the brain locks onto a task
        if random.random() < self.hyperfocus_chance:
            print(f"Entering hyperfocus mode on {task}. Will ignore distractions.")
            time_spent = 5
            time.sleep(5)  # Simulate hyperfocus time, ignoring interruptions
        else:
            time_spent = 0
        
        while time_spent < 5:
            if random.random() < self.switch_prob:
                print(f"Interrupted while performing: {task}")
                self.interrupted_tasks.append(task)
                new_task = random.choice(self.tasks)
                self.current_task = new_task
                self.perform_task(new_task)
                return
            
            # Simulate focus on the current task
            time.sleep(1)  # 1 second represents a time slice of work
            time_spent += 1
            print(f"Focused on {task} for {time_spent} seconds.")
        
        # If task completes, log it
        print(f"Completed task: {task}")
        self.completed_tasks.append(task)
    
    def get_distracted(self):
        """ Simulates distraction, pulling attention away from current task. """
        distraction_level = random.random()
        if distraction_level > 0.5:
            print("Got distracted by external stimuli!")
            new_task = random.choice(self.tasks)
            self.interrupted_tasks.append(self.current_task)
            self.perform_task(new_task)
    
    def switch_task(self):
        """ Frequently switches between tasks randomly. """
        if random.random() < self.switch_prob:
            print(f"Switching from {self.current_task} to a new task.")
            new_task = random.choice(self.tasks)
            self.interrupted_tasks.append(self.current_task)
            self.current_task = new_task
            self.perform_task(new_task)
    
    def run_brain_simulation(self):
        """ Simulates the ADHD brain processing over time. """
        initial_task = random.choice(self.tasks)
        self.current_task = initial_task
        print(f"Initial task: {initial_task}")
        self.perform_task(initial_task)
        
        for _ in range(10):  # Simulate a day in the brain
            self.switch_task()  # Randomly switch tasks
            self.impulsive_action()  # Sometimes act impulsively
            self.get_distracted()  # Occasionally get distracted
            self.check_addiction()  # Prioritize addictive tasks if addicted
            self.remember(f"Task performed: {self.current_task}")
            self.forget_recent()  # Forget the most recent thing
            self.energy_level -= 10  # Simulate energy loss over time (sleep deprivation)
            self.check_sleep()  # Check if sleep is needed
            time.sleep(1)  # Wait before next brain cycle

        print("\n--- Summary ---")
        print(f"Completed tasks: {self.completed_tasks}")
        print(f"Interrupted tasks: {self.interrupted_tasks}")
        print(f"Remaining memory: {list(self.memory)}")
        print(f"Final energy level: {self.energy_level}")

    def check_sleep(self):
        """ Forces the brain to sleep if energy is critically low. """
        if self.energy_level < 20:  # Force sleep if energy is too low
            print("Energy critically low! Must sleep.")
            self.perform_task('Sleep')
            self.energy_level = 100  # Restore energy after sleep

    def check_addiction(self):
        """ Prioritize addictive tasks when addiction takes over. """
        if random.random() < self.addiction_prob:
            print(f"Addiction takes over. Prioritizing {self.addiction_task}.")
            self.perform_task(self.addiction_task)

# Simulate the ADHD Brain with hyperactivity, hyperfocus, lack of sleep, and addiction
adhd_brain = ADHDBrain()
adhd_brain.run_brain_simulation()
