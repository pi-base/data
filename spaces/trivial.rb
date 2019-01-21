spaces = Dir.glob("*").select{ |f| f[0] == "S" }.each do |space|
  trait = <<-HEREDOC
---
space: #{space}
property: P100052
value: false
---

The space is non-trivial by definition.
  HEREDOC
  filename = "#{space}/properties/P100052.md"
  if File.exist?(filename)
    puts "wrote #{space}"
    File.open(filename,"w") {|f| f.write trait}
  end
end 
