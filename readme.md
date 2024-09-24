# ADHD Algorithm Simulation

This project simulates an ADHD-like brain using Python. The algorithm incorporates behaviors such as impulsivity, hyperactivity, hyperfocus, sleep deprivation, and addiction.

## Installation

1. **Clone the repository**:  
   ```bash
   https://github.com/jeffryhawchab/adhd_brain_algorithm
   cd adhd_brain_algorithm
   ```

2. **Set up a virtual environment** (optional but recommended):  
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:  
   - On Windows:  
     ```bash
     .\env\Scripts\activate
     ```  
   - On macOS and Linux:  
     ```bash
     source env/bin/activate
     ```

4. **Install requirements**:  
   Since this project only uses Python's built-in libraries, no additional packages are required.

## Code Explanation

The `ADHDBrain` class simulates the behavior of an ADHD brain. Here’s a breakdown of its components:

- **Attributes**:
  - `memory`: A deque that stores old memories, simulating the tendency to forget recent information.
  - `switch_prob`: Probability of switching tasks, representing impulsivity.
  - `impulsivity_threshold`: A threshold for taking impulsive actions.
  - `hyperfocus_chance`: Probability of entering hyperfocus on a task.
  - `energy_level`: Represents the energy status of the brain.
  - `sleep_deprivation_threshold`: The energy level below which the brain suffers from sleep deprivation.
  - `current_task`: The task currently being worked on.
  - `tasks`: A list of potential tasks to perform, including study, clean, code, etc.
  - `addiction_task`: A task that the brain prefers when in an addicted state.
  - `addiction_prob`: Probability of prioritizing addictive tasks.
  - `completed_tasks` and `interrupted_tasks`: Lists to track task performance.

- **Methods**:
  - `remember(info)`: Stores information in memory, retaining older memories while forgetting recent ones.
  - `forget_recent()`: Forgets the newest memories while keeping older ones.
  - `impulsive_action()`: Takes impulsive actions by switching to new tasks.
  - `perform_task(task)`: Simulates performing a task, with interruptions and hyperfocus.
  - `get_distracted()`: Simulates distraction from the current task.
  - `switch_task()`: Randomly switches between tasks.
  - `run_brain_simulation()`: Simulates the ADHD brain processing over time.
  - `check_sleep()`: Forces the brain to sleep if energy is critically low.
  - `check_addiction()`: Prioritizes addictive tasks when addiction takes over.

## Usage

To run the simulation, execute the following command:

```bash
cd src/
python main.py
```

This will start the simulation of the ADHD brain, processing various tasks while demonstrating impulsivity, hyperfocus, and other characteristics.

## License

This project is open-source and available under the MIT License.
