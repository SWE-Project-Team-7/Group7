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
using Microsoft.VisualBasic;

namespace PartsTrackerApp
{
    /// <summary>
    /// Interaction logic for ManageParts.xaml
    /// </summary>
    public partial class ManageParts : Window
    {
        public ManageParts()
        {
            InitializeComponent();
            keyTextBox.Focus();
        }



        private void SearchButton_Click(object sender, RoutedEventArgs e)
        {
            string keyword = keyTextBox.Text.Trim();
            bool inputsValid;

            
            inputsValid = ValidateInputs(keyword);

            if (!(partListBox.Items.IsEmpty))
            {
                MessageBox.Show("List has elements,\nneeds to be cleared.", "Error");
                clearButton.Focus();
            }
            else if (inputsValid == true)
            {
                SearchFunction(keyword);

                if (partListBox.Items.IsEmpty)
                {
                    MessageBox.Show("Part(s) not found", "Error");
                    keyTextBox.Focus();
                }

                keyTextBox.Clear();
            }
            else
            {
                keyTextBox.Clear();
                keyTextBox.Focus();
            }
        }

        private void ClearButton_Click(object sender, RoutedEventArgs e)
        {
            if (partListBox.Items.IsEmpty)
            {
                MessageBox.Show("No parts available \nto be cleared.", "Error");
                keyTextBox.Focus();
            }
            else
            {
                partListBox.Items.Clear();
                searchPartTextBox.Clear();
                keyTextBox.Clear();
                keyTextBox.Focus();
                optionsComboBox.SelectedIndex = -1;
            }
        }

        private void BackButton_Click(object sender, RoutedEventArgs e)
        {
            MainWindow main = new MainWindow();
            main.Show();
            this.Close();
        }


        private void SubmitButton_Click(object sender, RoutedEventArgs e)
        {
            string searchedPart = searchPartTextBox.Text;
            bool submitValid;

            submitValid = SubmitValidation(searchedPart);

            if (submitValid == true)
                SubmitFunction(searchedPart);
            
        }

        private void SearchFunction(string keyword)
        {
            string connString;
            string sqlSearch;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";;
            sqlSearch = "SELECT Name, [Part Number] FROM Parts WHERE CHARINDEX('"+ keyword + "', Name) > 0 OR CHARINDEX('" + keyword + "', [Part Number]) > 0";

            SqlConnection conn = new SqlConnection(connString);

            SqlCommand cmd = new SqlCommand(sqlSearch, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while(rdr.Read())
                {
                    this.partListBox.Items.Add(rdr["Name"].ToString() + "\t" + rdr["Part Number"].ToString());
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
        }

        private void SubmitFunction(string part)
        {
            if ((optionsComboBox.SelectedIndex == 0))
            {
                SqlViewFunciton(part);
            }
            else if ((optionsComboBox.SelectedIndex == 1))
            {
                if (PartExist(part) == true)
                {
                    UpdatePart update = new UpdatePart(part);
                    update.Show();
                    partListBox.Items.Clear();
                    searchPartTextBox.Clear();
                    keyTextBox.Clear();
                    optionsComboBox.SelectedIndex = -1;
                }
                else
                    MessageBox.Show("This part does not exist", "Error");
            }
            else if ((optionsComboBox.SelectedIndex == 2))
            {
                SQLDeleteFunction(part);
            }
            else
                MessageBox.Show("You have must select a function.", "Error");
        }

        private void SqlViewFunciton(string part)
        {

            Part aPart;
            string connString;
            string sqlSearch;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True"; ;
            sqlSearch = "SELECT * FROM Parts WHERE [Part Number] = '" + part + "'";

            SqlConnection conn = new SqlConnection(connString);

            SqlCommand cmd = new SqlCommand(sqlSearch, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                while (rdr.Read())
                {
                    aPart = new Part(rdr["Name"].ToString(), rdr["Part Number"].ToString(), rdr["Location"].ToString(), rdr["Unit Family"].ToString());
                        MessageBox.Show(aPart.ToString(), "Part Information");
                }

                if (!(rdr.HasRows))
                    MessageBox.Show("Part does not exist.", "Error");
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

        private void SQLDeleteFunction(string part)
        {
            string connString;
            string sqlSearch;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True"; ;
            sqlSearch = "DELETE FROM Parts WHERE [Part Number] = '" + part + "'";

            SqlConnection conn = new SqlConnection(connString);

            SqlCommand cmd = new SqlCommand(sqlSearch, conn);

            try
            {
                conn.Open();
                int del = cmd.ExecuteNonQuery();

                if(del > 0)
                    MessageBox.Show("Part deleted", "Message");
                else
                    MessageBox.Show("Part does not exist", "Error");

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

        private Boolean ValidateInputs(string keyword)
        {
            bool inputsValid = true;

            if (string.IsNullOrEmpty(keyword))
            {
                DisplayErrorMessage("Keyword Field is empty.");
                return false;
            }

            for (int i = 0; i < keyword.Length; i++)
            {
                char nameChar = keyword[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Part Name has an \ninvalid character(s).");
                    return false;
                }
            }

            return inputsValid;
        }

        
        private Boolean SubmitValidation(string part)
        {
            bool subValid = true;

            if (string.IsNullOrEmpty(part))
            {
                DisplayErrorMessage("Part Number Field is empty.");
                return false;
            }

            for (int i = 0; i < part.Length; i++)
            {
                char nameChar = part[i];

                if (CharChecker(nameChar) == false)
                {
                    DisplayErrorMessage("Part Name has an \ninvalid character(s).");
                    return false;
                }
            }

            return subValid;
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

        Boolean PartExist(string part)
        {
            bool exist = true;

            string connString;
            string sqlSelect;

            connString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Parts.mdf;Integrated Security=True";
            //sqlSelect = "SELECT * FROM Parts";
            sqlSelect = "SELECT * FROM Parts WHERE [Part Number] = '" + part + "'";

            SqlConnection conn = new SqlConnection(connString);
            SqlCommand cmd = new SqlCommand(sqlSelect, conn);

            try
            {
                conn.Open();
                SqlDataReader rdr = cmd.ExecuteReader();

                /*
                while(rdr.Read())
                {
                    string dbPartNum = rdr["Part Number"].ToString();

                    if (part != dbPartNum)
                        return exist = false;                
                }
                */
                if (rdr.HasRows == false)
                    exist = false;
            }
            catch(SqlException ex)
            {
                MessageBox.Show(ex.Message + ex.StackTrace, "Exception Details");
            }
            finally
            {
                conn.Close();
            }

            return exist;
        }

        private void DisplayErrorMessage(string message)
        {
            MessageBox.Show(message, "Error");
        }
        
    }
}
