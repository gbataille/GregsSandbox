# Load the rails application
require File.expand_path('../application', __FILE__)

# Initialize the rails application
Kenfaire::Application.initialize!

#Change the output of errors (from validators)
ActionView::Base.field_error_proc = Proc.new do |html_tag, instance_tag|
  "<span class=\"errors\">#{html_tag}</span>".html_safe
end
