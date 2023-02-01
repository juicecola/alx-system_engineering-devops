#!/usr/bin/env ruby
#matches string starts with h ends with n can have any single xter in between
puts ARGV[0].scan(/h.n/).join
