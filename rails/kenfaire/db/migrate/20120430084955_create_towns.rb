class CreateTowns < ActiveRecord::Migration
  def change
    create_table :towns do |t|
      t.string :name, :null => false
      t.references :city, :null => false
      t.integer :distance, :null => false

      t.timestamps
    end
    add_index :towns, :city_id
  end
end
