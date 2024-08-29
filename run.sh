#!/bin/sh

# Function to display help
show_help() {
  echo "Usage: $0 <command> [args]"
  echo
  echo "Commands:"
  echo "  search          Search the top 30 economic journals for relevant articles"
  echo "  snowball        Snowball the search results to find more relevant articles"
  echo "  help            Display this help message"
}

# Check if no arguments were provided
if [ $# -eq 0 ]; then
  show_help
  exit 1
fi

# Main switch-case to handle commands
case "$1" in
search)
  shift
  python literature_search/main.py --search
  ;;
snowball)
  shift
  python literature_search/main.py --snowball
  ;;
help)
  show_help
  ;;
*)
  echo "Error: Unknown command: $1"
  show_help
  exit 1
  ;;
esac
