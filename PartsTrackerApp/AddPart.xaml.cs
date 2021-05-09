using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Configuration;
using System.Data.SqlClient;

namespace PartsTrackerApp
{
    /// <summary>
    /// Interaction logic for AddPart.xaml
    /// </summary>
    public partial class AddPart : Window
    {
        
        public AddPart()
        {
            InitializeComponent();
            partNameTextBox.Focus();
        }

        private void BackButton_Click(object sender, RoutedEventArgs e)
        {
            MainWindow main = new MainWindow();
            main.Show();
            this.Close();
        }

        private void SubmitButton_Click(object sender, RoutedEventArgs e)
        {
            string name = partNameTextBox.Text.Trim();
            string partNumber = partNumberTextBox.Text.Trim();
            string location = locationTextBox.Text.Trim();
            string unitFamily = unitFamilyComboBox.Text.Trim();
            bool inputsValid;

            inputsValid = ValidateInputs(name, partNumber, location, unitFamily);

            if(inputsValid == true)
                InsertFunction(name, partNumber, location, unitFamily);

        }

        private void InsertFunction(string name, string partNum, string loc, string unitFamily)
        {
            string connString;
            string sqlInsert;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            sqlInsert = "INSERT INTO PARTS (Name, [Part Number], [Unit Family],Location) VALUES ( '" + name + "', '" + partNum + "', '" + unitFamily + "','" + loc.ToUpper() + "')";
            //sqlInsert = "INSERT INTO PARTS (Name, [Part Number], Location) VALUES (@Name, @Part, @Location)";
            SqlConnection conn = new SqlConnection(connString);

            SqlCommand cmd = new SqlCommand(sqlInsert, conn);

            /*
            cmd.Parameters.AddWithValue("@Name", name);
            cmd.Parameters.AddWithValue("@Part", partNumber);
            cmd.Parameters.AddWithValue("@Location", location);   
            */

            try
            {
                conn.Open();
                cmd.ExecuteNonQuery();

                MessageBox.Show("Part successfully added!", "Success");

                partNameTextBox.Focus();
                partNameTextBox.Clear();
                partNumberTextBox.Clear();
                locationTextBox.Clear();
                unitFamilyComboBox.SelectedIndex = -1;
            }
            catch (SqlException ex)
            {
                MessageBox.Show(ex.Message + ex.StackTrace, "Exception Details");
            }
            finally
            {
                conn.Close();
            }
        }

        private Boolean ValidateInputs(string name, string partNum, string location, string unitFamily)
        {
            Boolean inputsValid = true;

            if(string.IsNullOrEmpty(name))
            {
                DisplayErrorMessage("Part Name field is empty.");
                return false;
            }

            for(int i = 0; i < name.Length; i++)
            {
                char nameChar = name[i];

                if(CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Part Name has an \ninvalid character(s).");
                    return false;
                }
            }

            char pNameChar;
            int spCtr = 0;
            
            for(int i = 0; i < name.Length; i++)
            {
                pNameChar = name[i];

                if (Char.IsWhiteSpace(pNameChar))
                    spCtr++;

                if(spCtr > 1)
                {
                    DisplayErrorMessage("Part Name has an invalid space");
                    return false;
                }
            }

            if (string.IsNullOrEmpty(partNum))
            {
                DisplayErrorMessage("Part Number field is empty.");
                return false;
            }

            for (int i = 0; i < partNum.Length; i++)
            {
                char nameChar = partNum[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Part Number has an \ninvalid character(s).");
                    return false;
                }
            }

            if(partNum.Contains(" "))
            {
                DisplayErrorMessage("Part Number has an invalid space");
                return false;
            }

            if (string.IsNullOrEmpty(location))
            {
                DisplayErrorMessage("Location field is empty.");
                return false;
            }

            if(location.Contains(" "))
            {
                DisplayErrorMessage("Location has an invalid space.");
                return false;
            }

            for (int i = 0; i < location.Length; i++)
            {
                char nameChar = location[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Location has an \ninvalid character(s).");
                    return false;
                }
            }

            if (unitFamilyComboBox.SelectedIndex == 0)
                unitFamily = unitFamilyComboBox.Text;
            else if (unitFamilyComboBox.SelectedIndex == 1)
                unitFamily = unitFamilyComboBox.Text;
            else if (unitFamilyComboBox.SelectedIndex == 2)
                unitFamily = unitFamilyComboBox.Text;
            else
            {
                DisplayErrorMessage("No Unit Family category was selected.");
                return false;
            }

            if(DuplicateChecker(name, partNum,unitFamily) == false)
            {
                DisplayErrorMessage("Part already exists.");
                return false;
            }
            
            return inputsValid;
        }
        
        private Boolean CharChecker(char strChar)
        {
            bool check = true;
                 
            char[] specialChars = new char[] {'~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
                                              '(', ')', '_', '+', '=', '{', '}', '[', ']', '|',
                                              ':', ';', '<', '>', '?', '\\' };

            for(int i = 0; i < specialChars.Length; i++)
            {
                if (strChar == specialChars[i])
                    check = false;
            }

            return check;
        }

        private Boolean DuplicateChecker(string name, string partNum, string unitFamily)
        {
            bool check = true;
            string connString;
            string sqlSelect;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            sqlSelect = "SELECT Name, [Part Number],[Unit Family] FROM Parts";

            SqlConnection conn = new SqlConnection(connString);
            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    if (string.IsNullOrEmpty(rdr["Name"].ToString()) && 
                        string.IsNullOrEmpty(rdr["Part Number"].ToString()) && 
                        string.IsNullOrEmpty(rdr["Unit Family"].ToString()))
                        break;

                    string dbName = rdr["Name"].ToString().ToUpper();
                    string dbUnitFam = rdr["Unit Family"].ToString().ToUpper();
                    string dbPartNum = rdr["Part Number"].ToString().ToUpper();

                    if ((name.ToUpper() == dbName) && (partNum.ToUpper() == dbPartNum))
                        check = false;

                    if ((name.ToUpper() == dbName) && (unitFamily.ToUpper() == dbUnitFam))
                        check = false;                    
                }

            }
            catch(SqlException ex)
            {
                MessageBox.Show(ex.Message + ex.StackTrace, "Exception Details");
            }
            finally
            {
                conn.Close();
            }

            return check;
        }
        
        private void DisplayErrorMessage(string message)
        {
            MessageBox.Show(message, "Error");
        }
    }
}
