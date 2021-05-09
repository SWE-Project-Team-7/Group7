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
using System.Data.SqlClient;

namespace PartsTrackerApp
{
    /// <summary>
    /// Interaction logic for UpdatePart.xaml
    /// </summary>
    public partial class UpdatePart : Window
    {
        private string part;
        private string[] originalNames = new string[4];
        private int key;

        public UpdatePart(string partNum)
        {
            this.part = partNum;
            InitializeComponent();
        }

        private void UpdatePartsWindow_Loaded(object sender, RoutedEventArgs e)
        {
            string connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            string sqlSelect = "SELECT * FROM Parts WHERE [Part Number] = '" + part + "'";
            SqlConnection conn = new SqlConnection(connString);

            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    originalNames[0] = rdr["Name"].ToString();
                    originalNames[1] = rdr["Part Number"].ToString();
                    originalNames[2] = rdr["Location"].ToString();
                    originalNames[3] = rdr["Unit Family"].ToString();

                    partNameTextBox.Text = rdr["Name"].ToString();
                    partNumberTextBox.Text = rdr["Part Number"].ToString();
                    locationTextBox.Text = rdr["Location"].ToString();
                    unitFamilyComboBox.Text = rdr["Unit Family"].ToString();
                    key = Int32.Parse(rdr["Id"].ToString());

                    //MessageBox.Show("Primary Key: " + key);
                }
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

        private void UpdateButton_Click(object sender, RoutedEventArgs e)
        {
            string partName = partNameTextBox.Text.Trim();
            string partNumber = partNumberTextBox.Text.Trim();
            string location = locationTextBox.Text.Trim();
            string unitFamily = unitFamilyComboBox.Text.Trim();
            bool inputsValid;

            inputsValid = ValidateInputs(partName, partNumber, location, unitFamily);

            if (inputsValid == true)
            {
                SQLUpdateFunction(partName, partNumber, location, unitFamily);
                MessageBox.Show("Update Completed", "Success");
                this.Close();
            }
            else
            {
                MessageBox.Show("Update cannot be performed.", "Error");
                partNameTextBox.Text = originalNames[0];
                partNumberTextBox.Text = originalNames[1];
                locationTextBox.Text = originalNames[2];
                unitFamilyComboBox.Text = originalNames[3];
            }        
        }

        private void SQLUpdateFunction(string name, string partNum, string loc, string unitFam)
        {
            string connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            string sqlSelect = "UPDATE Parts SET Name = '" + name + "', [Part Number] = '" + partNum + "', Location = '" + loc.ToUpper() + "', " +
                               "[Unit Family] = '" + unitFam + "'  WHERE [Id] = '" + key + "'";
     
            SqlConnection conn = new SqlConnection(connString);
            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                cmd.ExecuteReader();     
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

        private Boolean ValidateInputs(string pName, string pNum, string loc, string unitFam)
        {
            bool valid = true;

            if (string.IsNullOrEmpty(pName))
            {
                DisplayErrorMessage("Part Name field is empty.");
                return false;
            }

            for (int i = 0; i < pName.Length; i++)
            {
                char nameChar = pName[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Part Name has an \ninvalid character(s).");
                    return false;
                }
            }

            char pNameChar;
            int spCtr = 0;

            for (int i = 0; i < pName.Length; i++)
            {
                pNameChar = pName[i];

                if (Char.IsWhiteSpace(pNameChar))
                    spCtr++;

                if (spCtr > 1)
                {
                    DisplayErrorMessage("Part Name has an invalid space");
                    return false;
                }
            }

            if (string.IsNullOrEmpty(pNum))
            {
                DisplayErrorMessage("Part Number field is empty.");
                return false;
            }

            for (int i = 0; i < pNum.Length; i++)
            {
                char nameChar = pNum[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Part Number has an \ninvalid character(s).");
                    return false;
                }
            }

            if(pNum.Contains(" "))
            {
                DisplayErrorMessage("Part Number has an invalid space.");
                return false;
            }

            if (string.IsNullOrEmpty(loc))
            {
                DisplayErrorMessage("Location field is empty.");
                return false;
            }

            for (int i = 0; i < loc.Length; i++)
            {
                char nameChar = loc[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Location has an \ninvalid character(s).");
                    return false;
                }
            }

            if(loc.Contains(" "))
            {
                DisplayErrorMessage("Location has an invalid space.");
                return false;
            }

            if (unitFamilyComboBox.SelectedIndex == 0)
                unitFam = unitFamilyComboBox.Text;
            else if (unitFamilyComboBox.SelectedIndex == 1)
                unitFam = unitFamilyComboBox.Text;
            else if (unitFamilyComboBox.SelectedIndex == 2)
                unitFam = unitFamilyComboBox.Text;
            else
            {
                DisplayErrorMessage("No Unit Family category was selected.");
                return false;
            }

            if(PartNumValid(pName, pNum) == false)
            {
                DisplayErrorMessage("Part already exists.");
                return false;
            }


            if(UnitFamValid(pName, unitFam) == false)
            {
                DisplayErrorMessage("Part Already exists.");
                return false;
            }
     
            return valid;
        }

        private Boolean CharChecker(char strChar)
        {
            bool check = true;

            char[] specialChars = new char[] {'~', '`', '!', '@', '#', '$', '%', '^', '&', '*',
                                              '(', ')', '_', '+', '=', '{', '}', '[', ']', '|',
                                              ':', ';', '<', '>', '?', '\\' };

            for (int i = 0; i < specialChars.Length; i++)
            {
                if (strChar == specialChars[i])
                    check = false;
            }

            return check;
        }
        
        private Boolean PartNumValid(string partName, string partNum)
        {
            bool partValid = true;

            string connString;
            string sqlSelect;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            sqlSelect = "SELECT Name, [Part Number] FROM Parts EXCEPT SELECT Name, [Part Number] FROM Parts WHERE Id = '" + key + "'";

            SqlConnection conn = new SqlConnection(connString);
            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {            
                    string dbName = rdr["Name"].ToString().ToUpper();
                    string dbPartNum = rdr["Part Number"].ToString().ToUpper();

                    if ((partName.ToUpper() == dbName) && (partNum.ToUpper() == dbPartNum))
                        partValid = false;
                }

            }
            catch (SqlException ex)
            {
                MessageBox.Show(ex.Message + ex.StackTrace, "Exception Details");
            }
            finally
            {
                conn.Close();
            }

            return partValid;
        }
        
        private Boolean UnitFamValid(string partName, string unitFam)
        {
            bool unitFamValid = true;

            string connString;
            string sqlSelect;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            sqlSelect = "SELECT Name, [Unit Family] FROM Parts EXCEPT SELECT Name, [Unit Family] FROM Parts WHERE Id = '" + key + "'";

            SqlConnection conn = new SqlConnection(connString);
            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    string dbName = rdr["Name"].ToString().ToUpper();
                    string dbUnitFam = rdr["Unit Family"].ToString().ToUpper();

                    if ((partName.ToUpper() == dbName) && (unitFam.ToUpper() == dbUnitFam))
                        unitFamValid = false;                
                }

            }
            catch (SqlException ex)
            {
                MessageBox.Show(ex.Message + ex.StackTrace, "Exception Details");
            }
            finally
            {
                conn.Close();
            }

            return unitFamValid;
        }

       
        private void DisplayErrorMessage(string message)
        {
            MessageBox.Show(message, "Error");
        }       
    }
}
