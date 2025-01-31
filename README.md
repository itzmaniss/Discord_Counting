# Discord_Counting
Better Counting Bot
 # Discord Counting Bot

A sophisticated Discord bot that turns counting into an engaging mathematical adventure. This bot supports sequential counting with mathematical expressions, tracks user statistics, and offers special recognition for prime numbers.

## Features

The Discord Counting Bot enriches your server's counting experience with these capabilities:

- Mathematical expression evaluation (e.g., "2+2", "sqrt(16)")
- Natural language number processing (e.g., "four", "twenty")
- Prime number detection and tracking
- Comprehensive user statistics
- Multiple leaderboard categories
- Error prevention and handling
- Milestone celebrations

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Discord Bot Token
- Required Python packages (specified in requirements.txt)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/discord_counting.git
cd discord_counting
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the project root with the following variables:
```
discord_token=your_bot_token_here
command_prefix=your_preferred_prefix
COUNTING_CHANNELS=channel1,channel2
```

4. Run the bot:
```bash
python main.py
```

## Commands

The bot responds to these commands:

- `/count_help` - Displays help information and counting rules
- `/count_stats [@user]` - Shows counting statistics for a user
- `/count_top` - Displays the top counters leaderboard
- `/prime_top` - Shows the top prime number counters
- `/fail_top` - Lists users with the most counting failures
- `/next_prime` - Reveals the next prime number in sequence

## Counting Rules

The bot enforces these counting rules:

1. Each number must be the next in sequence
2. Users cannot count twice in a row
3. Mathematical expressions must evaluate to the correct next number
4. The bot validates all inputs before accepting them

## Reactions

The bot uses these reactions to provide feedback:

- ✅ - Correct number
- 🔢 - Prime number
- ❌ - Wrong number/Failed attempt

## Technical Details

The bot utilizes these key components:

- SQLite database for persistent storage
- Safe mathematical expression evaluation
- Word-to-number conversion
- Prime number detection
- Comprehensive logging system

The code is structured into three main modules:

- `main.py` - Bot initialization and command handling
- `helper.py` - Core counting logic and database operations
- `logger.py` - Logging functionality

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.