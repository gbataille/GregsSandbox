class User < ActiveRecord::Base
  #Create a model attribute that is NOT in the database
  attr_accessor :pwd
  #Validators (triggered on save! action)
  validates_presence_of :email
  validates_uniqueness_of :email
  validates_presence_of :username
  validates_uniqueness_of :username
  validates_presence_of :pwd, :on => :create
  validates_confirmation_of :pwd
  #validates_presence_of :pwd_confirmation, :on => :create

  #Hooks
  before_save :encrypt_password

  def encrypt_password
    self.password_salt = BCrypt::Engine.generate_salt()
    self.password_hash = BCrypt::Engine.hash_secret(pwd, password_salt)
  end
end
