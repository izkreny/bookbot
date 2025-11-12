# frozen_string_literal: true

def main
  if ARGV.empty?
    puts 'Usage: ruby main.rb <path_to_book>'
    return 1
  end

  book_path = ARGV.first
  text = File.read(book_path)
  number_of_words = text.split.length
  characters_occurrence = text.downcase.chars.tally
  characters_occurrence_sorted_list = sort_characters_occurrence(characters_occurrence)

  print_report(book_path, number_of_words, characters_occurrence_sorted_list)
end

def sort_characters_occurrence(characters)
  characters
    .sort_by { |key, value| [-value, key] }
    .map { |key, value| { char: key, num: value } }
end

def print_report(book_path, number_of_words, characters_occurrence_sorted_list)
  puts '============ BOOKBOT ============'
  puts "Analyzing book found at #{book_path}..."

  puts '----------- Word Count ----------'
  puts "Found #{number_of_words} total words"

  puts '--------- Character Count -------'
  characters_occurrence_sorted_list.each do |character|
    puts "#{character[:char]}: #{character[:num]}" if character[:char].match?(/[[:alpha:]]/)
  end

  puts '============= END ==============='
end

main

# TODO: Error handling and safe file operations while reading file: https://betterstack.com/community/guides/scaling-ruby/files-in-ruby/#error-handling-and-safe-file-operations
